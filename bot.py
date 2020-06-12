import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
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
	result = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(city, settings.WEATHER_KEY))

	if result.status_code == 200:
		weather = {}
		weather = result.json()
		timestamp = weather['dt']
		time_now = datetime.datetime.fromtimestamp(timestamp)

		final = "Погода в городе {}, {}.\n\n".format(weather['name'], time_now.strftime('%H:%M %d.%m.%Y))
		final += "Погода: {} - {}.\n\n".format(weather['weather'][0]['main'], weather['weather'][0]['description'])
		final += "Температура: {} C, ощущается, как: {} C.\n".format(weather['main']['temp'], weather['main']['feels_like'])
		final += "Давление: {} мм.рт.ст. Влажность: {} %.\n\n".format(weather['main']['pressure']*0.75,weather['main']['humidity'])

		wind_course = weather['wind']['deg']
		if wind_course >= 337.5 and wind_course < 22.5:
			wind_course = 'северный'
		elif wind_course >= 22.5 and wind_course < 67.5:
			wind_course = 'северо-восточный'
		elif wind_course >= 67.5 and wind_course < 112.5:
			wind_course = 'восточный'
		elif wind_course >= 112.5 and wind_course < 137.5:
			wind_course = 'юго-восточный'
		elif wind_course >= 137.5 and wind_course < 202.5:
			wind_course = 'южный'
		elif wind_course >= 202.5 and wind_course < 247.5:
			wind_course = 'юго-западный'
		elif wind_course >= 247.5 and wind_course < 292.5:
			wind_course = 'западный'
		elif wind_course >= 292.5 and wind_course < 337.5:
			wind_course = 'северо-западный'
		else:
			wind_course = 'ошибка :('

		final += "Ветер - {}, скорость - {} метр/сек.\n".format(wind_course, weather['wind']['speed'])



		return (final)



	else:
		return("Сервер не отвечает :(")





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
