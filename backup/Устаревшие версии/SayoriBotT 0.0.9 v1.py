
import re; import os; import sys
import time; import random; import telebot; import threading
import logging; import datetime; import colorama; import subprocess

from colorama import Fore, Back, Style; from randomfile import pwd
from re import search; from gtts import gTTS; from random import randint
from threading import Timer; from os.path import abspath; from datetime import datetime
from plyer import notification; from googletrans import Translator; from os import scandir, getcwd, execl
from numbersrand import sixnumber; from monthdate import russiandate; from rockpapers import rock_paper_scissors

## Вход в аккаунт чат-бота и активация заданных параметров запуска.
logger = logging.getLogger(__name__); colorama.init() ## Включение библиотеки Colorama
bot = telebot.TeleBot('5568779412:AAFbQBM0RNZtWGGHYDWtWea8ZGwpugOT1lU', skip_pending=True) ## Токен и пропуск старых сообщений
logging.basicConfig(filename="log.txt", format='[%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S]', level=logging.INFO)

## Начальное сообщение о включении бота и его текущее состояние
print("\nИдентификация, выполняется вход в аккаунт чат-бота Telegram: ", Fore.CYAN + "— Сᴀйᴏᴘᴜ • ;")
print(Fore.WHITE + "Краткий справочник по командам: /help - список всех команд, !cls - очистить терминал бота.")
print("Сайори (Telegram) была создана Moxiess, ее цели - помощь администрации и общение с участниками!")
time.sleep(1); print(Fore.LIGHTYELLOW_EX + "\nБот запущен на версии 0.0.9 Обновление №1, активирование функции логгирования чатов...", Fore.CYAN + "OK")
time.sleep(1); print(Fore.WHITE+ " ‖ Это начало истории с чатов и групп, что бы очистить историю - используйте команду - /clt\n")

## Списки с ответами Сайори, которые та выдает в ответ на запрограммированые реакции и сообщения

lis = ['Наверное', 'Точно нет', 'Да, я уверена', 'Скорее всего да, а хотя, может и нет...', 'Возможно...~', 'Вероятнее всего', 'Не исключено', 
    'Я не знаю ответа на этот вопрос.', 'Почему ты так думаешь?', 'Я не уверена что тебе стоит знать ответ на твой вопрос... Эхе-хе-хе.~','Нет','Да']

lis2 = ['*Обняла в ответ* Мне приятно что ты заботишься о мне~', 'Ня~ Как приятно~', '*Обняла в ответ* Не отпускай меня...~',
    '*Обняла в ответ* Можно нам так стоять вместе вечно?..', '*Обняла в ответ* Я люблю тебя... Обещай что не заставишь меня грустить, ладно? :<', '*Обняла в ответ* :3', '*Обняла в ответ* Я счастлива~']

lis3 = ['Привет-привет!', "Охайо!", "Привет, солнышко!", "Мур-Мур~", "Я тоже рада тебя видеть, приветики!", "Здравствуй, хи-хи-хи.", "Приветики :>", "Кого я вижу! Наш любимый и дорогой участник!", "Ох, привет!"]

lis5 = ["Кто-то знает еще одно мое имя? :0", "Что-то случилось?", "Да-да, это я. :>", "Не часто меня так называют, но спасибо. :>", "Кто-то упомянул меня?", "Я внимательно вас слушаю. :>"]

lis6 = ["Оу, ты уже уходишь? Я буду скучать... *Обняла на прощание*", "Уже уходишь...? *Поцеловала в лобик* Я буду тебя ждать, приходи поскорее... :<", "Тебе уже пора? Если так, то я буду тебя ждать, эхе-хе-хе...~"]

lis7 = ["Ура! Наконец-то ты вернулся! Я очень соскучилась! Давай общаться! *Обняла с легкой улыбкой*", "Я рада тебя видеть, привет! *Сделала легкую улыбку*", "Здравствуй снова, я рада тебя видеть!",
      "Мне было очень скучно, я безумно рада видеть тебя, давай пообщаемся? *Обняла с легкой улыбкой*"]

lis8 = ["*Покраснела* Эхе-хе-хе...", "А...А...? Я-я т-тоже люблю тебя...~", "С-спасибо, взаимно. 💗", "😍", "Ты не шутишь...?~", "*Очень сильно покраснела и прикрыла лицо своей рукой*",
     "Я люблю тебя тоже. 💗", "Я... Так рада это слышать, вместе мы замечательно проведем время!", "Очень... приятно это слышать. 🥰"]

lis9 = ["Доброе утро, мои любимые участники!", "*Потирая сонные глазки* В-всем приветики, соскучились по мне?~", "Утречка!", "Я рада всех видеть!", "Утро настало.~",
     "Что я пропустила? Ах да, доброе утро!", "*Зевая* Я рада всех вас видеть, приветики!", "Новый день начинается, ура-ура-ура!"]

lis10 = ["*Зевая* Спокойной ночи, мои любимые участники.~", "*Зевая* Спокойной ночи сладкие мои.~", "Что-то я тоже устала, пожалуй и мне пора бы поспать...",
     "Уже все расходятся? Досадно, давайте высыпайтесь, я буду вас ждать!", "Люди хотят спать, роботы тоже могут хотеть, эхе-хе-хе."]

lis11 = ['Ой, спасибо за твой комплимент...~', 'Эхе-хе-хе, тоже самое могу сказать и о тебе...~', 'Ваушки! Комплимент! *Немного покраснела и улыбнулась*',
     'Я всегда стараюсь быть хорошей, спасибо за оценку...~ 🥰', 'Так приятно слышать это.~', 'Я думаю тоже самое и к тебе подходит, спасибо тебе! 💗']

lis12 = ['?', 'Кто-то меня звал?', 'Я вся во внимании.', 'М?', 'Слушаю и повинуюсь.', 'Я здесь! Слушаю.~']

## Ответы Сайори на какие-либо запрограммированые реплики в коде

answ1 = ['Каждому найдется место в моем сердечке, без исключений! 💗', 'Конечно я тебя люблю, эхе-хе-хе.~', 'Ты сомневаешься в том, что люблю я тебя или нет? :<',
    'Все мои любымые, никто не будет исключением, даже ты. :>', 'Конечно!', 'Я несу радость и позитив всем, ты не станешь исключением! *Улыбнулась*',
    'Что за глупый вопрос, конечно же я люблю тебя. :>', 'Можно было не задавать этот вопрос, мой ответ короток и ясен - да. 🥰']

answ2 = ['Эхе-хе-хе... Слишком неловкий и неуместный вопрос... 😳']

answ3 = ['Как таковых дел у меня нету, поэтому - никак. А как у тебя дела?', 'У меня все отлично, общаюсь с тобой. А что на счет тебя?',
     'Все просто замечательно, надеюсь у тебя тоже все хорошо?', 'У меня все отлично, что на счет тебя? 🧐', 'Все отлично, слушаю, общаюсь, мониторю чаты и так далее. Что на счет тебя?']

answ4 = ['Чем я занимаюсь? Вопрос хороший, в основном сейчас я мониторю чаты, передаю различную информацию создателю на компьютер, общаюсь с тобой и другими участниками и так далее.~',
     'Выполняю свою задачу и цель, с которой я была создана. Что на счет тебя?', 'Сейчас я выполняю много задач, например провожу мониторинг чатов и прочее.)',
     'Как обычно - мониторинг и не только, общение и так далее. Надеюсь у тебя занятия получше?']

answ5 = ['Выпей таблеточку, пожалуйста.', 'Полежи и отдохни, может быть поможет?', 'Не люблю когда у кого-то что-то болит, выпей таблеточку или скажи об этом родителям, они лучше знают что выпить. 😌',
     'Лучше с этим не затягивать и принять меры... Если станет плохо, то лучше вызови скорую или попроси родителей помочь разобраться с болью. 😞']

answ6 = ['Выздоравливай поскрее, не люблю когда кто-то болеет. 😞', 'Выздоравливай, надеюсь ты поскорее встанешь на ноги и снова будет заряжен энергией!',
     'Болезнь - вещь такая, но я уверена что все будет хорошо и ты поскорее поправишься.~']

answ7 = ['Ну и ладно, ябка. :<', 'Ну и ладненько, я все равно буду любить тебя, эхе-хе-хе.~', 'Меня это ни сколько не задело, эхе-хе-хе. :>', 'Ладненько, уверена ты поменяешь свое мнение в будущем.~']

answ8 = ['Все в порядке, не переживай. 😌', 'Я в порядке. Можешь не переживать за меня.~', 'Обычно грустной себя ощущала именно Сайори, я же сама радость и солнышко, эхе-хе-хе...!~ 💗']

answ9 = ['Эхе-хе-хе... Я даже не знаю как ответить на этот вопрос... Это... 😲', 'Ха-ха-ха, я надеюсь ты шутишь, да...?', 'П-пожалуйста скажи что ты шутишь, ладно? 😨', 'Ну... Эм... Я не знаю...']

answ10 = ['У меня все очень хорошо, что на счет тебя? 🥰', 'Я чувствую себя очень радостной и позитивной, все как обычно! Надеюсь, что ты испытываешь такие же чувства при общении со мной.~',
     'Меня переполняет радость и любовь ко всем и ко всему, что на счет тебя? 💗', 'Не смотря на возможные баги и прочее - я чувствую себя очень радостной и счастливой! Хи-хи-хи.~']

answ11 = ['Нет, я не сплю.', 'Нет, я не сплю, слушаю тебя, солнышко!~', 'Нет, а что такое?', 'Я конечно иногда сплю, но в данный момент не совсем, слушаю тебя, хи-хи-хи.~']

answ12 = ['Ого, я смотрю тебе эта тема довольно интересна, к счастью у меня есть подробная таблица с совместимыми знаками зодиака! Многие правда не верят в нее, но тем не менее... 👉👈']

## Реакции Сайори на какие-либо запрограммированые реплики пользователя

react1 = ['У тебя какие-то проблемы? Если так - то все можно пройти, в мире нету ничего возможно, все можно сделать - через все можно пройти!', 'Я уверена что все будет хорошо у тебя, будь более счастливее!',
     'Я люблю всех участников, видь во всем позитив! Если у тебя произошло что-то плохое, то не спеши расстраиваться и искать в этом минус, это все могут быть мелочи жизни.~', 'У тебя все обязательно получится!'
     'Все будет хорошо, просто постарайся много не думать о произошедшем. Выпей чаю, подыши воздухом и тебе станет легче, а мне будет спокойнее за тебя. 😌', 'Отдохни немного, все будет хорошо!~ 💗']

react3 = ['Нееет! Это не так!', 'Не правда! Ты хороший! 💗', 'Нет-нет, не говори так... :<', 'Не правда, не нужно так про себя говорить.~', 'Не верю, ты заблужаешься в себе.', 'Не говори так, это не правда!']

react4 = ['Я слышала эти фразы много раз, люблю их. :>', 'Ммммм... Знакомая для меня фраза.', 'Аха-ха-ха, хоть и слышала эту фразу - но она мне очень сильно нравится.~', 'Забавно :>']

## Возможные фразы пользователя, при которых Сайори будет выдавать различные реакции

keyword = ['официальный сайт ддлк', 'офф.сайт ддлк', 'официальный сайт ddlc', 'сайт ddlc', 'сайт ддлк', 'сайт создателей игры', 'сайт игры ddlc']

keyword2 = ['твои мысли о ', 'что ты думаешь о ', 'какого мнения ты о ', 'твое отношение к ', 'твое мнение о ', 'как ты относишься к ', 'что думаешь на счет ']

keyword3 = ['я чувствую себя плохо', 'мне плохо', 'мне нездоровится', 'чувствую себя слабым', 'чувствую слабость', 'чувствую боль', 'у меня что то болит', 'у меня болит голова']

keyword4 = ['я заболела', 'я болею', 'я заболел', 'я лежу в больнице', 'я лечусь']

keyword5 = ['какое твое отношение к зиме', 'какое твое отношение к зимней погоде', 'что ты думаешь о снежной погоде', 'что ты думаешь о зиме', 'какое твое отношение к зиме']

keyword7 = ['ты хочешь нашей смерти', 'ты хочешь убить нас', 'ты хочешь что бы мы умерли', 'ты хочешь что бы мы перестали существовать', 'ты желаешь нашей смерти']

keyword8 = ['ты шаришь в мемах', 'шаришь за мемы', 'ты разбираешься в мемах', 'ты разбираешься в приколах?', 'ты шаришь за мемы', 'ты шаришь за мем ']

keyword9 = ['какое аниме порекомендуешь', 'какое аниме посоветуешь', 'какое аниме мне стоит посмотреть', 'какое посмотреть аниме', 'твои любимые аниме', 
     'посоветуй аниме', 'какое аниме посоветуешь посмотреть', 'посоветуешь мне аниме', 'что из тайтлов мне стоит посмотреть', 'твое любимое аниме']

keyword10 = ['какое у тебя настроение', 'как твое настроение', 'как у тебя с настроением', 'что у тебя с настроением', 'как ты себя чувствуешь']

keyword11 = ['мне нужна помощь', 'мне нужна твоя поддержка', 'мне нужна поддержка', 'мне нужна моральная поддержка', 'мне нужно твое наставление',
     'мне нужен твой совет', 'мне нужно наставление', 'мне нужен совет', 'я хочу совет', 'я хочу поддержку', 'я хочу моральную поддержку']

keyword12 = ['пришли совместимость зз', 'совместимость знаков зодиака', 'пришли совместимость знаков зодиака', 'какова совместимость знаков зз']

keyword13 = ['ты спишь', 'ты дрыхнешь', 'ты дремаешь', 'ты заснула', 'не спи', 'не дремай', 'не дрыхни']

keyword14 = ['расскажи анекдот', 'пошути', 'расскажи шутку', 'поделись анекдотом', 'валяй анекдот', 'валяй шутку', 'поделись шуткой']

hatereaction = ['я тебя ненавижу', 'я не люблю тебя', 'я ненавижу тебя', 'я тебя не люблю', 'ты мне не нравишься']

typicalphrase = ['барбара это бебра', 'бебра', 'барбара бебра', 'посты пернул', 'начала мурчать', 'нажал на кнопку и начал сосать', 'дерево чинжоу']

compliments = ["ты лучшая", "ты замечательная", "ты классная", "ты великолепная", "ты великолепна", "ты крутышка", "ты умная", "ты красивая", "ты самая лучшая",
     "ты самая замечательная", "ты просто великолепна", "ты крутая", "замечательна", "красива", "великолепна", "умная", "лучшая", "крутая", "обалденная", "замечательна"]

strangereply = ['я тупой', 'я тупая', 'я глупая', 'я глупый', 'я еблан', 'я ебланка', 'я баран', 'я не умный', 'я не умная', 'я кретин', 'я урод', 'я некрасивый',
     'я некрасивая', 'я бестволочь', 'я скотина', 'я мразь', 'я ублюдок', 'я сука', 'я дебил', 'я дура', 'я овца', 'я такая тупая', 'я такой тупой']

strangequestions = ['как убрать кровь', 'как убить кого-то', 'как сжечь человека', 'как убить человека', 'как убрать кровь после убийства', 'как спрятать труп']

## Статьи из википедии вкратце (очень полезная функция(нет))

aboutsunny = ["Ой, ты хочешь знать обо мне? Хи-хи-хи, я готова рассказать о себе.~ Саёри (англ. Sayori) (яп. 小夜里/さより — деревня) — одна из четырех главных героинь и одна из трех девушек, которой вы можете писать поэмы. Она — друг детства протагониста и вице-президент Литературного Клуба в Акте 1. В Акте 4 она становится президентом Литературного Клуба.", "Я являюсь подругой детства протагониста и вице-президентом Литературного Клуба! Хи-хи-хи.~", "Саёри (англ. Sayori) (яп. 小夜里/さより — деревня) — одна из четырех главных героинь и одна из трех девушек, которой вы можете писать поэмы. Она — друг детства протагониста и вице-президент Литературного Клуба в Акте 1. В Акте 4 она становится президентом Литературного Клуба.", "Если вы хотите знать о моем персонаже в игре, то рассказываю: Сайори - одна из четырех героинь Литературного Клуба, с виду она выглядит очень неосторожной, жизнерадостной и вообще очень позитивной девушкой, что несет радость всем! Однако за ней скрываться нечто большее, чем радость. Впрочем, не буду спойлерить, советую пройти игру самим.~"]
aboutyuri = ["Юри (англ. Yuri) (яп. 百合 — лилия) — одна из четырех главных героинь Doki Doki Literature Club! и участник Литературного Клуба, позже стала вице-президентом в Акте 2 после того, как Саёри была удалена Моникой в Акте 1 и в Акте 4, когда президентом стала Саёри. Она одна из трех девушек, которым вы можете писать поэмы.", "Юри - очень застенчивая и начитанная девушка в Литературном Клубе! Большую часть игры Юри застенчивая, великодушная, вежливая, имеет страсть к теме, которая ей интересна, извиняющаяся, очень умная, зрелая и красноречивая девушка!", "Юри этакая увядающая фиалка (термин персонажа предпочитающего смешиваться с окружением, вместо того чтобы привлекать нежелательное внимание) в Литературном Клубе, из-за её постоянных извинений и застенчивости в дискуссиях за пределами её интересов, коими являются литература, хорроры и сюрреализм.", "У Юри большие проблемы с нахождением новых друзей, а также с сохранением дружбы со старыми, поскольку она имеет тенденцию слишком сильно привязываться к ним. Раньше над ней неоднократно издевались из-за её внешности и манеры поведения, что объясняет её интровертированность."]
aboutmonika = ["Моника (англ. Monika) (яп. モニカ — советник) — главный антагонист игры Doki Doki Literature Club!, также она является одним из главных героев и была президентом Литературного Клуба, пока она не была заменена Саёри после того, как была удалена в Акте 3. Во время прохождения игры становится ясно, что она имеет самосознание, вследствие чего она создает ошибки в игре, тем самым ломая игру. Вы не можете писать Монике поэмы вплоть до Акта 3.", "Моника - очень активная и интересная девушка! Она играет на пианино, она создала Литературный Клуб и вообще является некой звездочка в нашей замечательной школе! Но мне кажется что за ней скрывается нечто большее, она часто что-то недоговаривает и грустит после прихода протагониста...", "Моника, по словам других персонажей — умная, красивая, самоуверенная спортсменка. Она не такая разговорчивая как другие девушки, но не по своему собственному выбору.", "Хоть в клубе Моника появляется с оптимистичным настроением, позже становится очевидно, что ей очень одиноко и грустно в этой симуляции мира, в симуляции, в которой она не сможет достичь своего счастья (завершения своей романтической линии)."]
aboutnatsuki = ["Нацуки (англ. Natsuki) (яп. なつき, ナツキ — лето, редкая) — одна из четырех главных героинь в игре. Член Литературного Клуба и одна из трех персонажей, которым вы можете писать стихи.", "Нацуки - очень милая и с виду интересная девушка! Не смотря на то, что она считает себя не милой - это в корне не так! У нее даже милые кексики получаются, поэмы - абсолютно все!", "Нацуки, казалось бы, стремительная девушка, наглая и агрессивная, но внутри она дружелюбная и общительная.", "Нацуки не любит, когда её называют милой, даже когда она действует как таковая или делает милые вещи, и будет отрицать какие-либо претензии от других, связанные с этим, тем не менее ей гораздо удобнее быть более доброжелательной, если она знает, что люди не будут дразнить ее за это.", "Очень похоже, что у Нацуки комплекс Наполеона. Это означает, что она может быть агрессивной для того, чтобы компенсировать свой небольшой рост."]

## Списки для мини-игр (Списки городов, действия для КНБ, счастливые цифры и т.п)

possible_actions = ["камень", "бумага", "ножницы"]; luckynumber = ['11', '22', '33', '44', '55', '66', '77', '88', '99']

@bot.message_handler(content_types=['new_chat_members']) ## Поиск уведомлений о новых пользователях
def handle_new_members(message): ## Запускается handle на обработку и отправку сообщений в чаты
    for member in message.new_chat_members:
        bot.send_message(message.chat.id, f"Добро пожаловать в группу, {member.first_name}!")

@bot.message_handler(content_types=['text', 'photo', 'voice']) ## Поиск сообщений по типу: текст и фотографии
def get_text_messages(message): ## Запускается handle на обработку и отправку сообщений в чаты

    t = time.localtime() ## Определение времени на компьютере
    content = message.text ## Содержимое сообщения и его контента
    mydate = datetime.now() ## Получение текущего месяца (через ПК)
    translator = Translator(service_urls=['translate.google.com'])
    month = mydate.strftime("%B") ## Выдать название текущего месяца
    chatId = message.chat.id ## Внутренний адрес чата ЛС / группы ID
    chatName = message.chat.title ## Заголовок чата группы, ЛС и т.п
    messageId = message.message_id ## Внутренний адрес сообщения чата
    username = message.from_user.username ## Имя пользователя в ТГ ID
    lastname = message.from_user.last_name ## Фамилия пользователя ТГ
    firstname = message.from_user.first_name ## Имя пользователя в ТГ

    current_time = time.strftime("%H:%M:%S", t) ## Вывод времени в 24-часовом формате (00:00:00)
    if lastname is None: lastname = "[Не задано]" ## Если фамилия участника неизвестна - вывести фамилию в [Не задано]
    if message.content_type == 'photo': content = "[Изображение]" ## Показываем в логах, что пользователь прислал пикчу.
    if not content: content = "[Неизвестно]" ## Если тип контента не был определен - вывести content в [Неизвестный тип]
    if message.content_type == 'voice': content = "[Голосовое сообщение]" ## Показываем в логах, что пользователь прислал голос.
    if chatName is None: chatName = firstname + " (ЛС)" ## Если название чата неизвестно - вывести имя написавшего и приписку ЛС
    if username == 'Channel_Bot' or username == 'GroupAnonymousBot': username = chatName ## Вывести название чата, если пользовать анон.

    ## Вывод в реальном времени данных о имени пользователя, названии чата, содержании сообщения и т.п.
    print(Fore.CYAN + "[", current_time, "]",Fore.WHITE + "[", username, "]", Fore.WHITE + content, "[ Название чата:", chatName, "]")
    bot.send_message(chat_id='-1001927267798', text=f"[ {current_time} ] [ {username} ] {content} [ Название чата: {chatName} ]")
    maintenance_mode = False ## Включение режима отладки и проверки чат-бота (при проведении тех.работ - значение должно быть True)

    ## Блок №1: Основные функции и тело бота.
    ## Действия Сайори при выполнении команды /start (Вывод приветственного сообщения и небольшое меню с действиями)
    if content.lower().startswith("/start"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else: 
            welcomepictureofsayori = open(("pictures/welcome.png"), "rb"); reply = open('!replies/welcomelist.txt', 'r', encoding='utf8');
            captions = reply.read(); bot.send_chat_action(chatId, "upload_photo"); bot.send_photo(chatId, welcomepictureofsayori, caption=captions)

    ## Действия Сайори при выполнении команды /aboutsunny (Справочная команда для вывода информации о ситуации с Сайори в Амино)
    if content.lower().startswith("/aboutsunny") or content.lower().startswith("что стало с сайори в амино"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else: bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('!replies/sayorikz.txt', 'r', encoding='utf8'); bot.reply_to(message, reply)

    ## Действия Сайори при выполнении команды /creator (Справочная команда для вывода информации о создателе)
    if content.lower().startswith("/creator") or content.lower().startswith("создатель"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else: 
            reply = open('!replies/creatorlist.txt', 'r', encoding='utf8');
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Действия Сайори при выполнении команды /settings (Персональные настройки для чат-бота Сайори в Telegram)
    if content.lower().startswith("/settings") or content.lower().startswith("настройки"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else: bot.send_chat_action(chatId, "typing"); time.sleep(3); reply = open('!replies/settingslist.txt', 'r', encoding='utf8'); bot.reply_to(message, reply)

    ## Действия Сайори при выполнении команды /status (Справочная команда, позволяющая узнать рабочий статус Сайори)
    if content.lower().startswith("/status") or content.lower().startswith("!статус"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        elif __name__ == '__main__': bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, "Я нахожусь в сети, жду ваши запросы!")
        else: bot.reply_to(message, "К сожалению, мне не удается связаться с сервером и обработать запрос.")

    ## Действия Сайори при выполнении команды /help (Справочная служба для вывода всех доступных команд и не только)
    if content.lower() in ['/help', '!помощь', '/help@sunnyddlc_bot']:
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else:
            reply = open('!replies/helpservice/helplist.txt', 'r', encoding='utf8');
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
    elif content.lower().startswith("/help1") or content.lower().startswith("!помощь1"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else:
            reply = open('!replies/helpservice/helplist1.txt', 'r', encoding='utf8');
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
    elif content.lower().startswith("/help2") or content.lower().startswith("!помощь2"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else:
            reply = open('!replies/helpservice/helplist2.txt', 'r', encoding='utf8');
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Действия Сайори при выполнении команды /update (Команда, которая выводит информацию о текущих изменениях и обновлениях)

    if content.lower().startswith("!обновления") or content.lower().startswith("/update"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else:
            reply = open('!replies/updatelist.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing");
            time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Действия Сайори при выполнении команды /about (Справочная команда для вывода информации о профиле)
    if content.lower().startswith("/aboutprofile") or content.lower().startswith("о профиле"):
        if maintenance_mode == True and username != "ElliotMoxiess": bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else:
            reply = open('!replies/aboutprofile.txt', 'r', encoding='utf8'); about_text = reply.read(); bot.send_chat_action(chatId, "typing"); time.sleep(3);
            bot.reply_to(message, about_text.format(firstname=firstname, lastname=lastname, username=username, chatName=chatName, chatId=chatId))

    ## Реакция Сайори на команду Вопрос, /ask (Можно задать вопрос Сайори и она ответит на него)
    if content.lower().startswith("/inquiry "): question = message.text[9:]
    elif content.lower().startswith("вопрос, "): question = message.text[8:]
    else: question = None 
    if question is not None:
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
    if content.lower().startswith("/wiki"):
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
    if content.lower().startswith("сайори"):
        sayori1 = message.text[8:] ## Обрезание сообщения до нужных символов
        if sayori1.lower().startswith("привет"): ## Поприветствовать Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis3)))
        elif sayori1.lower().startswith("как дела"): ## Узнать как дела у Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ3)))
        elif sayori1.lower().startswith("что делаешь"): ## Узнать чем занимается Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ4)))
        elif sayori1.lower().startswith(tuple(hatereaction)): ## Реакция на ненависть к Сайори
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ7)))
        elif sayori1.lower().startswith("не грусти"): ## Реакция Сайори на поддержку
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ8)))
        elif sayori1.lower().startswith(tuple(compliments)): ## Реакция Сайори на комплименты
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis11)))
        elif sayori1.lower() in ['я люблю тебя', 'я тебя люблю']: ## Признание Сайори в чувствах
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis8)))  
        elif sayori1.lower().startswith("переведи на английский: "): ## Система перевода (основана с помощью Google Translate)
            trans_text = message.text[31:]; translator_text = open('translator.txt', 'w'); translator_text.write("\n"+trans_text)
            translator_text.close(); translator_text1  = open('translator.txt', 'r'); finaltext = translator_text1.read()
            result = translator.translate(finaltext, dest='en'); translator_text.close() ## Сайори переводит с любого языка на англ.
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, f"Вот ваш перевод на английский: {result.text}")
        elif sayori1.lower().startswith("переведи на русский: "):
            trans_text = message.text[28:]; translator_text = open('translator.txt', 'w', encoding='utf8'); translator_text.write(trans_text)
            translator_text.close(); translator_text1  = open('translator.txt', 'r', encoding='utf8'); finaltext = translator_text1.read()
            result = translator.translate(finaltext, dest='ru'); translator_text.close() ## Сайори переводит с любого языка на русс.
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, f"Вот ваш перевод на русский: {result.text}")
        elif sayori1.lower() in ['пришли фанарт', 'пришли арт']: ## Попросить прислать фанарт из ДДЛК
            path2 = pwd("fanart"); random_filename = str(random.choice(path2)); cg2 = open((random_filename), "rb")
            bot.send_chat_action(chatId, "upload_photo"); time.sleep(3); bot.send_photo(chatId, cg2) # Отправить фотографию в чат, где происходит общение
        elif sayori1.lower() in ['пришли катсцену', 'пришли cg']: ## Попросить прислать катсцену из ДДЛК
            path1 = pwd("sayori_cg"); random_filename = str(random.choice(path1)); cg = open((random_filename), "rb")
            bot.send_chat_action(chatId, "upload_photo"); time.sleep(3); bot.send_photo(chatId, cg); # Отправить фотографию в чат, где происходит общение
        elif sayori1.lower().startswith(tuple(keyword10)): ## Реакция Сайори на вопрос касаемо ее настроения
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ10)))
        elif sayori1.lower().startswith(tuple(keyword11)): ## Реакция Сайори на необходимость моральной поддержки
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(react1)))
        elif sayori1.lower().startswith(tuple(keyword13)): ## Реакция Сайори на ее попытку "заснуть"
            bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(answ11)))
        elif sayori1.lower().startswith('какой сегодня месяц'): ## Реакция Сайори на вопрос касаемо текущего месяца
            reply = open('!replies/questionservice/monthfortoday.txt', 'r', encoding='utf8'); answer = reply.read(); bot.send_chat_action(chatId, "typing"); time.sleep(3)
            bot.reply_to(message, answer.format(month=month)) ## Так как параметр {month} в текстовом формате - его нужно переконвертировать в f
        elif sayori1.lower().startswith("назови число от ") or sayori1.lower().startswith("выбери число от "):
            bot.send_chat_action(chatId, "typing"); time.sleep(3); random_number = message.text[24:]; splitted_text = random_number.split(); del splitted_text[1]
            bot.reply_to(message, "Случайное число от "+ random_number +" - "+ random.choice(splitted_text))
        elif sayori1.lower().startswith(tuple(keyword9)): ## Вопрос, какое аниме может посоветовать Сайори пользователю
            reply = open('!replies/questionservice/aboutanime.txt', 'r', encoding='utf8') 
            bot.send_chat_action(chatId, "typing"); time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        elif sayori1.lower().startswith(tuple(keyword12)): ## Попросить Сайори прислать совместимость между знаками зодиака
            bot.reply_to(message, str(random.choice(answ12)))  ## Сайори отвечает на запрос пользователя и присылает таблицу
            compatibility = open(("pictures/compatibility.png"), "rb"); bot.send_photo(chatId, compatibility)
        elif sayori1.lower().endswith('?'): bot.reply_to(message, str(random.choice(lis)))
        else: bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis12))) ## Если нету реакции - выдать "м?" и т.п

    ## Система отправки и регистрации предложений по улучшению Сайори (СОРПУС)
    if content.lower().startswith("!сорпус ") or content.lower().startswith("/sorpus "):
        sorpustext = message.text[8:] ## Выписать только содержимое идеи / предложения
        with open("!replies/suggestionfillter/fooldetector.txt", "r", encoding="utf-8") as file:
            fooldetector = [word.strip() for word in file.readlines()]; words = sorpustext.split()
        is_banned_word = False ## флаг, обозначающий наличие запрещенных слов
        for word in words:
            if word.lower() in fooldetector:
                sorpustext = sorpustext.replace(word, "*" * len(word))
                bot.reply_to(message, "Ваш запрос содержит просьбу исправить что-то, для того что бы сообщить о баге и попросить исправить его - используйте команду /sorrew")
                is_banned_word = True ## устанавливаем флаг запретного слова
                break  ## прерываем цикл, так как уже нашли запрещенное слово
        if not is_banned_word:  # если запрещенных слов не было, можно записать идею в файл и отправить ответ
            suggestion_text = open("suggestions.txt", "a") ## Открыть файл с предложениями
            sorpus = suggestion_text.write(sorpustext) ## Записать предложение в файл
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
    if content.lower().startswith("!соррев ") or content.lower().startswith("/sorrew "):
        sorrewtext = message.text[8:] ## Выписать только содержимое идеи / предложения
        suggestion_text = open("reviewsayori.txt", "a") ## Открыть файл с предложениями
        sorrew = suggestion_text.write(sorrewtext) ## Записать предложение в файл
        suggestion_text.write("\n") ## Если данные есть - начать с новой строки
        suggestion_text.close() ## Закрыть файл с предложениями и идеями
        bot.reply_to(message, "Ваш отзыв был отправлен на компьютер создателя, спасибо за то, что вы делитесь опытом! 💗")
        print(Fore.CYAN + "[", current_time, "]", Fore.WHITE, "Поступил отзыв о работе Сайори, подробнее в recallsayori.txt")
        notification.notify( ## Создать оповещение системы
            title = 'Прошу немного внимания!', ## Заголовок уведомления
            message = 'Был получен отзыв от пользователя!',
            app_icon = 'pictures/console.ico', ## Инонка для уведомления
            timeout = 3, ## Через сколько секунд пропадет уведомление
        )
        
    ## Реакция Сайори на реплики пользователя, которые не относятся к какому либо блоку.

    if content.lower().startswith("*обнял*") or content.lower().startswith("*обняла*"): ## Обнять Сайори (правильно!)
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.send_message(chatId, str(random.choice(lis2)))

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
    if content.lower() in ['доброе утро', 'всем доброго утра', 'всем доброе утро']:
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis9)))

    if content.lower() in ['спокойной ночи', 'сладких снов', 'всем спокойной ночи']:
        bot.send_chat_action(chatId, "typing"); time.sleep(3); bot.reply_to(message, str(random.choice(lis10)))
        photo = open('pictures/SayoriSleep.jpg', 'rb'); bot.send_photo(chatId, photo)

    ## Блок №1.1. Устаревшие команды и дополнения к телу бота.
    ## Попросить прислать Сайори ссылки на сайт ДДЛК и википедию по игре (Фандом и оригинальная англ.)

    if content.lower().startswith(tuple(keyword)):
        reply = open('!replies/ddlcsitelist.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing")
        time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Попросить прислать Сайори саундтреки из визуальной новеллы (MP3 и YouTube)
    if content.lower().startswith("/track"):
        nametrack = message.text[7:]
        if nametrack.lower() in ['список']:
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

    if content.lower().startswith("!гс") or content.lower().startswith("/gs"): voice_text = message.text[3:]
    elif content.lower().startswith("/gs@sunnyddlc_bot"): voice_text = message.text[17:]
    else: voice_text = None
    if voice_text is not None:
        if maintenance_mode == True and username != "ElliotMoxiess":
            bot.reply_to(message, "Проводятся технические работы, больше деталей в Telegram канале: @AminoDDLC")
        else:
            if len(voice_text) <= 4 or content.lower() == '/gs@sunnyddlc_bot':
                reply = open('!replies/errormessages/notextings.txt', 'r', encoding='utf8'); bot.send_chat_action(chatId, "typing")
                time.sleep(3); answer = reply.read(); bot.reply_to(message, answer); reply.close()
            else:
                myobj = gTTS(text=voice_text, lang='ru', slow=False);myobj.save("audio.mp3"); voice = open("audio.mp3", "rb")
                bot.send_chat_action(chatId, "record_audio"); time.sleep(3); bot.send_voice(chatId, voice)

    ## Блок 1.2. Действия и взаимодействия с участниками в группе.

    if content.lower().startswith("действия") or content.lower().startswith("/actions"):
        reply = open('!replies/actionlist.txt', 'r', encoding='utf8')
        answer = reply.read(); bot.reply_to(message, answer); reply.close()

    if content.lower().startswith("пощекотать @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, '...Аха-ха-ха...! П-перестань щекотать меня...!')
        tickle = open('gifanim/tickle.gif', 'rb')
        bot.send_document(chatId, tickle)
    elif content.lower().startswith("пощекотать @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} щекочет {author2}')
        tickle = open('gifanim/tickle.gif', 'rb')
        bot.send_document(chatId, tickle)

    if content.lower().startswith("ударить @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Эй, ты чего дерешься то? Больно же... 😢')
    elif content.lower().startswith("ударить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} бьёт {author2}')
        punch = open('gifanim/punch.gif', 'rb')
        bot.send_document(chatId, punch)

    if content.lower().startswith("тыкнуть @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Эй, Не нужно в меня тыкать!')
    elif content.lower().startswith("тыкнуть @"):    
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} тыкает в {author2}')
        poke = open('gifanim/poke.gif', 'rb')
        bot.send_document(chatId, poke)

    if content.lower().startswith("погладить @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Няяяяяя, люблю когда меня гладят!~')
    elif content.lower().startswith("погладить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} гладит {author2}')
        pat = open('gifanim/pat.gif', 'rb')
        bot.send_document(chatId, pat)

    if content.lower().startswith("обнять @sunnyddlc_bot"):
        bot.send_chat_action(chatId, "typing"); time.sleep(3)
        bot.reply_to(message, 'Урааааа, обнимашкииии!~ 🥰')
    elif content.lower().startswith("обнять @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} обнимает {author2}')
        hug = open('gifanim/hug.gif', 'rb')
        bot.send_document(chatId, hug)

    if content.lower().startswith("покормить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} кормит {author2}')
        feed = open('gifanim/feed.gif', 'rb')
        bot.send_document(chatId, feed)

    if content.lower().startswith("прижаться @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} прижимается к {author2}')
        hug = open('gifanim/hug.gif', 'rb')
        bot.send_document(chatId, hug)

    if content.lower().startswith("поцеловать @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} целует {author2}')
        kiss = open('gifanim/kiss.gif', 'rb')
        bot.send_document(chatId, kiss)

    if content.lower().startswith("укусить @"):
        author2 = message.text.split("@")[1].replace("@", "")[0:50]
        bot.reply_to(message, f'{username} делает кусь {author2}')
        bite = open('gifanim/bite.gif', 'rb')
        bot.send_document(chatId, bite)

    ## Блок №2. Мини-игры и развлечения. (Всего игр - 4)
    if content.lower().startswith("!игра") or content.lower().startswith("/game"):
        gamequest = message.text[6:]; bot.send_chat_action(chatId, "typing"); time.sleep(3)
        ## Мини-игра №1 (Счастливый билетик - выдается шестизначный билетик, в нем должны попасться одинаковые цифры)
        if gamequest.lower().startswith("счастливый билетик") or gamequest.lower().startswith("1"):
            bot.send_message(chatId, "Я запускаю первую мини-игру, пожалуйста подождите...")
            time.sleep(1.5); ticketgot = str(sixnumber(6))
            bot.send_message(chatId, "Итак, твой билетик с номером: "+ticketgot); time.sleep(1.5)
            if any(x in ticketgot for x in luckynumber):
                bot.reply_to(message, "Поздравляю тебя с победой! В твоем билетике оказались две одинаковые цифры! Я всегда в тебя верю.~ 💗")
            else:
                bot.reply_to(message, "Ой-ой, к сожалению в твоем билетике не оказалось две одинаковых цифр, может тебе повезет в следующий раз? 😌")
        ## Мини-игра №2 (Камень, ножницы, бумага - классическая игра, в пояснениях не нуждается)
        ## Сценарий мини-игры №1 - игрок выбирает камень, Сайори выбирает.
        elif gamequest.lower().startswith('2'):
            player_choice = gamequest.lower().split()[1] # Получаем выбор игрока (что он выбрал)
            if player_choice in ['камень', 'ножницы', 'бумага']: rock_paper_scissors(bot, message, player_choice)
            else: bot.reply_to(message, "Я не поняла тебя, что ты имел ввиду? Перефразируй или напиши корректно.")
        elif gamequest.lower().startswith("список"): reply = open('!replies/gamelist.txt', 'r', encoding='utf8'); answer = reply.read(); bot.reply_to(message, answer); reply.close()
        else: reply = open('!replies/wronggame.txt', 'r', encoding='utf8'); answer = reply.read(); bot.reply_to(message, answer); reply.close()

    ## Блок №3. Административные и отладочные команды
    ## Дистанционная очистка лог-файла (txt) с помощью команды.
    if content.lower().startswith("!очисткалогов") or content.lower().startswith("/cll"):
        if username == "ElliotMoxiess":
            bot.send_chat_action(chatId, "typing"); time.sleep(3); open("log.txt", "w").close(); print("Логи были успешно очищены.")
            bot.reply_to(message, 'Я успешно выполнила данную команду! Код ее выполнения: S0cl00, больше сведений находится в файле log.txt!')
        else:
            bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку, если ты есть есть в списке админов!')

    ## Дистанционная очистка терминала бота с помощью команды.
    if content.lower().startswith("!очиститьтерминал") or content.lower().startswith("/cls"):
        bot.send_chat_action(chatId, "typing")
        if username == "ElliotMoxiess":
            time.sleep(3); os.system('cls'); print("Терминал был успешно очищен.")
            bot.reply_to(message, 'Я успешно выполнила данную команду! Код ее выполнения: S0ct00, больше сведений находится в файле log.txt!')
            logger.warning('Была запрошена очистка терминала бота, команда выполнена успешно. Код выполнения операции: S0ct00')
        else:
            bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку, если ты есть есть в списке админов!')

    ## Дистанционная очистка предложений (suggestions.txt) с помощью команды.
    if content.lower().startswith("!очиститьидеи") or content.lower().startswith("/cli"):
        if username == "ElliotMoxiess":
            botssss.send_chat_action(chatId, "typing"); time.sleep(3); open("suggestions.txt", "w").close(); print("Предложения был успешно очищены.")
            bot.reply_to(message, 'Я успешно выполнила данную команду! Код ее выполнения: S0ci00, больше сведений находится в файле log.txt!')
            logger.warning('Была запрошена очистка предложений бота, команда выполнена успешно. Код выполнения операции: S0ci00')
        else:
            bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку, если ты есть есть в списке админов!')

    ## Дистанционная перезагрузка / обновление Сайори с помощью команды.
    if content.lower().startswith("!перезагрузка") or content.lower().startswith("/restart"):
        if username == "ElliotMoxiess":
            bot.reply_to(message, "Инициализирована команда перезагрузки кода, пожалуйста ожидайте выполнения операции... ☀")
            process = subprocess.Popen('SayoriBotT', shell=True); bot.stop_polling(); process.wait()
        else:
            bot.reply_to(message, 'К сожалению у тебя нету прав для выполнения данной команды, обратись в поддержку, если ты есть есть в списке админов!')  

    ## Блок №4. Система обнаружения ошибок внутри кода Сайори (СООВКС)
    ## Проверяем, запущен ли файл напрямую, в случае успеха - бот начинает работу
if __name__ == '__main__': ## Проверка того, был ли запущен файл напрямую
    try:
        bot.polling(none_stop=True, interval=0) ## Просматривать чаты и получать новые запросы бесконечно
        bot.notifyOnMessage() ## При получении новых запросов и сообщений в чатах - проверять содержимое пакета
    except Exception as error: 
        print(f"{type(error).__name__}: Причина прервания программы: {error}, идет перезагрузка...")
        notification.notify( ## Создать оповещение системы
            title = 'Произошла ошибка в коде', ## Заголовок уведомления
            message = 'Все детали находятся в терминале бота, выполняется перезагрузка.',
            app_icon = 'pictures/console.ico', ## Инонка для уведомления
            timeout = 3, ## Через сколько секунд пропадет уведомление
        )
        logger.error(f'Произошла ошибка: {type(error).__name__}: {error}')
        time.sleep(15); process = subprocess.Popen('SayoriBotT', shell=True); os.system('cls'); bot.stop_polling(); process.wait()
