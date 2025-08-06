# --- AGORATUBE TELEGRAM BOT (DIAGNOSTIC TEST VERSION) ---
import os
import telegram
from flask import Flask, request

# --- CONFIGURATION ---
# We are temporarily putting the token directly here to test the connection.
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

# This is the endpoint that Telegram sends messages to
@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.encode('utf-8').decode()

    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text=WELCOME_MESSAGE, parse_mode='Markdown')
    
    return 'ok'

# A simple route to check if the server is running
@app.route('/')
def index():
    return 'Server is running!'

# This sets the webhook when the server starts
def set_webhook():
    webhook_url = f"https://web-production-056b2.up.railway.app/{TELEGRAM_TOKEN}"
    response = bot.set_webhook(webhook_url)
    print(f"Webhook set to {webhook_url}: {response}")

if __name__ == '__main__':
    set_webhook()
    # The app is run by Gunicorn from the Procfile
    # This part is not directly run on Railway but the function call above is.
    # We need to ensure the app object is available for Gunicorn.
    pass
