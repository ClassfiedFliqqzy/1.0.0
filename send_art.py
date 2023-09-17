import random; import telebot
import time; from randomfile import pwd

bot = telebot.TeleBot('5568779412:AAFbQBM0RNZtWGGHYDWtWea8ZGwpugOT1lU', skip_pending=True)

sending_art = False; sending_cg = False

def sent_art(chatId, message):
    global sending_art  # Объявляем переменную как глобальную
    if not sending_art:
        try:
            sending_art = True; path1 = pwd("fanart")
            random_filename = str(random.choice(path1)); cg = open((random_filename), "rb")
            bot.send_chat_action(chatId, "upload_photo"); time.sleep(3); bot.send_photo(chatId, cg, timeout=540)
        except Exception: bot.reply_to(message, "Отправка файла немного задерживается, пожалуйста, подождите..."); return sent_art
        finally: sending_art = False
    else: bot.reply_to(message, "Я отправляю фанарт пользователю, пожалуйста, попробуйте использовать команду через 10-20 секунд. 😌")

def sent_cg(chatId, message):
    global sending_cg  # Объявляем переменную как глобальную
    if not sending_cg:
        try:
            sending_cg = True; path1 = pwd("sayori_cg")
            random_filename = str(random.choice(path1)); cg = open((random_filename), "rb")
            bot.send_chat_action(chatId, "upload_photo"); time.sleep(3); bot.send_photo(chatId, cg, timeout=540); return sent_cg
        except Exception: bot.reply_to(message, "Отправка файла немного задерживается, пожалуйста, подождите...")
        finally: sending_cg = False
    else: bot.reply_to(message, "Я отправляю катсцену пользователю, пожалуйста, попробуйте использовать команду через 10-20 секунд. 😌")