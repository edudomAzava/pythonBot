import telebot
import requests

bot = telebot.TelleBot("")
weatherMapAPI = ""

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, "Привямба" + message.text)

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    #res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}')
    #bot.reply_to(message, f'{res.json()}')

bot.polling(none_stop = True)
