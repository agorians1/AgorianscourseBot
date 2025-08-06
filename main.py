# --- AGORATUBE TELEGRAM BOT (V2 - WITH ADMIN FORWARDING) ---
import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURATION ---
# These are read from Render's Environment Variables for security
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')

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

# --- BOT LOGIC ---

# This function handles the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode='Markdown')

# This function handles any photo sent to the bot
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ADMIN_CHAT_ID:
        print("Admin Chat ID is not set. Cannot forward photo.")
        return

    user = update.message.from_user
    photo_file_id = update.message.photo[-1].file_id # Get the highest resolution photo

    # Create a caption with the user's information
    caption = f"New payment proof received!\n\n"
    caption += f"From: {user.first_name}"
    if user.last_name:
        caption += f" {user.last_name}"
    if user.username:
        caption += f" (@{user.username})"
    
    # Forward the photo by its file_id to your admin account
    await context.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=photo_file_id,
        caption=caption
    )
    
    # Send a confirmation message to the user
    await update.message.reply_text("Thank you! Your proof has been submitted for review. You will receive the group link shortly after confirmation.")


# --- WEB SERVER SETUP ---
# Initialize the bot application
application = Application.builder().token(TELEGRAM_TOKEN).build()

# Add the command and message handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

# Initialize the Flask web server
app = Flask(__name__)

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
async def webhook():
    # This is the endpoint Telegram sends updates to
    update_data = request.get_json(force=True)
    update = Update.de_json(update_data, application.bot)
    await application.process_update(update)
    return 'ok'

# A simple route to check if the server is running
@app.route('/')
def index():
    return 'Server is running!'

# This part is not run by Gunicorn, but it's good practice to have.
if __name__ == "__main__":
    # This is for local testing only. Render uses the Procfile.
    pass
