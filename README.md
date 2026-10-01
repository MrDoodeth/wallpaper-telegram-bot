# WallPapperBot

A Telegram bot that sends a random wallpaper from a selected category after checking
channel membership.

## 📦 Features

- Browse wallpapers through a Russian-language reply keyboard with eight category buttons.
- Receive a randomly selected local file as a Telegram document, preserving the original file.
- Require membership in four configured Telegram channels before serving wallpapers.
- Restrict access using a configurable list of Telegram user IDs.
- Open an admin menu with a user ID export and a plain-text broadcast action.

## 🚀 Getting Started

**Requirements**

- Python and `pip`. <!-- TODO: specify the supported Python versions -->
- A Telegram bot token obtained from [BotFather](https://t.me/BotFather).
- Access to the four channels used for membership checks and their IDs and join URLs.
- Local wallpaper files; `Resources/` is excluded from the repository by `.gitignore`.

**Installation**

Clone the repository and install the package imported by `bot.py`:

```bash
git clone https://github.com/MrDoodeth/WallPapperBot.git
cd WallPapperBot
python -m venv .venv
source .venv/bin/activate
python -m pip install pyTelegramBotAPI
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.
There is no dependency manifest or pinned dependency version in this repository.

**Quick Start**

1. Create a bot token and set `TELEGRAM_BOT_TOKEN` in your environment.
2. Set `TELEGRAM_ADMIN_ID` if you need access to `/admin`; update channel details in `config.py`.
3. Add at least one wallpaper to each category you want to use under `Resources/`.
4. Start the bot from the repository root:

```bash
export TELEGRAM_BOT_TOKEN='<your-new-bot-token>'
export TELEGRAM_ADMIN_ID='<your-chat-id>'
python bot.py
```

Open [@WallpapersAllWallpapers_bot](https://t.me/WallpapersAllWallpapers_bot), if using the
original bot deployment, or open the bot associated with your own token. Send `/start` and
select a category. The bot runs using Telegram polling; stop it with `Ctrl+C`.

## ⚙️ Configuration

Set the environment variables above and edit `config.py` before starting the bot:

- `TELEGRAM_BOT_TOKEN`: required token for the Telegram bot; read by `config.py`.
- `TELEGRAM_ADMIN_ID`: optional comma-separated administrator chat IDs; `/admin` checks this list.
- `BLACK_LIST`: list of blocked chat IDs as strings.
- `CHATS_INFO[0]`: four channel IDs used for membership checks.
- `CHATS_INFO[1]`: four corresponding channel URLs shown to users in the same order.
- Message constants such as `START_TEXT` and `CONDITION_TEXT`: user-facing Russian text.

The code checks exactly four channels. Ensure the bot can query membership for those channels;
otherwise access checks may fail. The category folders are relative to the working directory:

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

These folders and their files are not included in the repository. An empty or missing
category cannot return a wallpaper. The “random wallpaper” button uses `Resources/Другое`;
it does not sample across all categories.

**Security and data**

- Earlier revisions committed a bot token. Revoke it: removing it from the current files
  does not remove it from Git history. Never commit a replacement token.
- `users_id.txt` is ignored by Git and created automatically when needed. The bot appends
  user IDs after a successful membership check and reads the file for admin broadcasts.
  An earlier revision tracked user IDs; consider their privacy before sharing Git history.

## 🛠️ Usage

Send these commands to the bot in Telegram:

```text
/start
/admin
```

`/start` displays category buttons. Tap one to receive a file after the membership check.
`/admin` displays the admin menu only for IDs listed in `ADMIN_ID`. Its broadcast action
sends the submitted text to IDs in `users_id.txt`; it does not send media or formatted posts.

The interface and responses are currently in Russian. To change the text, update the button
labels in `bot.py` and the message constants in `config.py` together.

## 🤝 Contributing

1. Fork the repository and create a branch for your change.
2. Keep changes focused; do not commit tokens, user IDs, or wallpaper files without permission.
3. Open a pull request describing the change and how you checked it.

There is no automated test suite or contribution guide in the repository yet.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
