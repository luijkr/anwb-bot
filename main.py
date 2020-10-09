from config import Config
from telegram.ext import Updater, CommandHandler

conf = Config


def callback_timer(context):
    context.bot.send_message(chat_id=conf.CHAT_ID, text='One message every minute')


updater = Updater(conf.TOKEN)
job_queue = updater.job_queue

job_minute = job_queue.run_repeating(callback_timer, interval=5, first=0)
updater.start_polling()
