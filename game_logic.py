import asyncio
from api import OpenRouterAPI

class SafarGame:
    def __init__(self):
        self.player_name = ""
        self.current_location = "start"
        self.inventory = []
        self.api = OpenRouterAPI()
        self.conversation_history = []

    async def process_command(self, command):
        self.conversation_history.append(f"Player: {command}")
        
        prompt = f"""You are an interactive text adventure game called Safar. The player's name is {self.player_name}.
Current location: {self.current_location}
Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}

Conversation history:
{' '.join(self.conversation_history[-5:])}

Respond to the player's command in a creative and engaging way, describing the results of their actions and any new observations. Keep responses concise, around 2-3 sentences. If the player's action changes their location or inventory, include that information in your response.

Player command: {command}
Game response:"""

        response_stream = await self.api.generate_stream(prompt)
        return response_stream

    def update_game_state(self, response):
        # Update game state based on the LLM's response
        # This is a simple example and might need to be more sophisticated
        if "you move to" in response.lower():
            self.current_location = response.lower().split("you move to")[-1].strip().split(".")[0]
        if "you pick up" in response.lower():
            item = response.lower().split("you pick up")[-1].strip().split(".")[0]
            if item not in self.inventory:
                self.inventory.append(item)

    def get_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        return "Inventory: " + ", ".join(self.inventory)

    def set_player_name(self, name):
        self.player_name = name
        return f"Welcome, {self.player_name}! Your adventure begins now."