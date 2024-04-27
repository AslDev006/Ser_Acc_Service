from telebot import TeleBot
import environ
env = environ.Env()
environ.Env.read_env()


bot = TeleBot(token=env("TOKEN"))




def get_post(data):
    bot.send_message(chat_id=5322589899, text=f"Sizga yangi murojaat mavjud !\n\n\n"
                                              f"Ism: {data['name']}\n"
                                              f"Telefon Raqam: {data['phone_number']}")