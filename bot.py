import logging
from telegram.ext import Updater, CommandHandler
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(bot, update):
	print(update)
	
	mytext = """Ну привет тебе, {}!

Я простой бот и понимаю только команду start
	""".format(update.message.chat.first_name)

	update.message.reply_text(mytext)


def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot)) #когда жмякают start, запускается функция start_bot




	updtr.start_polling()
	updtr.idle()




if __name__ == "__main__":
	logging.info('Bot started')
	main()





