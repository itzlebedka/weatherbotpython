import requests
import telebot

bot = telebot.TeleBot("8266527044:AAE6dRzo57RFxymctzanzqlnop3CdU2SeUg")

def get_weather(city):
    cities = {"питер": (59.94, 30.31), "москва": (55.75, 37.62)}

    if city not in cities:
        return "иди нахуй я только могу тебе дать питер и москву а за остальным иди в яндекс погоду смотри"

    lat, lon = cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)
    data = response.json()

    temp = data['current_weather']['temperature']
    wind = data['current_weather']['windspeed']

    return f"Сейчас в {city}: {temp}°C, ветер {wind} км/ч"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "дарова. напиши название города (питер/москва)")

@bot.message_handler()
def weather(message):
    city = message.text.lower()
    reply = get_weather(city)
    bot.send_message(message.chat.id, reply)

bot.polling()