from telegram.ext import Updater, CommandHandler

import settings




def start_bot(bot, update):
	print(update)
	mytext = """Ну привет тебе, братюнь!

Я простой бот и понимаю только команду start
	"""
	update.message.reply_text(mytext)

	print("start") #пишется "start" в командной строке. это как бы отладочная фиговина



def main():
	updtr = Updater(settings.TELEGRAM_API_KEY, use_context = True)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot)) #когда жмякают start, запускается функция start_bot




	updtr.start_polling()
	updtr.idle()




if __name__ == "__main__":
	main()





