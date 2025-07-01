from email.mime import application
from telegram import Update
from telegram import Bot
import schedule
import time
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import nest_asyncio
nest_asyncio.apply()
import logging
logging.basicConfig(level=logging.INFO)
  

# Define a command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')

# Main function to run the bot
async def main():
    application = ApplicationBuilder().token("7228071022:AAFOlHNSC_SK67P9UsdAVg4ZWTsdbYO8jHo").build()

    # Register the command handler
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    try:
        await application.run_polling()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
    
TELEGRAM_TOKEN = '7228071022:AAFOlHNSC_SK67P9UsdAVg4ZWTsdbYO8jHo'
CHAT_ID = ' 6902452758'
bot = Bot(token=TELEGRAM_TOKEN)
def post_to_telegram(message):
      bot.send_message(chat_id=CHAT_ID, text=message)
      print("Message sent to Telegram!")
      
def job():
    logging.info("Job is running...")
    post_to_telegram("Automated message to Telegram!")
schedule.every().hour.do(job)
#schedule.every(1).minutes.do(job)
while True:
      schedule.run_pending()
      time.sleep(1)