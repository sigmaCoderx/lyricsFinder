# 🎵 Lyrics Finder Telegram Bot

A simple Telegram bot that searches for song lyrics using the Genius API.

Send the bot a song name, and it searches Genius for the song and returns the available lyrics directly in Telegram.

---

## Features

- 🎵 Search for song lyrics
- 🔎 Search songs by name
- 🤖 Telegram bot interface
- 🌐 Uses the Genius API
- ⚡ Simple and fast
- 📋 Returns lyrics directly in chat

---

## Tech Stack

- Python
- pyTelegramBotAPI
- LyricsGenius
- Genius API

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sigmaCoderx/lyricsFinder.git
cd lyricsFinder
```

### Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

The bot requires two credentials:

### Genius API Key

Create a Genius API client and get your API key from:

https://genius.com/api-clients

Replace:

```python
genuisKey = "GENIUS_API"
```

with your Genius API key.

### Telegram Bot Token

Create a Telegram bot using **BotFather**:

https://t.me/BotFather

Replace:

```python
bot = TeleBot("BOT_TOKEN", parse_mode="HTML")
```

with your Telegram Bot Token.

---

## Running the Bot

```bash
python getLyrics.py
```

The bot will start polling for messages.

---

## How It Works

1. Start the bot using `/start`.
2. Send a song name.
3. The bot searches Genius for the song.
4. The matching song is retrieved.
5. The available lyrics are sent back to Telegram.

---

## Example

### Input

```text
Believer Imagine Dragons
```

### Output

```text
[Song lyrics returned by Genius]
```

---

## Project Structure

```text
lyricsFinder/
├── getLyrics.py
├── requirements.txt
└── README.md
```

---

## Requirements

All Python dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## Notes

- Requires a valid Telegram Bot Token.
- Requires a valid Genius API key.
- Requires an active internet connection.
- Lyrics availability depends on Genius.
- Very long lyrics may exceed Telegram's message size limit.
- Never commit your Telegram Bot Token or Genius API key to GitHub.

---

## License

MIT License

---

## Author

**flippedCoin**

GitHub: https://github.com/sigmaCoderx
