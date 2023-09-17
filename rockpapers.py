import random
import time

def rock_paper_scissors(bot, message, player_choice):
    sayorichoose = ['камень', 'ножницы', 'бумага']
    sayori_select = random.choice(sayorichoose); time.sleep(1)
    bot.reply_to(message, "Ты выбрал(а) "+player_choice+", я выбрала: "+sayori_select); time.sleep(1)
    if sayori_select.lower() == player_choice.lower():
        bot.reply_to(message, "Это ничья, я рада что никто не выиграл! Хотя поражения всегда происходят где-то или в чем-то...")
    elif (player_choice.lower() == "камень" and sayori_select.lower() == "ножницы") or (player_choice.lower() == "ножницы" and sayori_select.lower() == "бумага") or (player_choice.lower() == "бумага" and sayori_select.lower() == "камень"):
        bot.reply_to(message, "Ура! Ты победил, молодец! Мне просто не повезло, это нормально!")
    else:
        bot.reply_to(message, "Я победила! Ха-ха-ха! Но не расстраивайся, уверена тебе просто не повезло, это нормально!")