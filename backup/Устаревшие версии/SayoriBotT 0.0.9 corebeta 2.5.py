
import re; import os; import sys; import json
import time; import random; import telebot; import threading
import logging; import datetime; import colorama; import subprocess

from sayorilists import * #from something import somethings
from randomfile import pwd; from os import scandir, getcwd, execl
from translate import Translator; from colorama import Fore, Back, Style
from langdetect import detect; from rockpapers import rock_paper_scissors
from plyer import notification; from re import search; from gtts import gTTS
from random import randint; from telebot import types; from threading import Timer
from gamerandoms import play_easy, play_normal, play_hard; from os.path import abspath
from datetime import datetime; from numbersrand import sixnumber; from send_art import sent_art, sent_cg

class IgnoreErrorFilter(logging.Filter):
    def filter(self, record): ## Создаем активный фильтр для следующих типов ошибки
        return "ReadTimeout" not in record.getMessage() and "ConnectionError" not in record.getMessage()

## Вход в аккаунт чат-бота и активация заданных параметров запуска.
ignore_error_filter = IgnoreErrorFilter() ## Фильтр для log.txt записей и ошибок
logger = logging.getLogger(__name__); logger.addFilter(ignore_error_filter); colorama.init() ## Включение библиотеки Colorama
bot = telebot.TeleBot('5568779412:AAFbQBM0RNZtWGGHYDWtWea8ZGwpugOT1lU', skip_pending=True) ## Токен и пропуск старых сообщений
logging.basicConfig(filename="log.txt", format='[%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S]', level=logging.INFO)

## Начальное сообщение о включении бота и его текущее состояние (для терминала на сервере)
print("\nИдентификация, выполняется вход в аккаунт чат-бота Telegram: ", Fore.CYAN + "— Сᴀйᴏᴘᴜ • ;")
print(Fore.WHITE + "Краткий справочник по командам: /help - список всех команд, !cls - очистить терминал бота.")
print("Сайори (Telegram) была создана Moxiess, ее цели - помощь администрации и общение с участниками!")
time.sleep(1); print(Fore.LIGHTYELLOW_EX + "\nБот запущен на версии 0.0.9 ч.2 Dialogcore, активирование функции логгирования чатов...", Fore.CYAN + "OK")
time.sleep(1); print(Fore.WHITE+ " ⁞ Вывод истории чатов был отключен. Идет регистрация системных сообщений бота в терминале.\n")

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def handle_new_members(message): ## Запускаем обработку и поиск уведомлений о юзерах
    if message.new_chat_members: ## Если были найдены новые пользователи в чате - приветствуем их
        for member in message.new_chat_members: ## Вытаскиваем уведомление о пользователе и работаем
            bot_id = bot.get_me().id ## Определяем новую переменную - получаем ID нашего чат-бота
            if not member.is_bot and member.id != bot_id: ## Если юзер не бот - приветствуем
                bot.send_message(message.chat.id, f"Добро пожаловать в группу, {member.first_name}!")
    elif message.left_chat_member: ## Если были найдены ушедшие пользователи - прощаемся с ними
        if not getattr(message.left_chat_member, 'is_bot', False) and hasattr(message.left_chat_member, 'first_name'):
            bot.send_message(message.chat.id, f"Прощай, {message.left_chat_member.first_name}, мы будем по тебе скучать. :<")

@bot.message_handler(content_types=['text', 'photo', 'voice']) ## Поиск сообщений по типу: текст и фотографии
def get_text_messages(message): ## Запускается handle на обработку и отправку сообщений в чаты, группы и т.п.

    def check_admin_rights(chat_id, user_id): ## Проверка на админа
        chat_member = bot.get_chat_member(chat_id=chat_id, user_id=user_id)
        return chat_member.status in ['administrator', 'creator']

    t = time.localtime() ## Определение времени на компьютере
    content = message.text ## Содержимое сообщения и его контента
    mydate = datetime.now() ## Получение текущего месяца (через ПК)
    month = mydate.strftime("%B") ## Выдать название текущего месяца
    chatId = message.chat.id ## Внутренний адрес чата ЛС / группы ID
    chatName = message.chat.title ## Заголовок чата группы, ЛС и т.п
    messageId = message.message_id ## Внутренний адрес сообщения чата
    userId = message.from_user.id ## Получаем внтуренний айди пользов.
    username = message.from_user.username ## Имя пользователя в ТГ ID
    lastname = message.from_user.last_name ## Фамилия пользователя ТГ
    firstname = message.from_user.first_name ## Имя пользователя в ТГ

    current_time = time.strftime("%H:%M:%S", t) ## Вывод времени в 24-часовом формате (00:00:00)
    if lastname is None: lastname = "[Не задано]" ## Если фамилия участника неизвестна - вывести фамилию в [Не задано]
    if chatName is None: chatName = firstname + " (ЛС)" ## Если название чата неизвестно - вывести имя написавшего и приписку ЛС
    if username is None: username = firstname ## Если имя пользователя не существует - то мы выведем его первое имя для логирования.
    if username == 'Channel_Bot' or username == 'GroupAnonymousBot': username = chatName ## Вывести название чата, если пользовать анон.
    if chatName == 'Telegram': chatName = message.chat.title ## Если любой из каналов выложил пост - выведем его название, ибо логи не могут.
    if message.content_type == 'photo': ## Если пользователь отправил изображение - то мы пробуем его переслать в логи
        try: content = "[🖼]"; bot.forward_message(chat_id='-1001927267798', from_chat_id=chatId,  message_id=messageId) ## Получаем фотографию
        except: pass ## Для того что бы избежать засорения логов сообщениями о невозможности перессылки - мы просто пропустим ошибку и пойдем дальше.
    if message.content_type == 'voice': ## Если пользователь отправил голосовое сообщение - то мы пробуем его переслать в логи
        try: content = "[🎙]"; bot.forward_message(chat_id='-1001927267798', from_chat_id=chatId,  message_id=messageId) ## Получаем ГС (голос)
        except: pass ## Для того что бы избежать засорения логов сообщениями о невозможности перессылки - мы просто пропустим ошибку и пойдем дальше.

    ## Вывод в реальном времени данных о имени пользователя, названии чата, содержании сообщения и т.п.
    maintenance_mode = False ## Включение режима отладки и проверки чат-бота (при проведении тех.работ - значение должно быть True), старый вариант
    #if maintenance_mode == True and username != "ElliotMoxiess": return ## Если включен режим отладки и проверки чат-бота - пользователь писать не может
    time.sleep(1); bot.send_message(chat_id='-1001927267798', text=f"[ {current_time} ] [ {username} ] {content} [ Название чата: {chatName} (Идентификатор: {chatId}) ]")

    ## Блок №1: Основные функции и тело бота (команды с использованием символа /).
    ## Действия Сайори при выполнении команды /start (Вывод приветственного сообщения и небольшое меню с действиями)
    if content.lower() == "/start" and chatName == firstname + " (ЛС)":
        welcomepictureofsayori = open(("pictures/welcome.png"), "rb"); reply = open('!replies/welcomelist.txt', 'r', encoding='utf8')
        captions = reply.read(); bot.send_chat_action(chatId, "upload_photo"); bot.send_photo(chatId, welcomepictureofsayori, caption=captions, reply_markup=markup, parse_mode="html")   
    elif content.lower() == "/start@sunnyddlc_bot":
        welcomepictureofsayori = open(("pictures/welcome.png"), "rb"); reply = open('!replies/welcomelist.txt', 'r', encoding='utf8');
        captions = reply.read(); bot.send_chat_action(chatId, "upload_photo"); bot.send_photo(chatId, welcomepictureofsayori, caption=captions, parse_mode="html")

    ## Действия Сайори при выполнении команды /aboutsunny (Справочная команда для вывода информации о ситуации с Сайори в Амино)
    if content.lower() == "/aboutsunny" or content.lower().startswith("что стало с сайори в амино"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('!replies/sayorikz.txt', 'r', encoding='utf8'); bot.reply_to(message, reply)

    ## Действия Сайори при выполнении команды /creator (Справочная команда для вывода информации о создателе)
    if content.lower() == "/creator" or content.lower() == "!создатель": 
        reply = open('!replies/creatorlist.txt', 'r', encoding='utf8'); answer = reply.read()
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, answer); reply.close()

    ## Действия Сайори при выполнении команды /settings (Персональные настройки для чат-бота Сайори в Telegram)
    if content.lower() == "/settings" or content.lower() == "/settings@sunnyddlc_bot":
        bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('!replies/settingslist.txt', 'r', encoding='utf8'); bot.reply_to(message, reply)

    ## Действия Сайори при выполнении команды /status (Справочная команда, позволяющая узнать рабочий статус Сайори)
    if content.lower().startswith("/status") or content.lower().startswith("!статус"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        elif __name__ == '__main__': bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, "Я нахожусь в сети, ожидаю ваши дальнейшие запросы!")
        else: bot.reply_to(message, "К сожалению, мне не удается связаться с сервером и обработать запрос.")

    ## Действия Сайори при выполнении команды /help (Справочная служба для вывода всех доступных команд и не только)
    if content.lower() in ['/help', '!помощь', '/help@sunnyddlc_bot', '< первая страница']:
        if chatName == firstname + " (ЛС)": ## Если чат является личными сообщениями, то мы выведем кнопки для пользователя
            reply = open('!replies/helpservice/helplist.txt', 'r', encoding='utf8')
            answer = reply.read(); bot.send_message(chatId, answer, reply_markup=helpmark, parse_mode="html"); reply.close()
        else:
            reply = open('!replies/helpservice/helplist.txt', 'r', encoding='utf8'); answer = reply.read()
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, answer, parse_mode="html"); reply.close()
    elif content.lower() in ['/help1', '!помощь1', '/help1@sunnyddlc_bot', 'вторая страница <', 'вторая страница >']:
        if chatName == firstname + " (ЛС)": ## Если чат является личными сообщениями, то мы выведем кнопки для пользователя
            reply = open('!replies/helpservice/helplist1.txt', 'r', encoding='utf8')
            answer = reply.read(); bot.send_message(chatId, answer, reply_markup=page2mark, parse_mode="html"); reply.close()
        else:
            reply = open('!replies/helpservice/helplist1.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer, parse_mode="html"); reply.close()
    elif content.lower() in ['/help2', '!помощь2', '/help2@sunnyddlc_bot', 'третья страница >']:
        if chatName == firstname + " (ЛС)": ## Если чат является личными сообщениями, то мы выведем кнопки для пользователя
            reply = open('!replies/helpservice/helplist2.txt', 'r', encoding='utf8')
            answer = reply.read(); bot.send_message(chatId, answer, reply_markup=page3mark, parse_mode="html"); reply.close()
        else:
            reply = open('!replies/helpservice/helplist2.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer, parse_mode="html"); reply.close()

    ## Действия Сайори при возвращении в главное меню с кнопками и быстрыми действиями (не слеш команда, главное меню button)
    if content.lower().startswith("в главное меню") and chatName == firstname + " (ЛС)":
        bot.send_message(chatId, "Вы вернулись в мое главное меню, чем я могу вам помочь?", reply_markup=markup)    

    ## Действия Сайори при выполнении команды /example (Справочная служба для вывода примеров команд и не только)
    if content.lower() in ['/example', '!пример', '/example@sunnyddlc_bot', 'первая страница 1️⃣']:
        if chatName == firstname + " (ЛС)": ## Если чат является личными сообщениями, то мы выведем кнопки для пользователя
            reply = open('!replies/exampleservice/examplelist.txt', 'r', encoding='utf8')
            answer = reply.read(); bot.send_message(chatId, answer, reply_markup=examplemark, parse_mode="html"); reply.close()
        else:
            reply = open('!replies/exampleservice/examplelist.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
    elif content.lower() in ['/example1', '!пример1', '/example1@sunnyddlc_bot', 'вторая страница 2️⃣']:
        if chatName == firstname + " (ЛС)": ## Если чат является личными сообщениями, то мы выведем кнопки для пользователя
            reply = open('!replies/exampleservice/examplelist1.txt', 'r', encoding='utf8')
            answer = reply.read(); bot.send_message(chatId, answer, reply_markup=example2mark, parse_mode="html"); reply.close()
        else:
            reply = open('!replies/exampleservice/examplelist1.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
    elif content.lower() in ['/example2', '!пример2', '/example2@sunnyddlc_bot', 'третья страница 3️⃣']:
        if chatName == firstname + " (ЛС)": ## Если чат является личными сообщениями, то мы выведем кнопки для пользователя
            reply = open('!replies/exampleservice/examplelist2.txt', 'r', encoding='utf8')
            answer = reply.read(); bot.send_message(chatId, answer, reply_markup=example3mark, parse_mode="html"); reply.close()
        else:
            reply = open('!replies/exampleservice/examplelist2.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()    

    ## Действия Сайори при выполнении команды /update (Команда, которая выводит информацию о текущих изменениях и обновлениях)
    if content.lower().startswith("!обновления") or content.lower().startswith("/update"):
        reply = open('!replies/updatelist.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing")
        time.sleep(3); answer = reply.read(); bot.reply_to(message, answer, parse_mode="html"); reply.close()

    ## Действия Сайори при выполнении команды /about (Справочная команда для вывода информации о профиле)
    if content.lower().startswith("/aboutprofile") or content.lower().startswith("о профиле"):
        reply = open('!replies/aboutprofile.txt', 'r', encoding='utf8'); about_text = reply.read(); bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, about_text.format(firstname=firstname, lastname=lastname, username=username, chatName=chatName, chatId=chatId))

    ## Реакция Сайори на команду Вопрос, /ask (Можно задать вопрос Сайори и она ответит на него)
    if content.lower().startswith("/inquiry "): question = message.text[9:]
    elif content.lower().startswith("вопрос, "): question = message.text[8:]
    else: question = None ## Ответ пользователя оказался пустым, пропускаем дальнейшие услов.
    if question is not None: ## Если ответ оказался не пустым - читаем что пользователь задал
        if question.lower().startswith("ты любишь меня"):
            bot.reply_to(message, str(random.choice(answ1)))
        elif question.lower().startswith("ты хочешь меня"):
            bot.reply_to(message, str(random.choice(answ2)))
        elif question.lower().startswith("какой твой любимый напиток"):
            reply = open('!replies/questionservice/favouritedrink.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif question.lower().startswith("какие сладости ты любишь"):
            reply = open('!replies/questionservice/favouritesweets.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif question.lower().startswith(tuple(keyword7)): ## Вопрос, касаемо желания смерти людям
            reply = open('!replies/questionservice/aboutmurderer.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif question.lower().startswith(tuple(keyword5)): ## Вопрос, касаемо отношения Сайори к зиме
            reply = open('!replies/questionservice/aboutwinter.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif question.lower().startswith('какой сегодня месяц'): ## Вопрос, касаемо того какой сегодня месяц и что планируется
            reply = open('!replies/questionservice/monthfortoday.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, answer.format(month=month)) ## Так как параметр {month} в текстовом формате - его нужно переконвертировать в f
        elif question.lower().startswith(tuple(keyword8)): ## Вопрос, разбирается ли Сайори в мемах / приколах
            reply = open('!replies/questionservice/aboutmemes.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif question.lower().startswith(tuple(keyword9)): ## Вопрос, какое аниме может посоветовать Сайори
            reply = open('!replies/questionservice/aboutanime.txt', 'r', encoding='utf8') 
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif question.lower().startswith(tuple(strangequestions)): bot.reply_to(message, str(random.choice(answ9))) ## Вопрос, связанный с убийством и кровью
        else: bot.reply_to(message, str(random.choice(lis)))

    ## Реакция Сайори на команду /wiki (Справочная команда для вывода информации и фактах о персонадах из ДДЛК)
    if content.lower() in ['/wiki', '/wiki@sunnyddlc_bot', '!вики']:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Сайори 🎀', callback_data='о сайори')) ## Сайори
        keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Юри 📖', callback_data='о юри')) ## Юри (Yuri)
        keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Монике 🖍', callback_data='о монике')) ## Моника
        keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Нацуки 🧁', callback_data='о нацуки')) ## Нацуки
        reply = open('!replies/wikilist.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_message(chatId, answer, reply_markup=keyboard); reply.close()         

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.data == "о сайори":
            bot.send_message(call.message.chat.id, str(random.choice(aboutsunny))) ## Краткие факты о Сайори
            sayori = open(("pictures/sayoriddlc.png"), "rb"); bot.send_photo(call.message.chat.id, sayori)
        elif call.data == "о юри":
            bot.send_message(call.message.chat.id, str(random.choice(aboutyuri)))
            yuri = open(("pictures/yuriddlc.png"), "rb"); bot.send_photo(call.message.chat.id, yuri)
        elif call.data == "о монике":
            bot.send_message(call.message.chat.id, str(random.choice(aboutmonika))) ## Краткие факты о Монике
            monika = open(("pictures/monikaddlc.png"), "rb"); bot.send_photo(call.message.chat.id, monika)
        elif call.data == "о нацуки":
            bot.send_message(call.message.chat.id, str(random.choice(aboutnatsuki))) ## Краткие факты о Нацуки
            natsuki = open(("pictures/natsukiddlc.jpg"), "rb"); bot.send_photo(call.message.chat.id, natsuki)

    ## Сайори реагирует на упоминание ее имени в сообщении пользователя и выдает реакции (С1)
    if content.lower().startswith("сайори "): sayori1 = message.text[7:] ## Обрезание сообщения до нужных символов
    elif content.lower().startswith("сайори, "): sayori1 = message.text[8:] ## Обрезание сообщения до нужных символов
    elif content.lower().startswith("сайори"): sayori1 = message.text[7:] ## Обрезание сообщения до нужных символов
    else: sayori1 = None
    if sayori1 is not None:
        if sayori1.lower().startswith("привет"): ## Поприветствовать Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis3)))
        elif sayori1.lower().startswith(tuple(keyword18)): ## Узнать как дела у Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ3)))
            def ask_doings(message):
                context = message.text.strip()
                if any(keyword in context.lower() for keyword in keyword27):
                    bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ18))) ## Есои все нормально - отвечаем вот так.
                elif any(keyword in context.lower() for keyword in keyword28):
                    bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ19))) ## Есои все отлично - отвечаем вот так.
                elif any(keyword in context.lower() for keyword in keyword29):
                    bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ20))) ## Есои все плохо - отвечаем вот так.
            bot.register_next_step_handler(message, ask_doings)
        elif sayori1.lower().startswith(tuple(keyword19)): ## Узнать чем занимается Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ4)))
        elif sayori1.lower().startswith(tuple(hatereaction)): ## Реакция на ненависть к Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ7)))
        elif sayori1.lower().startswith("не грусти"): ## Реакция Сайори на поддержку
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ8)))
        elif sayori1.lower().startswith(tuple(keyword21)): ## Пользователь просит поздравить Сайори с чем-то
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ14)))
        elif sayori1.lower().startswith(tuple(keyword23)): ## Пользователь спрашивает чем Сайори хочет заняться
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ15)))
        elif sayori1.lower().startswith(tuple(keyword24)): ## Пользователь спрашивает все ли в порядке с Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ16)))
        elif sayori1.lower().startswith(tuple(keyword25)): ## Пользователь спрашивает не умерла ли Сайори (активна)
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ17)))
        elif sayori1.lower().startswith(tuple(keyword14)): ## Пользователь просит Сайори рассказать шутку
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(funnyjokes)))
        elif sayori1.lower().startswith(tuple(keyword22)): ## Пользователь спрашивает Сайори как ее зовут (Идиоты что ли)
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(namequestion)))
        elif sayori1.lower().startswith(tuple(keyword26)): ## Пользователь спрашивает Сайори находится ли она в чате
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis13)))
        elif sayori1.lower().startswith(tuple(compliments)): ## Реакция Сайори на комплименты (она их обожает)
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis11)))
        elif sayori1.lower().startswith(tuple(keyword15)): ## Признание Сайори в чувствах (любовь-морковь ура)
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis8)))  
        elif sayori1.lower().startswith("повтори за мной") or sayori1.lower().startswith("повтори за мной "):
            sayori2 = message.text[25:]; bot.reply_to(message, sayori2) ## Сайори повторяет слова, которые сказал пользователь
        elif sayori1.lower().startswith(tuple(keyword10)): ## Реакция Сайори на вопрос касаемо ее настроения
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ10)))
            def ask_doings(message):
                context = message.text.strip()
                if any(keyword in context.lower() for keyword in keyword27):
                    bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ18))) ## Есои все нормально - отвечаем вот так.
                elif any(keyword in context.lower() for keyword in keyword28):
                    bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ19))) ## Есои все отлично - отвечаем вот так.
                elif any(keyword in context.lower() for keyword in keyword29):
                    bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ20))) ## Есои все плохо - отвечаем вот так.
            bot.register_next_step_handler(message, ask_doings)
        elif sayori1.lower().startswith(tuple(keyword11)): ## Реакция Сайори на необходимость моральной поддержки
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(react1)))
        elif sayori1.lower().startswith(tuple(keyword13)): ## Реакция Сайори на ее попытку "заснуть"
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ11)))
        elif sayori1.lower().startswith("переведи на английский: "):
            trans_text = message.text[31:]; translator = Translator(from_lang ="autodetect", to_lang="en"); translated_text = translator.translate(trans_text) 
            if translated_text == 'PLEASE SELECT TWO DISTINCT LANGUAGES':
                bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, "К сожалению я не умею работать с данным языком, попробуй перевести что-то другое. 😌")
            else: bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, f"Вот ваш перевод на английский: {translated_text}") ## Сайори переводит с любого языка на англ.
        elif sayori1.lower().startswith("переведи на русский: "):
            trans_text = message.text[28:]; translator = Translator(from_lang ="autodetect", to_lang="ru"); translated_text = translator.translate(trans_text) 
            if translated_text == 'PLEASE SELECT TWO DISTINCT LANGUAGES':
                bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, "К сожалению я не умею работать с данным языком, попробуй перевести что-то другое. 😌")
            else: bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, f"Вот ваш перевод на русский: {translated_text}") ## Сайори переводит с любого языка на русс.
        elif sayori1.lower() in ['пришли фанарт', 'пришли арт', 'пришли фанарт 🎨']: sent_art(chatId, message) ## Попросить прислать фанарт из ДДЛК
        elif sayori1.lower() in ['пришли катсцену', 'пришли cg', 'пришли катсцену 🖼']: sent_cg(chatId, message) ## Попросить прислать катсцену из ДДЛК
        elif sayori1.lower().startswith('какой сегодня месяц'): ## Реакция Сайори на вопрос касаемо текущего месяца
            reply = open('!replies/questionservice/monthfortoday.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, answer.format(month=month)) ## Так как параметр {month} в текстовом формате - его нужно переконвертировать в f
        elif sayori1.lower().startswith("назови число от ") or sayori1.lower().startswith("выбери число от "):
            bounds = message.text[24:].split(" до "); lower_bound = bounds[0]; upper_bound = bounds[1]
            if not lower_bound.isdigit() or not upper_bound.isdigit(): bot.reply_to(message, "Тебе нужно прислать цифры! Не нужно писать что-то лишнее в команду!")
            else: 
                lower_bound = int(lower_bound); upper_bound = int(upper_bound)
                if lower_bound > upper_bound: lower_bound, upper_bound = upper_bound, lower_bound 
                random_num = random.randint(lower_bound, upper_bound); bot.reply_to(message, f"Случайное число от {lower_bound} до {upper_bound} - {random_num}")
        elif sayori1.lower().startswith("закрепи это сообщение") or content.lower().startswith("прикрепи это сообщение"):
            if message.reply_to_message and check_admin_rights(chatId, userId):
                message_id = message.reply_to_message.message_id; bot.pin_chat_message(chatId, message_id); bot.reply_to(message, 'Сообщение успешно закреплено!')
            else:
                answer = "Для закрепления сообщения тебе нужно ответить на то сообщение, которое мне нужно прикрепить. Также возможность закреплять доступна лишь администраторам группы или чата."
                bot.reply_to(message, answer) ## Если пользователь не имеет админ.статуса или администратор не ответил на сообщение для закрепления - то мы разворачивает всех на 180 градусов
        elif sayori1.lower().startswith("перешли это сообщение") or sayori1.lower().startswith("отправь это сообщение"):
            if message.reply_to_message:
                original_message_id = message.reply_to_message.message_id; bot.send_message(chatId, "А теперь пришли мне ID пользователя: ")
                def ask_idofuser(reply_message):
                    getmyoid = reply_message.text.strip()
                    if not getmyoid.isdigit(): bot.send_message(chatId, "Тебе нужно прислать цифры! Не нужно писать что-то лишнее в команду!")
                    else:
                        try: bot.forward_message(chat_id=getmyoid, from_chat_id=chatId, message_id=original_message_id)
                        except telebot.apihelper.ApiException as e: bot.send_message(message.chat.id, f"Пользователь с ID {getmyoid} не существует. Убедитесь в правильности ввода уникального ID пользователя.")
                bot.register_next_step_handler(message, ask_idofuser)
        elif sayori1.lower().startswith(tuple(keyword9)): ## Вопрос, какое аниме может посоветовать Сайори пользователю
            reply = open('!replies/questionservice/aboutanime.txt', 'r', encoding='utf8') 
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif sayori1.lower().startswith(tuple(keyword12)): ## Попросить Сайори прислать совместимость между знаками зодиака
            bot.reply_to(message, str(random.choice(answ12)))  ## Сайори отвечает на запрос пользователя и присылает таблицу
            compatibility = open(("pictures/compatibility.png"), "rb"); bot.send_photo(chatId, compatibility)
        elif sayori1.lower().endswith('?'): bot.reply_to(message, str(random.choice(lis)))
        else: bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis12))) ## Если нету реакции - выдать "м?" и т.п

    ## Система отправки и регистрации предложений по улучшению Сайори (СОРПУС)
    if content.lower().startswith("/sorpus@sunnyddlc_bot "): sorpustext = message.text[22:]
    elif content.lower().startswith("!сорпус ") or content.lower().startswith("/sorpus "): sorpustext = message.text[8:]
    else: sorpustext = None
    if sorpustext is not None:
        with open("!replies/suggestionfillter/fooldetector.txt", "r", encoding="utf-8") as file:
            fooldetector = [word.strip() for word in file.readlines()]; words = sorpustext.split()
        is_banned_word = False ## флаг, обозначающий наличие запрещенных слов
        for word in words:
            if word.lower() in fooldetector:
                sorpustext = sorpustext.replace(word, "*" * len(word))
                bot.reply_to(message, "Ваш запрос содержит просьбу исправить что-то, для того что бы сообщить о баге и попросить исправить его - используйте команду /sorrew")
                is_banned_word = True ## устанавливаем флаг запретного слова
                break  ## прерываем цикл, так как уже нашли запрещенное слово
        with open("!replies/suggestionfillter/bannedwords.txt", "r", encoding="utf-8") as file:
            bannedwords = [word.strip() for word in file.readlines()]; words = sorpustext.split()
        is_bad_word = False ## флаг, обозначающий наличие запрещенных слов
        for word in words:
            if word.lower() in bannedwords:
                bot.reply_to(message, "Ваш запрос содержит запрещенные / оскорбительные слова, пожалуйста, используйте более безопасные слова для своего предложения.")
                is_bad_word = True ## устанавливаем флаг запретного слова
                break  ## прерываем цикл, так как уже нашли запрещенное слово
        if len(sorpustext) >= 400:
            bot.reply_to(message, "Ваш запрос содержит большое количество символов (400), пожалуйста, сократите ваш запрос или отправьте вашу идею по частям.")
        elif not is_banned_word and not is_bad_word:  # если запрещенных слов не было, можно записать идею в файл и отправить ответ
            suggestion_text = open("suggestions.txt", "a", encoding="utf-8") ## Открыть файл с предложениями
            sorpus = suggestion_text.write("• " + sorpustext) ## Записать предложение в файл
            suggestion_text.write("\n") ## Если данные есть - начать с новой строки
            suggestion_text.close() ## Закрыть файл с предложениями и идеями
            bot.reply_to(message, "Ваше предложение было записано и отправлено создателю, спасибо за ваши предложения! 💗")
            print(Fore.CYAN + "[", current_time, "]", Fore.WHITE, "Поступило предложение для обновления Сайори, подробнее в suggestions.txt")
            notification.notify( ## Создать оповещение системы
                title = 'Прошу немного внимания!', ## Заголовок уведомления
                message = 'Есть новое предложение для обновления!',
                app_icon = 'pictures/console.ico', ## Инонка для уведомления
                timeout = 3, ## Через сколько секунд пропадет уведомление
            )

    ## Система отправки и регистрации отзывов касаемо работы Сайори (СОРПКС)
    if content.lower().startswith("/sorrew@sunnyddlc_bot "): sorrewtext = message.text[22:]
    elif content.lower().startswith("!соррев ") or content.lower().startswith("/sorrew "): sorrewtext = message.text[8:]
    else: sorrewtext = None
    if sorrewtext is not None:
        with open("!replies/suggestionfillter/bannedwords.txt", "r", encoding="utf-8") as file:
            bannedwords = [word.strip() for word in file.readlines()]; words = sorrewtext.split()
        is_bad_word = False ## флаг, обозначающий наличие запрещенных слов
        for word in words:
            if word.lower() in bannedwords:
                bot.reply_to(message, "Ваш отзыв содержит запрещенные / оскорбительные слова, пожалуйста, используйте более безопасные слова для своего отзыва.")
                is_bad_word = True ## устанавливаем флаг запретного слова
                break  ## прерываем цикл, так как уже нашли запрещенное слово
        if len(sorrewtext) >= 400:
            bot.reply_to(message, "Ваш отзыв содержит большое количество символов (400), пожалуйста, сократите ваш отзыв или отправьте его по частям.")
        elif not is_bad_word:  # если запрещенных слов не было, можно записать идею в файл и отправить ответ
            suggestion_text = open("reviewsayori.txt", "a", encoding="utf-8") ## Открыть файл с предложениями
            sorrew = suggestion_text.write("• " + sorrewtext) ## Записать отзыв в файл
            suggestion_text.write("\n") ## Если данные есть - начать с новой строки
            suggestion_text.close() ## Закрыть файл с отзывами пользователя
            bot.reply_to(message, "Ваш отзыв был отправлен на компьютер создателя, спасибо за то, что вы делитесь опытом! 💗")
            print(Fore.CYAN + "[", current_time, "]", Fore.WHITE, "Поступил отзыв о работе Сайори, подробнее в recallsayori.txt")
            notification.notify( ## Создать оповещение системы
                title = 'Прошу немного внимания!', ## Заголовок уведомления
                message = 'Был получен отзыв от пользователя!',
                app_icon = 'pictures/console.ico', ## Инонка для уведомления
                timeout = 3, ## Через сколько секунд пропадет уведомление
            )
        
    ## Реакция Сайори на реплики пользователя, которые не относятся к какому либо блоку.
    if content.lower() in ['поздравления список', '!поздравления список', '!поздравления list']:
        reply = open('!replies/holidayslist.txt', 'r', encoding='utf8')
        answer = reply.read(); bot.send_message(chatId, answer, parse_mode="html"); reply.close()

    if content.lower().startswith("поздравь @"):
        words = message.text.split()
        if len(words) >= 4 and words[2].lower() == "с":
            author2 = words[1][0:]; holiday = " ".join(words[3:]) ## Убираем лишние символы
            if holiday in holidayssunny: 
                answer = random.choice(answ_birthday).replace("{author2}", author2)
                bot.send_message(message.chat.id, answer) ## Присылаем ответ из нашего списка
            elif holiday in dayofthemen:
                answer = random.choice(answ_dayofman).replace("{author2}", author2)
                bot.send_message(message.chat.id, answer) ## Присылаем ответ из нашего списка
            elif holiday in dayofvictory:
                answer = random.choice(answ_dayvictory).replace("{author2}", author2)
                bot.send_message(message.chat.id, answer) ## Присылаем ответ из нашего списка
            elif holiday in sevenmay:
                answer = random.choice(answ_7ofthemay).replace("{author2}", author2)
                bot.send_message(message.chat.id, answer) ## Присылаем ответ из нашего списка
            elif holiday in newyearholiday: 
                answer = random.choice(answ_newyear).replace("{author2}", author2)
                bot.send_message(message.chat.id, answer)
            elif holiday in eightmarch: 
                answer = random.choice(answ_8march).replace("{author2}", author2)
                bot.send_message(message.chat.id, answer)
            else: bot.send_message(message.chat.id, f"Поздравляю {author2} с {holiday}! 🎉")

    if content.lower().startswith("*обнял*") or content.lower().startswith("*обняла*"): ## Обнять Сайори (правильно!)
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis2)))

    if content.lower().startswith(tuple(keyword15)): ## Признаемся Сайори в любви (излюбленная фишка пользователей)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis8)))

    if content.lower().startswith(tuple(keyword16)): ## Приветствуем Сайори с помощью реплик
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis3)))

    if content.lower().startswith(tuple(keyword17)): ## Прощаемся с Сайори с помощью реплик
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis6)))

    if content.lower().startswith(tuple(keyword18)): ## Спрашиваем как дела у Сайори (Реакция будет лишь в личных сообщ.)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ3)))
            def ask_doings(message):
                context = message.text.strip()
                if any(keyword in context.lower() for keyword in keyword27):
                    time.sleep(3); bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ18))) ## Есои все нормально - отвечаем вот так.
                elif any(keyword in context.lower() for keyword in keyword28):
                    time.sleep(3); bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ19))) ## Есои все отлично - отвечаем вот так.
                elif any(keyword in context.lower() for keyword in keyword29):
                    time.sleep(3); bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ20))) ## Есои все плохо - отвечаем вот так.
            bot.register_next_step_handler(message, ask_doings)

    if content.lower().startswith(tuple(keyword19)): ## Спрашиваем что делает Сайори (Реакция будет лишь в личных сообщ.)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ4)))

    if content.lower().startswith(tuple(keyword20)): ## Спрашиваем является ли Сайори чат-ботом (Проверяем на личн.сообщ.)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ13)))

    if content.lower().startswith(tuple(keyword21)): ## Пользователь просит поздравить Сайори с достижением цели
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ14)))

    if content.lower().startswith(tuple(keyword22)): ## Пользователь спрашивает имя у Сайори (тупо, но задают вопрос)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(namequestion)))
        
    if content.lower().startswith(tuple(keyword23)): ## Пользователь спрашивает чем хочет заняться Сайори (ничем)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ15)))

    if content.lower().startswith(tuple(keyword24)): ## Пользователь спрашивает все ли в порядке с Сайори (активность)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ16)))

    if content.lower().startswith(tuple(keyword25)): ## Пользователь спрашивает не умерла ли Сайори (активна или нет)
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ17)))

    if content.lower().startswith(tuple(compliments)): ## Пользователь говорит комплименты в сторону чат-бота Сайори
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis11)))

    if content.lower().startswith(tuple(hatereaction)): ## Пользователь говорит гадости в сторону чат-бота Сайори
        if chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(answ7)))

    if content.lower() in ['я тут', 'я здесь', 'я вернулся', 'я вернулась']: ## Объявить о своем возвращении Сайори
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis7)))

    if content.lower().startswith(tuple(keyword3)): ## Сказать Сайори о своем плохом самочувствии (здоровье)
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ5)))

    if content.lower().startswith(tuple(keyword4)): ## Сказать Сайори о своем состоянии здоровья и выздоровлении
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ6)))

    if content.lower().startswith(tuple(strangereply)): ## Сказать Сайори нехорошие слова о себе (она не любит такое)
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(react3)))

    if content.lower().startswith(tuple(typicalphrase)): ## Типичные фразы со времен Амино или жизни (Дерево Чинжоу)
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(react4)))

    ## Реакция Сайори на реплики пользователя (Доброе утро и спокойной ночи)
    if content.lower() in ['доброе утро', 'всем доброго утра', 'всем доброе утро', 'всем утречка', 'утречка', 'доброе утро ☀']:
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis9)))

    if content.lower() in ['спокойной ночи', 'сладких снов', 'всем спокойной ночи', 'спокойной ночки', 'доброй ночи', 'спокойной ночи 🌑']:
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis10)))
        photo = open('pictures/SayoriSleep.jpg', 'rb'); bot.send_photo(chatId, photo)

    ## Блок №1.1. Устаревшие команды и дополнения к телу бота.
    ## Попросить прислать Сайори ссылки на сайт ДДЛК и википедию по игре (Фандом и оригинальная англ.)
    if content.lower().startswith(tuple(keyword)):
        reply = open('!replies/ddlcsitelist.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing")
        time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Попросить прислать Сайори саундтреки из визуальной новеллы (MP3 и YouTube)
    if content.lower().startswith("/track@sunnyddlc_bot"): nametrack = message.text[21:]
    elif content.lower().startswith("/track"): nametrack = message.text[7:]
    elif content.lower().startswith("!трек"): nametrack = message.text[6:]
    else: nametrack = None
    if nametrack is not None:
        if nametrack.lower() in ['список', 'list']:
            reply = open('!replies/soundlist.txt', 'r', encoding='utf8')
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif nametrack.lower() in ['1', 'doki doki literature club! (main theme)']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/BFSWlDpA6C4")
        elif nametrack.lower() in ['2', 'ohayou sayori!']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/BUWuDdfe7v4")  
        elif nametrack.lower() in ['3', 'dreams of love and literature']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/rsBeCQA93-Q")  
        elif nametrack.lower() in ['4', 'okay, everyone!']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/Hh2e9_bGSys")  
        elif nametrack.lower() in ['5', 'play with me']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/BUKN_ySpqU4")  
        elif nametrack.lower() in ['6', 'poem panic!']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/7JDlEpvE-cs")  
        elif nametrack.lower() in ['7', 'daijoubu!']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/FDG1AUN53S8")  
        elif nametrack.lower() in ['8', 'my feelings']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/IgRUaVHq1Hs")  
        elif nametrack.lower() in ['9', 'my confession']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/GAhiW1Z3GJY")  
        elif nametrack.lower() in ['10', 'sayo-nara']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/al1BNB8bKaE")  
        elif nametrack.lower() in ['11', 'just monika']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/JC0mFHN7r2c")  
        elif nametrack.lower() in ['12', 'i still love you']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/QIHUK68L9qQ")  
        elif nametrack.lower() in ['13', 'your reality']:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "https://youtu.be/CAL4WMpBNs0")  
        else:
            bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, "Что бы использовать данную команду введи цифру или название саундтрека, если ты не знаешь данные о нужной музыке - напиши /track список")  

    ## Попросить Сайори записать голосовые сообщения с помощью Google TTS
    if content.lower().startswith("/gs@sunnyddlc_bot"): voice_text = message.text[17:]
    elif content.lower().startswith("!гс") or content.lower().startswith("/gs"): voice_text = message.text[3:]
    else: voice_text = None
    if voice_text is not None:
        if len(voice_text) <= 4 or content.lower() == '/gs@sunnyddlc_bot':
            reply = open('!replies/errormessages/notextings.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing")
            time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif len(voice_text) >= 1000 or content.lower() == '/gs@sunnyddlc_bot':
            reply = open('!replies/errormessages/toolongtext.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing")
            time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        else:
            try:
                language = detect(voice_text)
                myobj = gTTS(text=voice_text, lang=language, slow=False);myobj.save("audio.mp3"); voice = open("audio.mp3", "rb")
                bot.send_chat_action(chatId, "record_audio"); time.sleep(3); bot.send_voice(chatId, voice)
            except Exception: bot.reply_to(message, "К сожалению я не могу озвучить сообщение на этом языке.")

    ## Блок 1.2. Действия и взаимодействия с участниками в группе.

    if content.lower().startswith("действия") or content.lower().startswith("/actions"):
        reply = open('!replies/actionlist.txt', 'r', encoding='utf8')
        answer = reply.read(); bot.reply_to(message, answer); reply.close()

    if content.lower().startswith("пощекотать @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, '...Аха-ха-ха...! П-перестань щекотать меня...!')
        try: tickle = open('gifanim/tickle.gif', 'rb'); bot.send_document(chatId, tickle)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("пощекотать @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} щекочет {author2}')
        try: tickle = open('gifanim/tickle.gif', 'rb'); bot.send_document(chatId, tickle)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("ударить @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Эй, ты чего дерешься то? Больно же... 😢')
    elif content.lower().startswith("ударить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} бьёт {author2}')
        try: punch = open('gifanim/punch.gif', 'rb'); bot.send_document(chatId, punch)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("тыкнуть @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Эй, не нужно в меня тыкать!')
        try: poke = open('gifanim/poke.gif', 'rb'); bot.send_document(chatId, poke)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("тыкнуть @"):    
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} тыкает в {author2}')
        try: poke = open('gifanim/poke.gif', 'rb'); bot.send_document(chatId, poke)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("погладить @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Няяяяяя, люблю когда меня гладят!~')
        try: pat = open('gifanim/pat.gif', 'rb'); bot.send_document(chatId, pat)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("погладить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} гладит {author2}')
        try: pat = open('gifanim/pat.gif', 'rb'); bot.send_document(chatId, pat)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("обнять @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Урааааа, обнимашкииии!~ 🥰')
        try: hug = open('gifanim/hug.gif', 'rb'); bot.send_document(chatId, hug)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("обнять @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} обнимает {author2}')
        try: hug = open('gifanim/hug.gif', 'rb'); bot.send_document(chatId, hug)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("покормить @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Ням-ням, но я же бот, я могу не есть. :>')
        try: feed = open('gifanim/feed.gif', 'rb'); bot.send_document(chatId, feed)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("покормить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} кормит {author2}')
        try: feed = open('gifanim/feed.gif', 'rb'); bot.send_document(chatId, feed)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("прижаться @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'О-оо-ооо? Это было довольно неожиданно. ❤')
        try: hug = open('gifanim/hug.gif', 'rb'); bot.send_document(chatId, hug)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("прижаться @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} прижимается к {author2}')
        try: hug = open('gifanim/hug.gif', 'rb'); bot.send_document(chatId, hug)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("поцеловать @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Эхе-хе-хех... Это было очень неожиданно. 😳')
        try: kiss = open('gifanim/kiss.gif', 'rb'); bot.send_document(chatId, kiss)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')
    elif content.lower().startswith("поцеловать @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} целует {author2}')
        try: kiss = open('gifanim/kiss.gif', 'rb'); bot.send_document(chatId, kiss)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    if content.lower().startswith("укусить @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Ай-ай-ай...! Чего же ты кусаешься? Больно! 💢')
    elif content.lower().startswith("укусить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} делает кусь {author2}')
        try: bite = open('gifanim/bite.gif', 'rb'); bot.send_document(chatId, bite)
        except Exception: bot.reply_to(message, 'Я не смогла отправить GIF анимацию, может быть вы запретили ее отправку в группе?')

    ## Блок №2. Мини-игры и развлечения. (Всего игр - 4)
    if content.lower().startswith("!игра"): gamequest = message.text[6:]
    elif content.lower().startswith("/game") and chatName == firstname + " (ЛС)": gamequest = message.text[6:]
    elif content.lower().startswith("/game@sunnyddlc_bot"): gamequest = message.text[20:]
    else: gamequest = None
    if gamequest is not None:
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        ## Мини-игра №1 (Счастливый билетик - выдается шестизначный билетик, в нем должны попасться одинаковые цифры)
        if gamequest.lower().startswith("счастливый билетик") or gamequest.lower().startswith("1"):
            bot.send_message(chatId, "Я запускаю первую мини-игру, пожалуйста подождите...")
            time.sleep(1.5); ticketgot = str(sixnumber(6))
            bot.send_message(chatId, "Итак, твой билетик с номером: "+ticketgot); time.sleep(1.5)
            if any(x in ticketgot for x in luckynumber):
                bot.reply_to(message, "Поздравляю тебя с победой! В твоем билетике оказались две одинаковые цифры! Я всегда в тебя верю.~ 💗")
            else: bot.reply_to(message, "Ой-ой, к сожалению в твоем билетике не оказалось две одинаковых цифр, может тебе повезет в следующий раз? 😌")
        ## Мини-игра №2 (Камень, ножницы, бумага - классическая игра, в пояснениях не нуждается)
        elif gamequest.lower().startswith('2'):
            if len(gamequest.lower().split()) > 1:
                player_choice = gamequest.lower().split()[1] # Получаем выбор игрока (что он выбрал)
                if player_choice in ['камень', 'ножницы', 'бумага']: rock_paper_scissors(bot, message, player_choice)
                else: bot.reply_to(message, "Я не поняла тебя, что ты имел ввиду? Перефразируй или напиши корректно.")
            else: bot.reply_to(message, "Ты не добавил после данной команды свое действие (Камень, ножницы или бумагу). Попробуй еще раз!")
        ## Мини-игра №3 (Угадайка - Сайори выбирает числа, а пользователю нужно угадывать, звучит просто)
        elif gamequest.lower().startswith('3'):
            def ask_userselect(message, is_game_active):
                text = message.text.lower()
                if text == 'легкий 🟢':
                    bot.send_message(chatId, "Вы выбрали легкий режим.", reply_markup=types.ReplyKeyboardRemove())
                    ask_iscorrectnumber = play_easy(bot, chatId, is_game_active)
                    bot.register_next_step_handler(message, ask_iscorrectnumber)
                elif text == 'средний 🟡':
                    bot.send_message(chatId, "Ты выбрал средний режим.", reply_markup=types.ReplyKeyboardRemove())
                    ask_iscorrectnumbernormal = play_normal(bot, chatId, is_game_active)
                    bot.register_next_step_handler(message, ask_iscorrectnumbernormal)
                elif text == 'сложный 🔴':
                    bot.send_message(chatId, "Ты выбрал сложный режим.", reply_markup=types.ReplyKeyboardRemove())
                    ask_iscorrectnumberhard = play_hard(bot, chatId, is_game_active)
                    bot.register_next_step_handler(message, ask_iscorrectnumberhard)
            is_game_active = False
            bot.send_message(chatId, "Выбери уровень сложности.", reply_markup=difficulty)
            bot.register_next_step_handler(message, lambda msg: ask_userselect(msg, is_game_active))
        elif gamequest.lower().startswith("список") or gamequest.lower().startswith("list"):
            reply = open('!replies/gamelist.txt', 'r', encoding='utf8'); answer = reply.read(); bot.reply_to(message, answer, parse_mode="html"); reply.close()
        else: reply = open('!replies/wronggame.txt', 'r', encoding='utf8'); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Блок №3. Административные и отладочные команды
    ## Функция, позволяющая Сайори выйти из определенной группы / чата с помощью chatID
    if content.lower().startswith("!leave") or content.lower().startswith("/leave"):
        if username == "ElliotMoxiess":
            chats_id = input("Введите ID чата из которой мне нужно выйти: ")
            try: bot.leave_chat(chats_id); print(f"Бот успешно покинул группу с chatId: {chats_id}")
            except Exception as e: print(f"Ошибка при покидании группы с chat_id {chats_id}: {e}")
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Дистанционная очистка лог-файла (txt) с помощью команды.
    if content.lower().startswith("!очисткалогов") or content.lower().startswith("/cll"):
        if username == "ElliotMoxiess":
            bot.send_chat_action(chatId, "typing"); time.sleep(3); open("log.txt", "w").close(); print("Логи были успешно очищены.")
            bot.reply_to(message, 'Я успешно выполнила данную команду! Код ее выполнения: S0cl00, больше сведений находится в файле log.txt!')
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')

    ## Дистанционная очистка терминала бота с помощью команды.
    if content.lower().startswith("!очиститьтерминал") or content.lower().startswith("/cls"):
        bot.send_chat_action(chatId, "typing")
        if username == "ElliotMoxiess":
            time.sleep(3); os.system('cls'); print("Терминал был успешно очищен.")
            bot.reply_to(message, 'Я успешно выполнила данную команду! Код ее выполнения: S0ct00, больше сведений находится в файле log.txt!')
            logger.warning('Была запрошена очистка терминала бота, команда выполнена успешно. Код выполнения операции: S0ct00')
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')

    ## Дистанционная очистка предложений (suggestions.txt) с помощью команды.
    if content.lower().startswith("!очиститьидеи") or content.lower().startswith("/cli"):
        if username == "ElliotMoxiess":
            bot.send_chat_action(chatId, "typing"); time.sleep(3); open("suggestions.txt", "w").close(); print("Предложения был успешно очищены.")
            bot.reply_to(message, 'Я успешно выполнила данную команду! Код ее выполнения: S0ci00, больше сведений находится в файле log.txt!')
            logger.warning('Была запрошена очистка предложений бота, команда выполнена успешно. Код выполнения операции: S0ci00')
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')

    ## Дистанционная перезагрузка / обновление Сайори с помощью команды.
    if content.lower().startswith("!перезагрузка") or content.lower().startswith("/restart"):
        if username == "ElliotMoxiess":
            bot.reply_to(message, "Инициализирована команда перезагрузки кода, пожалуйста ожидайте выполнения операции... ☀")
            process = subprocess.Popen('SayoriBotT', shell=True); bot.stop_polling(); process.wait()
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Дистанционное зачитывание данных с файла (log.txt) для просмотра логов и ошибок.
    if content.lower().startswith("!чтениелогов") or content.lower().startswith("/logreader"):
        if username == "ElliotMoxiess":
            bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('log.txt', 'r', encoding='Windows-1251'); answer = reply.read(); bot.reply_to(message, answer)
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Дистанционное зачитывание данных с файла (suggestions.txt) для просмотра идей.
    if content.lower().startswith("!чтениеидей") or content.lower().startswith("/ideareader"):
        if username == "ElliotMoxiess":
            bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('suggestions.txt', 'r', encoding='Windows-1251'); answer = reply.read(); bot.reply_to(message, answer)
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Дистанционное зачитывание данных с файла (reviewsayori.txt) для просмотра отзывов.
    if content.lower().startswith("!чтениеотзывов") or content.lower().startswith("/reviewreader"):
        if username == "ElliotMoxiess":
            bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('reviewsayori.txt', 'r', encoding='Windows-1251'); answer = reply.read(); bot.reply_to(message, answer)
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Дистанционная отправка сообщений от лица чат-бота Сайори (ручной метод ввода данных)
    if content.lower().startswith("!сайоринапиши") or content.lower().startswith("/sayoriwrite"):
        if username == "ElliotMoxiess":
            chatus_id = input("Введите уникальный ID чата для отправки: "); soderzhus = input("Введите текст сообщения для отправки: ")
            bot.send_chat_action(chatus_id, "typing"); time.sleep(3); bot.send_message(chatus_id, f"{soderzhus}")
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!') 

    ## Удаление последний 10 сообщений в чатах / группах / каналах с помощью команды.
    if content.lower().startswith("!очистка10") or content.lower().startswith("/clean10"):
        if check_admin_rights(chatId, userId):
            last_message_id = message.message_id
            try:
                for i in range(10): time.sleep(1); bot.delete_message(message.chat.id, last_message_id); last_message_id -= 1
                bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(message.chat.id, 'Последние 10 сообщений были успешно удалены.')
            except Exception: reply = open('!replies/errormessages/cantremove.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_message(chatId, answer); reply.close()
        elif chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            last_message_id = message.message_id
            try:
                for i in range(10): time.sleep(1); bot.delete_message(message.chat.id, last_message_id); last_message_id -= 1
                bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(message.chat.id, 'Последние 10 сообщений были успешно удалены.')
            except Exception: reply = open('!replies/errormessages/cantremove.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_message(chatId, answer); reply.close()
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Удаление последний 50 сообщений в чатах / группах / каналах с помощью команды.
    if content.lower().startswith("!очистка50") or content.lower().startswith("/clean50"):
        if check_admin_rights(chatId, userId):
            last_message_id = message.message_id
            try:
                for i in range(50): time.sleep(1); bot.delete_message(message.chat.id, last_message_id); last_message_id -= 1
                bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(message.chat.id, 'Последние 50 сообщений были успешно удалены.')
            except Exception: reply = open('!replies/errormessages/cantremove.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_message(chatId, answer); reply.close()
        elif chatName == firstname + " (ЛС)": ## Проверяем, пишет ли пользователь в личные сообщения Сайори или же нет
            last_message_id = message.message_id
            try:
                for i in range(50): time.sleep(1); bot.delete_message(message.chat.id, last_message_id); last_message_id -= 1
                bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(message.chat.id, 'Последние 50 сообщений были успешно удалены.')
            except Exception: reply = open('!replies/errormessages/cantremove.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_message(chatId, answer); reply.close()
        else: bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку если ты есть есть в списке админов!')  

    ## Блок №4. Система обнаружения ошибок внутри кода Сайори (СООВКС)
    ## Проверяем, запущен ли файл напрямую, в случае успеха - бот начинает работу
if __name__ == '__main__': ## Проверка того, был ли запущен файл напрямую
    try:
        bot.polling(none_stop=True, interval=0, timeout=1024) ## Просматривать чаты и получать новые запросы бесконечно
        bot.notifyOnMessage() ## При получении новых запросов и сообщений в чатах - проверять содержимое пакета
    except Exception as error: 
        print(f"{type(error).__name__}: Причина остановки: {error}, выполняется перезагрузка.")
        notification.notify( ## Создать оповещение системы
            title = 'Произошла ошибка в коде 🚨', ## Заголовок уведомления
            message = 'Все детали находятся в терминале, выполняется перезагрузка.',
            app_icon = 'pictures/console.ico', ## Инонка для уведомления
            timeout = 3, ## Через сколько секунд пропадет уведомление
        )
        logger.error(f'Произошла ошибка: {type(error).__name__}: {error}')
        time.sleep(15); process = subprocess.Popen('SayoriBotT', shell=True); os.system('cls'); bot.stop_polling(); process.wait()

