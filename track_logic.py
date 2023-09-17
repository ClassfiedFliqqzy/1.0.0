import telebot; import time

def original_game(bot, message, nametrack, chatId):
   if nametrack.lower() in ['список', 'list']:
      reply = open('!replies/soundlist.txt', 'r', encoding='utf8')
      bot.send_chat_action(chatId, "typing"); time.sleep(3)
      answer = reply.read(); bot.reply_to(message, answer, parse_mode="html"); reply.close()
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
      bot.reply_to(message, "Для использования данной команды необходимо ввести после команды цифру саундтрека или его полное название. Пример: /track 1. 😊")  