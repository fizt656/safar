import asyncio
from api import generate_response, generate_image_prompt, generate_image
from config import (
    IMAGE_DIRECTORY, TerminalColors, BANNER, GOODBYE_BANNER,
    OPENROUTER_KEY, REPLICATE_API_TOKEN, get_image_gen_method
)

class Safar:
    def __init__(self):
        self.conversation_history = []
        self.image_gen_method = None

    def start(self):
        self.image_gen_method = get_image_gen_method()
        
        startup_message = f"""Initializing Safar...
Loading Desert Modules...
Verifying Oasis Integrity...

{BANNER}

The sands of time begin to shift...
Ancient whispers carried on the desert wind...

|*!!MYSTICAL ENERGIES AWAKENED!!*|
Sand dunes mapped: 1001
Mirage stability: 87.6%
Oasis water index: 32.4

Loading complete.
Safar: Desert Odyssey [v. 1.0]
Last caravan departure: 7 moons ago

$Safar> Welcome, traveler, to the mystical deserts of Safar! What secrets do you seek in these ancient sands?"""
        
        return startup_message

    async def process_input(self, user_input):
        if user_input.lower() in ['vis', 'visualize']:
            return await self.visualize_full()
        elif user_input.lower() == 'visfast':
            return await self.visualize_quick()
        else:
            self.conversation_history.append(("user", user_input))
            response_stream = await generate_response(self.conversation_history, 'openrouter', OPENROUTER_KEY)
            return response_stream

    async def visualize_full(self):
        if len(self.conversation_history) > 0:
            last_message = self.conversation_history[-1][1]
            context = f"""Based on the following text adventure context:\n{last_message}\n\nGenerate a detailed image prompt for an AI image generation model to create an image that captures the player's surroundings, objects, characters, and any other relevant visual elements mentioned in the context. The prompt should provide a comprehensive description of what the player is seeing from their point of view (POV) in the text adventure."""

            image_prompt = await generate_image_prompt(context)
            if image_prompt:
                image_path = await generate_image(image_prompt, self.image_gen_method)
                if image_path:
                    return f"Image generated: {image_path}\n\nImage prompt: {image_prompt}"
                else:
                    return "Error generating image"
            else:
                return "Error generating image prompt"
        else:
            return "No previous context available for visualization"

    async def visualize_quick(self):
        if len(self.conversation_history) > 0:
            last_message = self.conversation_history[-1][1]
            context = f"""Based on the following text adventure context:\n{last_message}\n\nGenerate a brief image prompt for an AI image generation model to create a quick sketch or simple representation of the scene."""

            image_prompt = await generate_image_prompt(context)
            if image_prompt:
                image_path = await generate_image(image_prompt, self.image_gen_method)
                if image_path:
                    return f"Quick visualization generated: {image_path}\n\nImage prompt: {image_prompt}"
                else:
                    return "Error generating quick visualization"
            else:
                return "Error generating image prompt for quick visualization"
        else:
            return "No previous context available for quick visualization"

    def shutdown(self):
        return f"""Last caravan departure: 7 moons ago
The desert sands begin to settle...

{GOODBYE_BANNER}"""