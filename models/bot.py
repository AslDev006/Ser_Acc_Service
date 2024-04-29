from telebot import TeleBot
import environ
env = environ.Env()
environ.Env.read_env()


bot = TeleBot(token=env("TOKEN"))



ids = [5823007647, 5322589899]
for i in ids:
    def get_post(data):
        bot.send_message(chat_id=i, text=f"Sizga yangi murojaat mavjud !\n\n\n"
                                              f"Ism: {data['name']}\n"
                                              f"Telefon Raqam: {data['phone_number']}")