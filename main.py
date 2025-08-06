# --- AGORATUBE TELEGRAM BOT (STABLE FLASK VERSION) ---
import os
import telegram
from flask import Flask, request

# --- CONFIGURATION ---
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

# --- BOT & WEB SERVER SETUP (No need to edit) ---
bot = telegram.Bot(token=TELEGRAM_TOKEN)
app = Flask(__name__)

# This is the endpoint that Telegram sends messages to
@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def respond():
    # Retrieve the message in JSON and transform it to a Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # Get the chat ID and message text
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()

    # Handle the /start command
    if text == "/start":
        bot.sendMessage(chat_id=chat_id, text=WELCOME_MESSAGE, parse_mode='Markdown')
    
    return 'ok'

# A simple route to check if the server is running
@app.route('/')
def index():
    return 'Server is running!'

if __name__ == '__main__':
    # The app is run by Gunicorn from the Procfile, so this part is not used on Railway
    # but is useful for local testing if needed.
    app.run(threaded=True)
