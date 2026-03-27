# 🏠 SharedFlatBot

A Telegram bot designed to help flatmates manage shared living tasks — cleaning schedules, shopping lists, and shared expenses.

## Features

- **🧹 Weekly Cleaning Schedule** — Automatically rotates cleaning area assignments among flatmates each week based on the ISO calendar week number.
- **🛒 Shopping List** — Add, remove, view, and reset a shared shopping list stored in a text file.
- **💸 Expense Tracking** *(in progress)* — Log shared expenses with `/add_expense` and view debts with `/show_debts`.

## Commands

| Command | Description |
|---|---|
| `/test` | Check that the bot is running |
| `/clean` | Show this week's cleaning assignments |
| `/add_item <item>` | Add an item to the shopping list |
| `/remove_item <item>` | Remove an item from the shopping list |
| `/shopping_list` | View the current shopping list |
| `/reset_list` | Clear the entire shopping list |
| `/add_expense <payer> <amount> <description>` | Log a shared expense |
| `/show_debts` | Show current debt balances *(coming soon)* |

## Tech Stack

- **Python 3**
- **[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)** v22.5
- **python-dotenv** — for managing environment variables
- Deployed on **[Render](https://render.com)** via webhook

## Getting Started

### Prerequisites

- Python 3.8+
- A Telegram Bot token (get one from [@BotFather](https://t.me/BotFather))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Diegodmbot/SharedFlatBot.git
   cd SharedFlatBot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```env
   TELEGRAM_BOT_KEY=your_telegram_bot_token_here
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

### Deployment (Render)

The bot is configured to run as a webhook on Render. Make sure to set the `TELEGRAM_BOT_KEY` environment variable in your Render service settings and update the `webhook_url` in `bot.py` to match your Render app URL.

## Project Structure

```
SharedFlatBot/
├── bot.py              # Main bot logic and command handlers
├── api_keys.py         # API key configuration
├── requirements.txt    # Python dependencies
├── shopping_list.txt   # Persistent shopping list (auto-created)
└── .gitignore
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
