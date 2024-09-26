import aiohttp
import asyncio
import json
import os
import requests
import base64
from PIL import Image
from io import BytesIO
from config import OPENROUTER_KEY, SYSTEM_PROMPT, SYSTEM_PROMPT_IMG, REPLICATE_API_TOKEN, REPLICATE_MODEL, REPLICATE_GUIDANCE, STABLE_DIFFUSION_URL, IMAGE_DIRECTORY

class OpenRouterAPI:
    def __init__(self):
        self.api_key = OPENROUTER_KEY
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def generate_stream(self, prompt):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.base_url,
                headers=self.headers,
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": True
                }
            ) as response:
                async for line in response.content:
                    if line:
                        try:
                            json_line = json.loads(line.decode('utf-8').split('data: ')[1])
                            if 'choices' in json_line and len(json_line['choices']) > 0:
                                delta = json_line['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    yield delta['content']
                        except json.JSONDecodeError:
                            pass
                        except IndexError:
                            pass

async def generate_response(conversation_history, api_type, api_key):
    api = OpenRouterAPI()
    full_prompt = SYSTEM_PROMPT + "\n\n" + "\n".join([f"{role}: {content}" for role, content in conversation_history])
    return api.generate_stream(full_prompt)

async def generate_image_prompt(context):
    api = OpenRouterAPI()
    full_prompt = SYSTEM_PROMPT_IMG + "\n\n" + context + "\n\nGenerate a prompt for an image in the style of pixel art, 80s video game, or 80s RPG game."
    response = ""
    async for token in api.generate_stream(full_prompt):
        response += token
    return response.strip()

async def generate_image(prompt, method):
    if method == 'replicate':
        return await generate_image_replicate(prompt)
    elif method == 'local_sd':
        return await generate_image_local_sd(prompt)
    else:
        raise ValueError(f"Unknown image generation method: {method}")

async def generate_image_replicate(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "version": REPLICATE_MODEL,
        "input": {
            "prompt": prompt,
            "guidance_scale": REPLICATE_GUIDANCE
        }
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            result = await response.json()
    
    # Poll for the result
    while result['status'] != 'succeeded':
        await asyncio.sleep(1)
        async with aiohttp.ClientSession() as session:
            async with session.get(result['urls']['get'], headers=headers) as response:
                result = await response.json()
    
    # Download the image
    image_url = result['output'][0]
    image_path = os.path.join(IMAGE_DIRECTORY, f"replicate_image_{len(os.listdir(IMAGE_DIRECTORY))}.png")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            with open(image_path, 'wb') as f:
                f.write(await response.read())
    
    return image_path

async def generate_image_local_sd(prompt):
    payload = {
        "prompt": prompt,
        "steps": 50
    }
    
    try:
        response = requests.post(url=STABLE_DIFFUSION_URL, json=payload)
        response.raise_for_status()
        r = response.json()
        
        image_data = r['images'][0]
        image_bytes = base64.b64decode(image_data)
        
        # Use PIL to open and save the image
        image = Image.open(BytesIO(image_bytes))
        image_path = os.path.join(IMAGE_DIRECTORY, f"local_sd_image_{len(os.listdir(IMAGE_DIRECTORY))}.png")
        image.save(image_path, 'PNG')
        
        return image_path
    except Exception as e:
        print(f"Error generating image with local Stable Diffusion: {str(e)}")
        return None

async def test_api():
    api = OpenRouterAPI()
    prompt = "Tell me a short story about a brave adventurer."
    async for token in api.generate_stream(prompt):
        print(token, end='', flush=True)
    print()

if __name__ == "__main__":
    asyncio.run(test_api())