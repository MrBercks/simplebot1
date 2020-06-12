import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(bot, update):
	mytext = """Привет, {}!

Я простой бот, который может только подсказать погоду и немного поддержать беседу. Для запроса погоды напиши \"погода в городе Москва\" или впиши другой город.
	""".format(update.message.chat.first_name)
	update.message.reply_text(mytext)

def get_weather(city):
	result = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID{}'.format(city, settings.WEATHER_KEY))
	return (result.json())



def chat(bot,update):
	text = update.message.text.lower() #равно введённому тексту
	username = update.message.chat.username #равно никнейму
	logging.info('{}: {}'.format(username, text)) #логинит то, что написал пользователь
	answers = {"привет":"И тебе привет!", "как дела":"Лучше всех!", "пока":"Увидимся"}
	if text in answers:
		return update.message.reply_text(answers[text])
	else:
		words = text.split(' ')
		if len(words) == 2 and words[0] == 'погода':
			update.message.reply_text(get_weather(words[1])) #возвращает погоду
		else:
			return update.message.reply_text("Не понял тебя :( \n\nДля запроса погоды напиши \"погода Moscow\" или впиши другой город.")
	#update.message.reply_text('Сам ' + text)


def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot)) #когда жмякают start, запускается функция start_bot
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat)) #обработчик сообщений.Filters.text-введённый текст.chat-функция,куда передаётся update и bot

	updtr.start_polling()
	updtr.idle()




if __name__ == "__main__":
	logging.info('Bot started')
	main()
