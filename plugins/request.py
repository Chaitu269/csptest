import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Enter your bot token here
TOKEN = 'BOT_TOKEN'

# Enter your admin chat id here
ADMIN_CHAT_ID = 'ADMINS'

def request(update, context):
    """Send a message to the bot's admin requesting action."""
    message = update.message
    user = message.from_user
    text = message.text

    # Send the request to the admin chat
    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"New request from {user.username}:\n{text}")

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register message handler to forward messages to admin
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, request))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
