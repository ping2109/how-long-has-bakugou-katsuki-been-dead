import time
import datetime
import asyncio
import telegram.ext

# Your Telegram bot token and chat ID
bot_token = 'TOKEN'
chat_id = 'TG_ID'

# Create an instance of the Telegram bot
bot = telegram.Bot(token=bot_token)

# Set a specified time to send the message
# In this case midnight
send_time = datetime.time(hour=0, minute=0, second=0)

# Function to send the message
async def send_daily_message(message):
    await bot.send_message(chat_id=chat_id, text=message)

# Loop indefinitely
while True:

    # Calculate Bakugou's death date
    now = datetime.datetime.now().time()    ## Get the current time
    d0 = datetime.datetime(2022, 8, 1)
    d1 = datetime.datetime.now()
    delta = d1 - d0
    days = delta.days
    
    # Message
    message = (f"""Bakugou Katsuki has been dead for {days} days.""")

    # Check if it's time to send the message
    if now.hour == send_time.hour:
        # Create an event loop
        loop = asyncio.get_event_loop()
        # Run the function to send the message
        loop.run_until_complete(send_daily_message(message))

    # Sleep before checking the time again
    time.sleep(60)
