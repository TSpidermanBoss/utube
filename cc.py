from telegram.ext import Updater
updater = Updater(token='696541972:AAE3EQpvWHocxWp-lnJSgUwaVXOrFg-7upI', use_context=True)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

updater.start_polling()
