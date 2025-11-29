import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from dotenv import load_dotenv

cleaning_schedule = [
    ["Baño", "Cocina", "Salón", "Pasillo + Solana"],
    ["Cocina", "Baño", "Pasillo + Solana", "Salón"],
    ["Salón", "Pasillo + Solana", "Baño", "Cocina"],
    ["Pasillo + Solana", "Salón", "Baño", "Cocina"],
    ["Cocina", "Baño", "Pasillo + Solana", "Salón"],
    ["Baño", "Salón", "Cocina", "Pasillo + Solana"]
]

users = ["Diego", "Pablo", "Dario", "Juds"]


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('PRUEBA')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')


async def weekly_cleaning(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    current_week = datetime.date.today().isocalendar()[1]
    assignments = cleaning_schedule[current_week % len(cleaning_schedule)]
    if len(assignments) != len(users):
        return
    response = "Asignaciones de limpieza para esta semana:\n"
    for user, area in zip(users, assignments):
        response += f"- {user}: {area}\n"
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=response)


async def add_expense_test(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) >= 3:
        valor1, valor2, valor3 = args[0], args[1], args[2]
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Valores: {valor1}, {valor2}, {valor3}")


def main():
    load_dotenv()
    API_TOKEN = os.getenv("TELEGRAM_BOT_KEY")
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("limpiar", weekly_cleaning))
    app.add_handler(CommandHandler("gasto", add_expense_test, has_args=3))
    print("Bot is running...")
    PORT = int(os.environ.get("PORT", 8000))
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url="https://sharedflatbot.onrender.com"
    )
    print(f"Webhook is running on port {PORT}...")

    app.run_polling()


if __name__ == "__main__":
    main()
