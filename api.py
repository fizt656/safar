# api.py

import aiohttp
from datetime import datetime
import base64
import json
import os
from config import OPENROUTER_KEY, STABLE_DIFFUSION_URL, SYSTEM_PROMPT, SYSTEM_PROMPT_IMG, SYSTEM_PROMPT_MODEL, IMG_PROMPT_MODEL

async def generate_response(conversation_history, api_name, api_key):
    # Concatenate the conversation history into a single string
    conversation_context = "\n".join([f"{role}: {message}" for role, message in conversation_history])

    if api_name == 'anthropic':
        api_url = 'https://api.anthropic.com/v1/completion'
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': api_key
        }
        data = {
            'model': 'claude-v1',
            'prompt': f'{conversation_context}\n\nAssistant:',
            'max_tokens_to_sample': 512,
            'stop_sequences': ['\n\nUser:']
        }
    elif api_name == 'openrouter':
        api_url = 'https://openrouter.ai/api/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': SYSTEM_PROMPT_MODEL,
            'messages': [{'role': 'system', 'content': SYSTEM_PROMPT}] + [{'role': role, 'content': message} for role, message in conversation_history],
            'stream': True,
            'max_tokens': 1024
        }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=data, headers=headers) as response:
            if api_name == 'anthropic':
                response_json = await response.json()
                return response_json['completion'].strip()
            elif api_name == 'openrouter':
                response_text = ''
                first_chunk = True
                
                if 'text/event-stream' in response.headers.get('Content-Type', ''):
                    async for chunk in response.content:
                        chunk_data = chunk.decode('utf-8')
                        
                        if 'data: [DONE]' in chunk_data:
                            break
                        if chunk_data.startswith('data:'):
                            chunk_data = chunk_data[6:]
                        if chunk_data.strip():
                            try:
                                chunk_json = json.loads(chunk_data)
                                if 'choices' in chunk_json:
                                    delta = chunk_json['choices'][0]['delta']
                                    if 'content' in delta:
                                        content = delta['content']
                                        response_text += content
                                        print(content, end='', flush=True)
                            except json.JSONDecodeError as e:
                                if not first_chunk:
                                    print()
                                first_chunk = False
                else:
                    response_json = await response.json()
                    if 'choices' in response_json and len(response_json['choices']) > 0:
                        response_text = response_json['choices'][0]['message']['content']
                        print(response_text)
                    else:
                        print("No response received from the API.")
                
                return response_text.strip()

async def generate_image_prompt(last_message):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_IMG},
        {"role": "user", "content": last_message}
    ]

    async with aiohttp.ClientSession() as session:
        async with session.post('https://openrouter.ai/api/v1/chat/completions', json={"model": IMG_PROMPT_MODEL, "temperature": .5, "max_tokens": 128, "messages": messages}, headers={'Authorization': f'Bearer {OPENROUTER_KEY}', 'Content-Type': 'application/json'}) as response:
            response_json = await response.json()

            if 'choices' in response_json and len(response_json['choices']) > 0:
                generated_prompt = response_json['choices'][0]['message']['content']
                return generated_prompt
            else:
                print("No 'choices' found in the OpenRouter API response.")
                return None

async def generate_image(image_prompt):
    try:
        # Ensure the directory for saving images exists
        image_directory = "saved_images"
        if not os.path.exists(image_directory):
            os.makedirs(image_directory)

        # Prepare the API payload with specific parameters for the Stable Diffusion model
        payload = {
            "sd_model_checkpoint": "XL_epicrealismXL_v5Ultimate.safetensors",
            "prompt": image_prompt,
            "steps": 30,    
            "sampler_name": "DPM++ 2M Karras",
            "width": 1152,
            "height": 896,
            "seed": -1,
            "guidance_scale": 7
        }

        # Make the POST request to the Stable Diffusion API
        async with aiohttp.ClientSession() as session:
            async with session.post(STABLE_DIFFUSION_URL, json=payload) as response:
                if response.status == 200:
                    # Read the response content
                    response_content = await response.read()

                    # Check if the response content starts with the PNG magic number
                    if response_content.startswith(b'\x89PNG'):
                        # Save the PNG image data to a file
                        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                        image_filename = f'generated_image_{timestamp}.png'
                        image_path = os.path.join(image_directory, image_filename)
                        print("Image path:", image_path)

                        with open(image_path, 'wb') as f:
                            f.write(response_content)
                        print("Image saved successfully.")
                        return image_path
                    else:
                        # Try to parse the response as JSON
                        try:
                            response_json = json.loads(response_content)
                            if 'images' in response_json and len(response_json['images']) > 0:
                                image_data = response_json['images'][0]
                                if image_data.startswith('data:image/png;base64,'):
                                    image_data = image_data.split(',', 1)[1]
                                image_data = base64.b64decode(image_data)

                                # Save the image data to a file
                                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                                image_filename = f'generated_image_{timestamp}.png'
                                image_path = os.path.join(image_directory, image_filename)
                                print("Image path:", image_path)

                                with open(image_path, 'wb') as f:
                                    f.write(image_data)
                                print("Image saved successfully.")
                                return image_path
                                print(image_prompt)
                            else:
                                print("No image data found in the response.")
                        except json.JSONDecodeError:
                            print("Error parsing JSON response.")
                else:
                    print("Request failed with status code:", response.status)

                return None
    except Exception as e:
        print(f"An error occurred in generate_image: {str(e)}")
        return None