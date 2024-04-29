from telebot import TeleBot
import environ
env = environ.Env()
environ.Env.read_env()


bot = TeleBot(token=env("TOKEN"))



ids = [5322589899, 5823007647]
for i in ids:
    def get_post(data):
        print(i)
        bot.send_message(chat_id=i, text=f"Sizga yangi murojaat mavjud !\n\n\n"
                                              f"Ism: {data['name']}\n"
                                              f"Telefon Raqam: {data['phone_number']}")