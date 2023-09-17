import json; import telebot; from telebot import types

## Блок №0. Создание кнопок для взаимодействия с пользователем в личных сообщениях.

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Сайори 🎀', callback_data='о сайори')) ## Сайори
keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Юри 📖', callback_data='о юри')) ## Юричк (Yuri)
keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Монике 🖍', callback_data='о монике')) ## Моника
keyboard.add(telebot.types.InlineKeyboardButton('Узнать о Нацуки 🧁', callback_data='о нацуки')) ## Нацуки

mainmenu = types.KeyboardButton("В главное меню 🏠") ## Создаем кнопки для главного меню и не только
btnh = types.KeyboardButton("📝 Команды"); btne = types.KeyboardButton("👤 Добавление чат-бота")
btn1 = types.KeyboardButton("Взаимодействия с ботом"); btn2 = types.KeyboardButton("🕹 Все мини-игры"); btn3 = types.KeyboardButton("Взаимодействия с участниками")
btn4 = types.KeyboardButton("Технические команды"); btn5 = types.KeyboardButton("Полезные ссылки"); btn6 = types.KeyboardButton("Доброе утро ☀"); btn7 = types.KeyboardButton("Спокойной ночи 🌑")
btn9 = types.KeyboardButton("🔁 История обновлений"); btn10 = types.KeyboardButton("☎ Статус чат-бота"); btn11 = types.KeyboardButton("🦺 Административные команды"); markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=False)
markup.row(btnh, btne); markup.row(btn1); markup.row(btn2); markup.row(btn3); markup.row(btn4, btn5); markup.row(btn6, btn7); markup.row( btn9, btn10); markup.row(btn11)

s_1 = types.KeyboardButton("Сайори, привет"); s_2 = types.KeyboardButton("Сайори, как дела?"); s_3 = types.KeyboardButton("Сайори, что делаешь?")
s_4 = types.KeyboardButton("Сайори, расскажи шутку 📕"); s_5 = types.KeyboardButton("Сайори, повтори за мной 🔁"); s_6 = types.KeyboardButton("Сайори, поздравь меня 🎉")
s_7 = types.KeyboardButton("Сайори, пришли фанарт 🎨"); s_8 = types.KeyboardButton("Сайори, пришли катсцену 🖼"); s_9 = types.KeyboardButton("Сайори, мне нужна помощь")
s_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=False); s_markup.row(mainmenu); s_markup.row(s_1, s_2, s_3); s_markup.row(s_4, s_5, s_6); s_markup.row(s_7, s_8); s_markup.row(s_9)

b_hug = types.KeyboardButton("Обнять"); b_rob = types.KeyboardButton("Ограбить"); b_pat = types.KeyboardButton("Погладить"); b_huddle = types.KeyboardButton("Прижаться")
b_feed = types.KeyboardButton("Покормить"); b_bite = types.KeyboardButton("Укусить"); b_punch = types.KeyboardButton("Ударить"); b_poke = types.KeyboardButton("Тыкнуть")
b_kiss = types.KeyboardButton("Поцеловать"); b_tickle = types.KeyboardButton("Пощекотать"); b_waving = types.KeyboardButton("Поприветствовать"); a_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=False)
a_markup.row(mainmenu); a_markup.row(b_kiss, b_hug, b_huddle); a_markup.row(b_waving, b_rob); a_markup.row(b_punch, b_bite, b_poke); a_markup.row(b_tickle, b_feed, b_pat)

helpbut1 = types.KeyboardButton("< Первая страница"); helpbut2 = types.KeyboardButton("Вторая страница >"); helpbut3 = types.KeyboardButton("Третья страница >"); helpbut4 = types.KeyboardButton("Вторая страница <")
helpmark = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True); helpmark.row(mainmenu, helpbut2); page2mark = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True); page2mark.row(helpbut1, mainmenu , helpbut3)
page3mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True); page3mark.row(helpbut4, mainmenu)
    
originalost = types.KeyboardButton("Оригинальная игра"); fallenangel = types.KeyboardButton("Мод: Fallen Angel (New!)"); ostlists = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True); ostlists.row(originalost, fallenangel)
btneasy = types.KeyboardButton("Легкий 🟢"); btnnormal = types.KeyboardButton("Средний 🟡"); btnhard = types.KeyboardButton("Сложный 🔴"); difficulty = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True); difficulty.row(btneasy, btnnormal, btnhard)

examplebut1 = types.KeyboardButton("Первая страница1️⃣"); examplebut2 = types.KeyboardButton("Вторая страница 2️⃣"); examplebut3 = types.KeyboardButton("Третья страница 3️⃣")
examplemark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True); examplemark.row(mainmenu, examplebut2); example2mark = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
example2mark.row(examplebut1, mainmenu, examplebut3); example3mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True); example3mark.row(examplebut2, mainmenu)

## Списки с ответами Сайори, которые та выдает в ответ на запрограммированые реакции и сообщения
with open('!replies/listreplies.json', 'r', encoding='utf-8') as f: ## Открытие json файла с репликами
    data = json.load(f) ## Подгружаем данные с нашего json файла со списками для Сайори (списки проще говоря)

item_lists = data['items_lists']

lis = data['lis']; lis2 = data['lis2']; lis3 = data['lis3']; lis5 = data['lis5']; lis6 = data['lis6'] ## Списки с репликами Сайори под №1
lis7 = data['lis7']; lis8 = data['lis8']; lis9 = data['lis9']; lis10 = data['lis10']; lis11 = data['lis11']; lis12 = data['lis12']; lis13 = data['lis13']

answ1 = data['answ1']; answ2 = data['answ2']; answ3 = data['answ3']; answ4 = data['answ4']; answ5 = data['answ5']; answ6 = data['answ6']; bannedlinks = data['bannedlinks']
answ7 = data['answ7']; answ8 = data['answ8']; answ9 = data['answ9']; answ10 = data['answ10']; answ11 = data['answ11']; answ12 = data['answ12']; answ13 = data['answ13']; answ14 = data['answ14']
answ15 = data['answ15']; answ16 = data['answ16']; answ17 = data['answ17']; answ18 = data['answ18']; answ19 = data['answ19']; answ20 = data['answ20']; answ21 = data['answ21']; answ22 = data['answ22']
answ23 = data['answ23']

react1 = data['react1']; react3 = data['react3']; react4 = data['react4']
keyword = data['keyword']; keyword2 = data['keyword2'];keyword3 = data['keyword3']; keyword4 = data['keyword4']
keyword5 = data['keyword5']; keyword7 = data['keyword7']; keyword8 = data['keyword8']; keyword9 = data['keyword9']; keyword10 = data['keyword10']; keyword11 = data['keyword11']
keyword12 = data['keyword12']; keyword13 = data['keyword13']; keyword14 = data['keyword14']; keyword15 = data['keyword15']; keyword16 = data['keyword16']; keyword17 = data['keyword17']
keyword18 = data['keyword18']; keyword19 = data['keyword19']; keyword20 = data['keyword20']; keyword21 = data['keyword21']; keyword22 = data['keyword22']; keyword23 = data['keyword23']
keyword24 = data['keyword24']; keyword25 = data['keyword25']; keyword26 = data['keyword26']; keyword27 = data['keyword27']; keyword28 = data['keyword28']; keyword29 = data['keyword29']

hatereaction = data['hatereaction']; typicalphrase = data['typicalphrase']; compliments = data['compliments']; strangereply = data['strangereply']; strangequestions = data['strangequestions']; namequestion = data['namequestion']
aboutsunny = data['aboutsunny']; aboutyuri = data['aboutyuri']; aboutmonika = data['aboutmonika']; aboutnatsuki = data['aboutnatsuki']; possible_actions = data['possible_actions']; luckynumber = data['luckynumber']
funnyjokes = data['funnyjokes']; holidayssunny = data['holidayssunny']; dayofvictory = data['dayofvictory']; newyearholiday = data['newyearholiday']; dayofthemen = data['dayofthemen']; sevenmay = data['sevenmay']; eightmarch = data['eightmarch']
answ_birthday = data['answ_birthday']; answ_7ofthemay = data['answ_7ofthemay']; answ_dayofman = data['answ_dayofman']; answ_newyear = data['answ_newyear']; answ_dayvictory = data['answ_dayvictory']; answ_8march = data['answ_8march']