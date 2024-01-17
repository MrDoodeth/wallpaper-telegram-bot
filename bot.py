import telebot
import random
import os.path
from telebot import types
bot = telebot.TeleBot("6714412265:AAE6Opkyc2w3PO3SAEwCIa7Us2I4NdUoCrk")

@bot.message_handler(commands=['start'])
def start(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Случайные обои 🎲")
    item2 = types.KeyboardButton("Тачки🏎")
    item3 = types.KeyboardButton("Абстракция🟦")
    item4 = types.KeyboardButton("Архитектура🏛")
    item5 = types.KeyboardButton("Космос🌑")
    item6 = types.KeyboardButton("Мемные🤣")
    item7 = types.KeyboardButton("Персонажи👩‍🦰")
    item8 = types.KeyboardButton("Природа🐈")
    
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    
    bot.send_message(message.chat.id,'👋 Привет,самые крутые обои только у нас! Выбирай!👇', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def Action(message): 
    def Send(directory):
        bot.send_message(message.chat.id,'Подожди немного⏳')
        # Получение списка файлов в указанной директории
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        # Выбор случайного файла
        random_file = random.choice(files)
        random_file_path = os.path.join(directory, random_file)        
        image = open(random_file_path, 'rb')         
        bot.send_photo(chat_id=message.chat.id, photo=image)
          
    if message.chat.type == 'private':
        if message.text == 'Случайные обои 🎲': 
            try:
                Send(directory='Resources/Другое')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')       
           
        elif message.text == 'Тачки🏎':
            try:
                Send(directory='Resources/Тачки')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')  
            
        elif message.text == 'Абстракция🟦':
            try:
                Send(directory='Resources/Абстракция')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')  

            
        elif message.text == 'Архитектура🏛':
            try:
                Send(directory='Resources/Архитектура')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')  

            
        elif message.text == 'Космос🌑':
            try:
                Send(directory='Resources/Космос')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')  

        
        elif message.text == 'Мемные🤣':
            try:
                Send(directory='Resources/Мемные')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')  

        
        elif message.text == 'Персонажи👩‍🦰':
            try:
                Send(directory='Resources/Персонажи')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')  

        
        elif message.text == 'Природа🐈':
            try:
                Send(directory='Resources/Природа')
            except Exception as e:
                bot.send_message(message.chat.id,'😢Не получилось, попробуйте ещё раз!')
        else:
            bot.send_message(message.chat.id,'Извините, я вас не понял.🧐')  
             
            

               
bot.infinity_polling()


    