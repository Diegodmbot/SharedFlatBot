from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

cleaning_schedule = [
    ["Baño", "Cocina", "Salón", "Pasillo + Solana"],
    ["Cocina", "Baño", "Pasillo + Solana", "Salón"],
    ["Salón", "Pasillo + Solana", "Baño", "Cocina"],
    ["Pasillo + Solana", "Salón", "Baño", "Cocina"],
    ["Cocina", "Baño", "Pasillo + Solana", "Salón"],
    ["Baño", "Salón", "Cocina", "Pasillo + Solana"]
]


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('PRUEBA')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')


async def weekly_cleaning(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    current_week = datetime.date.today().isocalendar()[1]
    assignments = cleaning_schedule[current_week % len(cleaning_schedule)]
    response = "Asignaciones de limpieza para esta semana:\n"
    for i, area in enumerate(assignments):
        match i:
            case 0:
                name = "Diego"
            case 1:
                name = "Pablo"
            case 2:
                name = "Eli"
            case 3:
                name = "Juds"
        response += f"- {name}: {area}\n"
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=response)


async def add_expense(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) >= 3:
        valor1, valor2, valor3 = args[0], args[1], args[2]
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Valores: {valor1}, {valor2}, {valor3}")


def main():
    app = ApplicationBuilder().token(
        "8310991019:AAHSGCFtUAtjsQwFHl06mO9TUKLt-BkVa_A").build()
    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("limpiar", weekly_cleaning))
    app.add_handler(CommandHandler("gasto", add_expense, has_args=3))

    app.run_polling()


if __name__ == "__main__":
    main()
