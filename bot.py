from os import close
from pickle import TRUE
from unittest import result
import telebot
import config
import random
import os.path
from telebot import types


bot = telebot.TeleBot(config.API_TOKEN)

@bot.message_handler(commands=['admin'])
def admin(message):        
    if str(message.chat.id) in config.ADMIN_ID:

        markup = types.InlineKeyboardMarkup(row_width=1)
        
        item1 = types.InlineKeyboardButton("Админ панель🕹", callback_data='admin')
        item2 = types.InlineKeyboardButton("Вернуться к боту🔙", callback_data='back')

        markup.add(item1, item2)
        
        bot.send_message(message.chat.id,'Приветствуем администратора!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Упс! Вы не являетесь администратором.')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == 'admin':  
            #Действия админа
            print('admin signed in')
            
            markup = types.InlineKeyboardMarkup(row_width=1)
        
            item1 = types.InlineKeyboardButton("Получить 🆔 пользователей", callback_data='users_ID')
            item2 = types.InlineKeyboardButton("Создать рассылку📥", callback_data='mailing')
            item3 = types.InlineKeyboardButton("Вернуться к боту🔙", callback_data='back')

            markup.add(item1, item2, item3)
        
            bot.send_message(call.message.chat.id,'Выберите действие⬇️', reply_markup=markup)
            
        elif call.data == 'users_ID':
                with open('users_id.txt', "r+") as users_list:
                    users_list.seek(0)             
                    bot.send_document(call.message.chat.id, users_list) 
                    print(f'Отправил {users_list.name}!')
                    users_list.close()
        elif call.data == 'mailing':
            #Рассылка
            print('Рассылка...') 
            return      
        elif call.data == 'back':
            bot.delete_message(call.message.chat.id, call.message.id)
    except Exception as e:
        bot.send_message(call.message.chat.id,'Что-то пошло не так.')
        print(repr(e))
   
                   
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
    
    def Exept():
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        item1 = types.InlineKeyboardButton("КАНАЛ №1", url=config.CHATS_URL[0]) #КИНО
        item2 = types.InlineKeyboardButton("КАНАЛ №2", url=config.CHATS_URL[1]) #АНИМЕ
        item3 = types.InlineKeyboardButton("КАНАЛ №3", url=config.CHATS_URL[2]) #ПРО100 КАНАЛ           
        item4 = types.InlineKeyboardButton("КАНАЛ №4", url=config.CHATS_URL[3]) #ЕГЭ ОТВЕТЫ 2024
            
        markup.add(item1, item2, item3, item4)
        
        bot.send_message(message.chat.id,'Для работы бота нужно подписаться на каналы!🤖', reply_markup=markup) 
        
        
    if message.chat.type == 'private':
        access = False
        for i in range(0,4):            
                result = bot.get_chat_member(config.CHATS_ID[i], message.chat.id).status
                access = result in ["creator", "administrator", "member"]
                if access:
                    print(f'Подписан на Канал №{i+1}')                          
                else:
                    print('Ещё не всё')
                    Exept()           
                    return               
        else:
            if access:
                #Заполнение списка users_id
                with open('users_id.txt', "r+") as users_list:
                    l = users_list.readlines()
                    if not(f'{message.chat.id}\n' in l):
                        users_list.write(f'{message.chat.id}\n')
                        print('ID добавлен')
                        users_list.seek(0)
                        users_list.close()
            print('\n')
                    
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


    