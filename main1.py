import logging
import requests

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

import config1


def start(bot, update):
    update.effective_message.reply_text("Hi {}!".format(update.effective_user.username))
    logger.debug('/start')


def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)
    logger.debug('/echo')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + (r.text) + '</pre>')


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='bot1.log')
    logger = logging.getLogger(__name__)

    updater = Updater(config1.token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(config1.port), url_path=config1.token)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(config1.name, config1.token))
    # updater.start_polling()

    updater.idle()
