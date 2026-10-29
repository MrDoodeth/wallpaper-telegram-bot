# Wallpaper Telegram Bot

A Telegram bot that sends a random wallpaper from a chosen category, but only to users
subscribed to four required channels.

This is an educational project and is not perfect :)

## 📦 Features

- Reply keyboard with eight categories.
- Wallpapers are sent as documents, so the original quality is kept.
- Mandatory subscription to four channels, checked on every request.
- `BLACK_LIST` of blocked chat IDs.
- `/admin` menu: export user IDs and send a plain-text broadcast.

## 📋 Requirements

- Python 3 and `pip`.
- A bot token from [BotFather](https://t.me/BotFather).
- The IDs and URLs of the four channels (the bot must be able to read their members).
- Your own wallpaper files in `Resources/` (ignored by Git).

## 🚀 Build and run

```bash
git clone https://github.com/MrDoodeth/wallpaper-telegram-bot.git
cd wallpaper-telegram-bot
python -m venv .venv
source .venv/bin/activate
python -m pip install pyTelegramBotAPI
```

Set the environment variables and start the bot from the repository root:

```bash
export TELEGRAM_BOT_TOKEN='<bot-token>'
export TELEGRAM_ADMIN_ID='<chat-id>[,<chat-id>...]'   # optional, for /admin
python bot.py
```

The bot uses polling; stop it with `Ctrl+C`.

## ⚙️ Configuration

Edit [`config.py`](config.py):

- `CHATS_INFO[0]` and `CHATS_INFO[1]`: IDs and URLs of the four channels, in the same order.
  The code expects exactly four.
- `BLACK_LIST`: blocked chat IDs as strings.
- Message constants (`START_TEXT`, `CONDITION_TEXT`, ...): bot texts.

Category folders are read from the working directory and are not in the repository:

```text
Resources/
├── Другое/
├── Тачки/
├── Абстракция/
├── Архитектура/
├── Космос/
├── Мемные/
├── Персонажи/
└── Природа/
```

An empty or missing folder makes the bot reply with an error message.

User IDs are saved to `users_id.txt` after a successful subscription check.

## 🛠️ Usage

- `/start`: show the category buttons.
- `/admin`: admin menu, only for IDs in `TELEGRAM_ADMIN_ID`.

Broadcasts are plain text only (no media or formatting).

## 📜 License

MIT, see [LICENSE](LICENSE).
