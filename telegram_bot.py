from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import requests

API_KEY = "9190a75114cb17ceeda7a455a62735b3"
BOT_TOKEN = "7439581797:AAG67kDTjuy9ibmuTFcMWRR3jNlNP4PXLsE"

NUMBER = range(1)

def get_number_info(number: str):
    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"
    response = requests.get(url)
    data = response.json()

    if 'valid' in data and data['valid']:
        return (
            f"Valid\n"
            f"Local Format: {data.get('local_format', 'N/A')}\n"
            f"Intl. Format: {data.get('international_format', 'N/A')}\n"
            f"Country: {data.get('country_name', 'N/A')}\n"
            f"Location: {data.get('location', 'N/A')}\n"
            f"Carrier: {data.get('carrier', 'N/A')}\n"
            f"Line Type: {data.get('line_type', 'N/A')}"
        )
    else:
        return f"Invalid phone number: {number}"

async def start_numinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please provide a phone number.")
    return NUMBER

async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text
    info = get_number_info(number)
    await update.message.reply_text(info)
    return ConversationHandler.END

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("numinfo", start_numinfo)],
        states={
            NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number)],
        },
        fallbacks=[],
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
