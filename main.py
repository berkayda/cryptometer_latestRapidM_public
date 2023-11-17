import time
import requests, datetime
from pycryptometer import Cryptometer
c = Cryptometer("eJ62U24MA946GJ0pqs28GLfrGA1xZyHn1bqMV7Tz")
#https://pypi.org/project/pycryptometer/#description
#syntax = c.ANY_OF_THE_CATEGORIES.ANY_OF_THE_FUNCTIONS(THE_ARGS_IT_NEEDS)


def telegram_bot_sendtext(bot_mesaj, id: str):
    bot_token = '5410434254:AAHSxzOQ6hLoiK5myWKCZtdbIwzPXq0nH_Q'
    bot_chatID = id
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(
        bot_chatID) + '&parse_mode=Markdown&text=' + bot_mesaj
    response = requests.get(url)


def rapid_movements():
    last_rapidM = None
    while True:
        rapidM = c.infos.rapid_movements()  # Pump-Dump #PARSE
        if rapidM != last_rapidM:
            timestamp = rapidM[0]['timestamp']
            dt_object = datetime.datetime.fromisoformat(timestamp[:-1])
            formatted_time = dt_object.strftime("%d/%m/%Y %H:%M:%S")

            pair = "Pair: " + rapidM[0]['pair']
            exchange = "Exchange: " + rapidM[0]['exchange']
            changeDetected = "Change detected: % " + str(rapidM[0]['change_detected'])
            side = "Side: " + rapidM[0]['side']
            UTCtime = formatted_time + " UTC"

            print()
            print(pair)
            print(exchange)
            print(changeDetected)
            print(side)
            print(UTCtime)
            print()
            telegram_bot_sendtext(pair + "\n" + exchange + "\n" + changeDetected + "\n" + side + "\n" + UTCtime, -1001919037999)
            last_rapidM = rapidM
        else:
            print("No new data available.")
        time.sleep(30)

if __name__ == '__main__':
    rapid_movements()
