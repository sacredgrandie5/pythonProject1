import telebot
import requests
import json


TOKEN = '6246241522:AAGPx1QB3L_Wwd4fQ0pWAOwfeXzhpP9Jb7A'


bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}


class ConvertionException(Exception):
    pass


class Cryptoconverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно ввести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        expect KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        expect KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base}.')

        try:
            amount = float(amount)
        expect valueError:
            raise ConvertionException(f'Неудалось обработать валюту {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду бота в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n Увидеть список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    value = message.text.split(' ')

    if len(values) !> 3
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values
    total_base = Cryptoconverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()