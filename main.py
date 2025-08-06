# --- AGORATUBE TELEGRAM BOT (FINAL DEBUGGING VERSION) ---
import os
import requests
from flask import Flask, request

# --- CONFIGURATION ---
# The token is hardcoded here for our test.
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

# --- WEB SERVER SETUP (No need to edit) ---
app = Flask(__name__)

# This is the endpoint that Telegram sends messages to.
@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def respond():
    print("--> Webhook received a request!")
    try:
        # Get the JSON data from Telegram
        update = request.get_json()
        print(f"--> Full update JSON: {update}")

        # Extract chat_id and the message text
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        print(f"--> Received message: '{text}' from chat_id: {chat_id}")

        # If the message is /start, send the welcome message
        if text == "/start":
            print("--> '/start' command detected. Preparing to send reply.")
            
            # Use the 'requests' library to call the Telegram API directly
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': WELCOME_MESSAGE,
                'parse_mode': 'Markdown'
            }
            
            # Send the message
            response = requests.post(url, json=payload)
            print(f"--> Telegram API response: {response.json()}")

    except Exception as e:
        # If any error happens, print it to the logs
        print(f"--> An error occurred: {e}")

    # Tell Telegram we received the message
    return 'ok'

# A simple route to check if the server is running
@app.route('/')
def index():
    return 'Server is running!'
