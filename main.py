# --- AGORATUBE TELEGRAM BOT (FINAL STABLE VERSION) ---
import os
import telegram
from flask import Flask, request

# --- CONFIGURATION ---
# The token is read from Railway's secret variables.
# We are hardcoding it here because the variable system was not working.
TELEGRAM_TOKEN = "8327178761:AAEwcqgJkZ7o3SIYQg9Raw3WXC6kQpYbdhU"

WELCOME_MESSAGE = """
Hello! Welcome to the AgoraTube AI Website Course.

To get instant access, please follow these simple payment steps:

**Course Price:** 2,000 ETB

**Payment Options:**

**1. CBE (Commercial Bank of Ethiopia):**
   - **Account Name:** Bisrat Tadesse
   - **Account Number:** 1000539889102

**2. Telebirr:**
   - **Account Number:** +251930551468

After you have made the payment, please send a screenshot of the transaction to this chat.

Once I confirm the payment, I will send you the private invitation link to the course group.

Thank you!
"""

# --- BOT & WEB SERVER SETUP (No need to edit) ---
bot = telegram.Bot(token=TELEGRAM_TOKEN)
app = Flask(__name__)

# This is the endpoint that Telegram sends messages to.
# The webhook for this was set manually.
@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def respond():
    # Retrieve the message in JSON and transform it to a Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # Get the chat ID and message text
    chat_id = update.message.chat.id
    text = update.message.text

    # Handle the /start command
    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text=WELCOME_MESSAGE, parse_mode='Markdown')
    
    return 'ok'

# A simple route to check if the server is running
@app.route('/')
def index():
    return 'Server is running!'

# The app is run by Gunicorn from the Procfile, so the __main__ block is not needed for Railway.
