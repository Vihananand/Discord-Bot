# Discord AI Bot 🤖

A Discord bot powered by Google's Gemini AI that provides intelligent, conversational responses while maintaining chat history per channel.

## Features ✨

- **AI-Powered Responses**: Uses Google Gemini 2.5 Flash for intelligent conversations
- **Per-Channel Memory**: Remembers conversation history separately for each Discord channel
- **Mention-Only Activation**: Bot only responds when mentioned, preventing spam
- **Smart History Management**: Automatically manages conversation history to prevent token overflow
- **Typing Indicator**: Shows "Bot is typing..." while generating responses
- **Bot Personality**: Configured to act as a friendly Discord bot companion rather than a generic AI

## Prerequisites 📋

- Python 3.7 or higher
- Discord Developer Account
- Google AI API Key (Gemini)

## Required Packages 📦

- `discord.py` - Discord API wrapper
- `google-genai` - Google Generative AI client
- `python-dotenv` - Environment variable management

## Setup Instructions 🚀

### 1. Clone or Download

Download the project files to your local machine.

### 2. Install Dependencies

```bash
pip install discord.py google-genai python-dotenv
```

### 3. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and create a bot
4. Copy the bot token
5. Enable "Message Content Intent" in the bot settings

### 4. Get Google AI API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create an API key for Gemini
3. Copy the API key

### 5. Environment Setup

Create a `.env` file in the project directory:

```env
DISCORD_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 6. Invite Bot to Server

1. Go to OAuth2 > URL Generator in Discord Developer Portal
2. Select "bot" scope
3. Select "Send Messages" and "Read Message History" permissions
4. Use the generated URL to invite your bot

## Usage 💬

1. Run the bot:

   ```bash
   python main.py
   ```

2. In Discord, mention your bot in any message:

   ```Text
   @YourBot Hello! How are you?
   ```

3. The bot will respond with context-aware messages and remember the conversation!

## Configuration ⚙️

### Adjustable Settings in `main.py`

- `MAX_CHAT_HISTORY = 50` - Maximum messages to remember per channel
- `MAX_DISCORD_MSG_LENGTH = 2000` - Discord message character limit
- `model="gemini-2.5-flash"` - Gemini model version

### Bot Personality Customization

You can modify the bot's personality in the `bot_prompt` section:

```python
bot_prompt = f"""You are a helpful Discord bot assistant. You should:
- Be friendly and conversational
- Remember the context of our conversation in this channel
- Give concise, helpful responses
- Use emojis occasionally to be more engaging
- Act like a bot companion, not just an AI model
```

## File Structure 📁

```Code
DiscordBot/
├── main.py          # Main bot application
├── .env             # Environment variables (create this)
├── README.md        # This file
├── pyvenv.cfg       # Virtual environment config
├── Include/         # Virtual environment includes
├── Lib/             # Virtual environment libraries
└── Scripts/         # Virtual environment scripts
```

## How It Works 🔧

1. **Message Detection**: Bot listens for messages where it's mentioned
2. **History Management**: Stores conversation history per Discord channel
3. **AI Processing**: Sends conversation context to Gemini AI
4. **Response Generation**: Receives and processes AI response
5. **Message Sending**: Sends clean response back to Discord channel

## Security Notes 🔐

- Keep your `.env` file private and never commit it to version control
- Your Discord token and API keys should remain secret
- The bot only responds to mentions, preventing unauthorized usage

## Troubleshooting 🔧

### Bot doesn't respond

- Check if bot has proper permissions in the server
- Ensure you're mentioning the bot correctly
- Verify `.env` file has correct tokens

### API Errors

- Check if your Google AI API key is valid
- Ensure you have sufficient API quota
- Verify your Discord bot token is correct

## License 📄

This project is open source and available under the MIT License.

## Support 💡

If you encounter any issues or have questions, feel free to reach out or create an issue in the repository.

---
Made with ❤️ and Python
