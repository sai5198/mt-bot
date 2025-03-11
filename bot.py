from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7798144467:AAHFgZ8iniMdxnKrQzcxy0NAis9b65vJzQI"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to ShadowCase Bot! Type /mystery to get a random mystery case.")

async def mystery(update: Update, context: CallbackContext):
    await update.message.reply_text("Here's a mystery: A man was found dead in a locked room… What happened?")

# Create the bot application
app = Application.builder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mystery", mystery))

# Run the bot
print("Bot started... Waiting for messages")

app.run_polling()
