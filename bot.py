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


async def add_shopping_item(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    item = ' '.join(args)
    with open("shopping_list.txt", "a") as file:
        file.write(f"{item}\n")
    pass


async def remove_shopping_item(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def show_shopping_list(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('shopping_list.txt', 'r') as file:
        content = file.read().replace("\n", ", ")
    await update.message.reply_text(content)


async def reset_shopping_list(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def add_expense(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) >= 3:
        valor1, valor2, valor3 = args[0], args[1], args[2]
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Valores: {valor1}, {valor2}, {valor3}")


async def show_debts(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    pass


def main():
    load_dotenv()
    API_TOKEN = os.getenv("TELEGRAM_BOT_KEY")
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("limpiar", weekly_cleaning))
    app.add_handler(
        CommandHandler(
            "añadir_articulo",
            add_shopping_item,
            has_args=True))
    app.add_handler(
        CommandHandler(
            "quitar_articulo",
            remove_shopping_item,
            has_args=True))
    app.add_handler(CommandHandler("lista", show_shopping_list))
    app.add_handler(CommandHandler("borrar_lista", reset_shopping_list))
    app.add_handler(CommandHandler("gasto", add_expense, has_args=3))
    app.add_handler(CommandHandler("deudas", show_debts))
    PORT = int(os.environ.get("PORT", 8000))
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url="https://sharedflatbot.onrender.com"
    )


if __name__ == "__main__":
    main()
