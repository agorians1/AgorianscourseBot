# --- AGORATUBE TELEGRAM BOT (RENDER STABLE VERSION) ---
import os
import requests
from flask import Flask, request

# --- CONFIGURATION ---
# The token is read securely from Render's Environment Variables
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

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

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def respond():
    try:
        update = request.get_json()
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            text = update['message']['text']
            if text == "/start":
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
                payload = {'chat_id': chat_id, 'text': WELCOME_MESSAGE, 'parse_mode': 'Markdown'}
                requests.post(url, json=payload)
    except Exception as e:
        print(f"An error occurred: {e}")
    return 'ok'

@app.route('/')
def index():
    return 'Server is running!'
