from random import randint; from telebot import types

mainmenu = types.KeyboardButton("В главное меню 🏠") ## Создаем кнопки для главного меню и не только
btnh = types.KeyboardButton("/help"); btne = types.KeyboardButton("/example"); btng = types.KeyboardButton("/game список")
btn1 = types.KeyboardButton("Сайори, привет"); btn2 = types.KeyboardButton("Сайори, как дела?"); btn3 = types.KeyboardButton("Сайори, что делаешь?"); btn4 = types.KeyboardButton("Сайори, пришли фанарт 🎨")
btn5 = types.KeyboardButton("Сайори, пришли катсцену 🖼"); btn6 = types.KeyboardButton("Сайори, пришли совместимость зз ♈"); btn7 = types.KeyboardButton("Доброе утро ☀"); btn8 = types.KeyboardButton("Спокойной ночи 🌑")
btn9 = types.KeyboardButton("/track список"); btn10 = types.KeyboardButton("Сайори, поздравь меня"); btn11 = types.KeyboardButton("Сайори, расскажи шутку"); btn12 = types.KeyboardButton("Сайори, как твое настроение")
markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=False); markup.row(btnh, btne, btng); markup.row(btn1, btn2, btn3); markup.row(btn4, btn5); markup.row(btn7, btn8); markup.row( btn10, btn11, btn12)

def play_easy(bot, chatId, is_game_active):
    if is_game_active:
        return

    sayoriselect_easy = randint(1, 5)
    bot.send_message(chatId, "Я загадала число, время угадывать! Это число 1 до 5.")

    def ask_iscorrectnumber(message):
        text = message.text.lower()
        if not text.isdigit(): bot.send_message(chatId, "Тебе нужно прислать цифру! Не нужно писать что-то лишнее!")
        elif text == str(sayoriselect_easy):
            bot.send_message(chatId, "Надо же! Ты смог угадать! Поздравляю тебя, солнышко!", reply_markup=markup)
        else:
            bot.send_message(chatId, f"Ты был близок, верным ответом было число {sayoriselect_easy}", reply_markup=markup)

    return ask_iscorrectnumber

def play_normal(bot, chatId, is_game_active):
    if is_game_active:
        return

    sayoriselect_normal = randint(1, 10)
    bot.send_message(chatId, "Я загадала число, время угадывать! Это число 1 до 10.")

    def ask_iscorrectnumber(message):
        text = message.text.lower()
        if not text.isdigit(): bot.send_message(chatId, "Тебе нужно прислать цифру! Не нужно писать что-то лишнее!")
        elif text == str(sayoriselect_normal):
            bot.send_message(chatId, "Надо же! Ты смог угадать! Поздравляю тебя, солнышко!", reply_markup=markup)
        else:
            bot.send_message(chatId, f"Ты был близок, верным ответом было число {sayoriselect_normal}", reply_markup=markup)

    return ask_iscorrectnumber

def play_hard(bot, chatId, is_game_active):
    if is_game_active:
        return

    sayoriselect_hard = randint(1, 20)
    bot.send_message(chatId, "Я загадала число, время угадывать! Это число 1 до 20.")

    def ask_iscorrectnumber(message):
        text = message.text.lower()
        if not text.isdigit(): bot.send_message(chatId, "Тебе нужно прислать цифру! Не нужно писать что-то лишнее!")
        elif text == str(sayoriselect_hard):
            bot.send_message(chatId, "Надо же! Ты смог угадать! Поздравляю тебя, солнышко!", reply_markup=markup)
        else:
            bot.send_message(chatId, f"Ты был близок, верным ответом было число {sayoriselect_hard}", reply_markup=markup)

    return ask_iscorrectnumber
