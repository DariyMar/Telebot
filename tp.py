
import telebot


bot = telebot.TeleBot('5456394807:AAHBpWaqWE7sSW0KAFkTvoEqZj3grtI-RQQ')
@bot.message_handler(commands=['start'])


def start(message):
    user_name = f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}, введите первый общий вес, второй общий вес и вес поддона через пробел, без каких либо других символов за исключением точки (не запятой), если число дробное.По образцу:"  124 105 15  " или же "  124.5 105.5 15.5  ":</b>'
    bot.send_message(message.chat.id, user_name, parse_mode='html')

@bot.message_handler()
def get_user_text(message):

    x = list(message.text.split())
    if x[0].replace(".", "").isdigit() and x[1].replace(".", "").isdigit() and x[2].replace(".", "").isdigit():
        v_1 = float(x[0]) - float(x[2])
        v_2 = float(x[1]) - float(x[2])
        res = (v_2 / v_1)*100 - 100
        bot.send_message(message.chat.id, round(res, 2), parse_mode='html')

    else:
       bot.send_message(message.chat.id,f'<b>Введите корректные числа через пробел, если числа дробные - разделите их ТОЧКОЙ, по образцу: "  124 105 15  " или же "  124.5 105.5 15.5  ":</b>', parse_mode='html')

bot.polling(none_stop=True)