# --- AGORATUBE TELEGRAM BOT (CORRECTED FINAL VERSION) ---
import os
import telegram
from telegram.ext import Updater, CommandHandler

# --- CONFIGURATION ---
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

# This is the message the bot will send with your payment details.
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

# --- BOT LOGIC (No need to edit below this line) ---
def start(update, context):
    """Sends the welcome message when the /start command is issued."""
    update.message.reply_text(WELCOME_MESSAGE, parse_mode='Markdown')

def main():
    """Start the bot."""
    if not TELEGRAM_TOKEN:
        print("ERROR: TELEGRAM_TOKEN environment variable not set!")
        return

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Get the port from the environment variable Railway provides
    PORT = int(os.environ.get('PORT', '8443'))
    
    # This single command correctly starts the bot and sets the webhook with Telegram.
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TELEGRAM_TOKEN,
                          webhook_url=f"https://web-production-056b2.up.railway.app/{TELEGRAM_TOKEN}")
    
    print("Bot has started correctly in webhook mode.")
    updater.idle()

if __name__ == '__main__':
    main()
