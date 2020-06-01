from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater):
	print("start")



def main():
	updtr = Updater('1089476369:AAFSy2_Rmxp02rISWXaoLHK-8eebXhcqWSo', use_context = True)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))




	updtr.start_polling()
	updtr.idle()




if __name__ == "__main__":
	main()





