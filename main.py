# --- AGORATUBE TELEGRAM BOT ---
import os
import telegram
from telegram.ext import Updater, CommandHandler

# --- CONFIGURATION ---
# We will get the token from Railway's secret variables
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

# This is the message the bot will send.
WELCOME_MESSAGE = """
Hello! Welcome to the AgoraTube AI Website Course.

To get instant access, please follow these simple payment steps:

**Course Price:** 2,000 ETB

**Payment Options:**

**1. CBE (Commercial Bank of Ethiopia):**
   - **Account Name:** [Your Full Name Here]
   - **Account Number:** [Your CBE Account Number Here]

**2. Telebirr:**
   - **Account Number:** [Your Telebirr Number Here]

After you have made the payment, please send a screenshot of the transaction to this chat.

Once I confirm the payment, I will send you the private invitation link to the course group.

Thank you!
"""

# --- BOT LOGIC ---
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

    # Use the PORT environment variable Railway provides.
    PORT = int(os.environ.get('PORT', '8443'))

    # Start the Bot in webhook mode for hosting
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TELEGRAM_TOKEN,
                          webhook_url=f"https://YOUR_RAILWAY_APP_URL.up.railway.app/{TELEGRAM_TOKEN}")

    print("Bot has started in webhook mode.")
    updater.idle()

if __name__ == '__main__':
    main()
