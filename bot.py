from telegram.ext import Updater, CommandHandler

import settings




def start_bot(bot, updater):
	print("start")



def main():
	updtr = Updater(settings.TELEGRAM_API_KEY, use_context = True)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))




	updtr.start_polling()
	updtr.idle()




if __name__ == "__main__":
	main()





