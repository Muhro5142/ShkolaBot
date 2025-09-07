import telebot
import pandas as pd
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# Replace with your bot's token
TELEGRAM_BOT_TOKEN = "7261741533:AAEHEitc-Xf8kqWXGiLHRjggT6M0g_4voLI"

# Path to the CSV file
CSV_FILE_PATH = "formatted_calendar.csv"

# Create a bot instance
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Function to check if today is 14 days before the event
def check_reminders():
    data = pd.read_csv(CSV_FILE_PATH)
    today = datetime.today().date()

    for index, row in data.iterrows():
        # Assuming the event date is in the 'Month' and 'Day' columns (adjust as needed)
        try:
            event_date = datetime.strptime(f"{row['Month']} {row['Day']} {today.year}", "%b %d %Y").date()
            reminder_date = event_date - timedelta(days=14)
            
            # If today is 14 days before the event, send a reminder
            if today == reminder_date:
                message = f"Reminder: The event {row['Hebrew Day']} is happening in 14 days!"
                # Send the message to a predefined chat or user
                bot.send_message(chat_id="1076261091", text=message)
        except Exception as e:
            print(f"Error processing row {row}: {e}")

# Command to start the bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! I'll remind you about events 14 days before they happen!")

# Command to send the CSV file
@bot.message_handler(commands=['get_calendar'])
def send_calendar(message):
    try:
        with open(CSV_FILE_PATH, 'rb') as file:
            bot.send_document(chat_id=message.chat.id, document=file, caption="Here is the reformatted calendar.")
    except FileNotFoundError:
        bot.reply_to(message, "The file could not be found. Please make sure it exists.")

# Set up a scheduler to run every day at midnight using CronTrigger
scheduler = BackgroundScheduler()
scheduler.add_job(check_reminders, CronTrigger(hour=0, minute=0))

# Start the scheduler
scheduler.start()

# Start the bot polling
bot.polling()
