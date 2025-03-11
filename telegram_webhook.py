from flask import Flask, request
import telebot

TOKEN = "7798144467:AAHFgZ8iniMdxnKrQzcxy0NAis9b65vJzQIOKEN"  # Replace with your actual Telegram bot token
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is set up with a webhook!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
