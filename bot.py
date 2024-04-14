import telebot
import config
import random
import os.path
from telebot import types


bot = telebot.TeleBot(config.API_TOKEN)
updates = bot.get_updates()

@bot.message_handler(commands=['admin'])
def admin(message):        
    if str(message.chat.id) in config.ADMIN_ID:

        markup = types.InlineKeyboardMarkup(row_width=1)
        
        item1 = types.InlineKeyboardButton("Получить 🆔 пользователей", callback_data='users_ID')
        item2 = types.InlineKeyboardButton("Создать рассылку📥", callback_data='mailing')
        item3 = types.InlineKeyboardButton("Вернуться к боту🔙", callback_data='back')

        markup.add(item1, item2, item3)
        
        bot.send_message(message.chat.id,'Приветствуем администратора!🕹 Выберите действие⬇️', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Упс! Вы не являетесь администратором.')

@bot.callback_query_handler(func=lambda call: True)                   
def callback_inline(call):
    try:
        if call.data == 'users_ID':
                with open('users_id.txt', "r+") as users_list:
                    users_list.seek(0)
                    bot.send_document(call.message.chat.id, users_list)
                    print(f'Отправил {users_list.name}!')
                    users_list.close()
        elif call.data == 'mailing':
            markup = types.InlineKeyboardMarkup(row_width=1)  
            item1 = types.InlineKeyboardButton("Отмена❌", callback_data='back')
            markup.add(item1)
            msg = bot.send_message(call.message.chat.id, "Отправьте пост📩", reply_markup=markup)
            bot.register_next_step_handler(msg, Send_Mailing) 
                         
        elif call.data == 'back':
            bot.delete_message(call.message.chat.id, call.message.id)
        elif call.data == 'check':
            if Check(call.message) == False:
                bot.send_message(call.message.chat.id, config.THAT_IS_NOT_ALL_TEXT)
                Exept(call.message)
            else:
                bot.send_message(call.message.chat.id,config.ALL_RIGHT_TEXT)
            
    except Exception as e:
        bot.send_message(call.message.chat.id,'Что-то пошло не так.')
        print(repr(e))
   
def Send_Mailing(msg):
                #Рассылка
                with open('users_id.txt', "r+") as users_list:
                    users_list.seek(0)
                    l = users_list.readlines()
                    for i in range(0, len(l)):
                        try:       
                            bot.send_message(l[i], msg.text)  #нужно настроить parse_mode
                            print(f'{i+1}) successfully')
                        except Exception as e:
                            print(repr(e))
                            continue
                    print('Всё отправлено!')      
                    users_list.seek(0)
                    users_list.close()
                           
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
    
    bot.send_message(message.chat.id, config.START_TEXT, reply_markup=markup)

def Exept(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
        
    item1 = types.InlineKeyboardButton("КАНАЛ №1", url=config.CHATS_INFO[1][0]) #КИНО
    item2 = types.InlineKeyboardButton("КАНАЛ №2", url=config.CHATS_INFO[1][1]) #АНИМЕ
    item3 = types.InlineKeyboardButton("КАНАЛ №3", url=config.CHATS_INFO[1][2]) #ПРО100 КАНАЛ           
    item4 = types.InlineKeyboardButton("КАНАЛ №4", url=config.CHATS_INFO[1][3]) #ЕГЭ ОТВЕТЫ 2024
    item5 = types.InlineKeyboardButton("ПОДПИСАЛСЯ", callback_data='check') 
            
    markup.add(item1, item2, item3, item4, item5)
        
    bot.send_message(message.chat.id, config.CONDITION_TEXT, reply_markup=markup) 

def Check(message):
    access = False
    for i in range(0,4):            
        result = bot.get_chat_member(config.CHATS_INFO[0][i], message.chat.id).status
        access = result in ["creator", "administrator", "member"]
        if access:
            print(f'Подписан на Канал №{i+1}')                          
        else:
            print('Ещё не всё')                       
            return False               
    else:
        #Заполнение списка users_id
        with open('users_id.txt', "r+") as users_list:
            l = users_list.readlines()
            if not(f'{message.chat.id}\n' in l):
                users_list.write(f'{message.chat.id}\n')
                print('ID добавлен')
                users_list.seek(0)
                users_list.close()
        print('\n')
        
def CheckBlackList(message):
    isBlock = str(message.chat.id) in config.BLACK_LIST
    if isBlock:
        bot.send_message(message.chat.id, config.BLACK_LIST_MESSAGE)
        print("=Blocked=")
        return True
    else:
        return False
           

@bot.message_handler(content_types=['text'])
def Action(message): 
    def Send(directory):
        bot.send_message(message.chat.id,config.WAITING_TEXT)
        # Получение списка файлов в указанной директории
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        # Выбор случайного файла
        random_file = random.choice(files)
        random_file_path = os.path.join(directory, random_file)        
        image = open(random_file_path, 'rb')         
        image.seek(0)
        bot.send_document(message.chat.id, document=image)
     
    if message.chat.type == 'private':
        
        if CheckBlackList(message):
            return
        
        if Check(message) == False: 
            Exept(message)
            return
                    
        if message.text == 'Случайные обои 🎲': 
            try:
                Send(directory='Resources/Другое')
            except Exception as e:
                print(repr(e))
                bot.send_message(message.chat.id, config.EXCEPTION_TEXT)       
           
        elif message.text == 'Тачки🏎':
            try:
                Send(directory='Resources/Тачки')
            except Exception as e:
                bot.send_message(message.chat.id, config.EXCEPTION_TEXT)  
            
        elif message.text == 'Абстракция🟦':
            try:
                Send(directory='Resources/Абстракция')
            except Exception as e:
                bot.send_message(message.chat.id, config.EXCEPTION_TEXT)  
            
        elif message.text == 'Архитектура🏛':
            try:
                Send(directory='Resources/Архитектура')
            except Exception as e:
                bot.send_message(message.chat.id, config.EXCEPTION_TEXT)  

            
        elif message.text == 'Космос🌑':
            try:
                Send(directory='Resources/Космос')
            except Exception as e:
                bot.send_message(message.chat.id,config.EXCEPTION_TEXT)  

        
        elif message.text == 'Мемные🤣':
            try:
                Send(directory='Resources/Мемные')
            except Exception as e:
                bot.send_message(message.chat.id,config.EXCEPTION_TEXT)  

        
        elif message.text == 'Персонажи👩‍🦰':
            try:
                Send(directory='Resources/Персонажи')
            except Exception as e:
                bot.send_message(message.chat.id,config.EXCEPTION_TEXT)  

        
        elif message.text == 'Природа🐈':
            try:
                Send(directory='Resources/Природа')
            except Exception as e:
                bot.send_message(message.chat.id, config.EXCEPTION_TEXT)
        else:
            bot.send_message(message.chat.id,config.UNKNOWN_TEXT)
                          
bot.infinity_polling()