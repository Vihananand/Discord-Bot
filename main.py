# Application ID: 1404790674208854157
# Public Key: 477e75c78e75014765fd037f44c09f6065915f60419ed071491e83f848c9198a

import discord
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client_ai = genai.Client(api_key=GEMINI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

MAX_DISCORD_MSG_LENGTH = 2000

# Store conversation history per channel
chat_history = {}
MAX_CHAT_HISTORY = 50  # Limit conversation history to prevent token overflow

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        # This if prevents the bot from replying to its own messages
        if message.author == self.user:
            return

        # This if prevents the bot from replying you until you mention it in your chat
        if self.user not in message.mentions:
            return
        
        channel_id = message.channel.id
        
        # Initialize chat history for this channel if it doesn't exist
        if channel_id not in chat_history:
            chat_history[channel_id] = []
        
        # Add user message to history
        chat_history[channel_id].append(f"User {message.author.display_name}: {message.content}")
        
        # Keep only recent messages to prevent token overflow
        if len(chat_history[channel_id]) > MAX_CHAT_HISTORY:
            chat_history[channel_id] = chat_history[channel_id][-MAX_CHAT_HISTORY:]
        
        # Create conversation context with bot personality
        conversation_history = "\n".join(chat_history[channel_id])
        bot_prompt = f"""You are a helpful Discord bot assistant. You should:
        - Be friendly and conversational
        - Remember the context of our conversation in this channel
        - Give concise, helpful responses
        - Use emojis occasionally to be more engaging
        - Act like a bot companion, not just an AI model

        Previous conversation:
        {conversation_history}

        Please respond as the Discord bot:"""

        # This function creates a "Chatbot is typing..." and waits until you message is received by the Generative AI
        async with message.channel.typing():
            response = client_ai.models.generate_content(
                model="gemini-2.5-flash",
                contents=bot_prompt
            )
        
        # Add bot response to history
        bot_response = response.text.strip()
        chat_history[channel_id].append(f"Bot: {bot_response}")
        
        # Send the response directly
        await message.channel.send(bot_response)

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
