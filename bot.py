import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(bot, update):	
	mytext = """Ну привет тебе, {}!

Твои друзья знают, что ты пидор?
	""".format(update.message.chat.first_name)


	update.message.reply_text(mytext)

def chat(bot,update):
	text = update.message.text.lower() #равно введённому тексту
	username = update.message.chat.username #равно никнейму
	logging.info('{}: {}'.format(username, text)) #логинит то, что написал пользователь
	answers = {"привет":"И тебе привет!", "как дела":"Лучше всех!", "пока":"Увидимся", "not found":"Не понял тебя :("}
	if text in answers:
		return answers[text]
	else:
		return answers["not found"]
	#update.message.reply_text('Сам ' + text)




def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot)) #когда жмякают start, запускается функция start_bot
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat)) #добавили обработчик сообщений. Filters.text - введённый текст. chat - функция, куда передаётся update и bot



	updtr.start_polling()
	updtr.idle()




if __name__ == "__main__":
	logging.info('Bot started')
	main()





