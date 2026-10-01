import os

# Выдаётся владельцу бота
# Команды бота:
# /start - начать
# /admin - включает админку если ID пользователя совпадает с ADMIN_ID
#
API_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
ADMIN_ID = [
    chat_id.strip()
    for chat_id in os.environ.get('TELEGRAM_ADMIN_ID', '').split(',')
    if chat_id.strip()
]
BLACK_LIST = ['']
BLACK_LIST_MESSAGE = 'У вас нет доступа к боту!😭'

CHATS_INFO = [["-1001956144520", "-1002030631293", "-1002094874052", "-1002031696214"],                                 #ID
              ['https://t.me/FILMetsd', 'https://t.me/Animaaaad', 'https://t.me/fggswsc', 'https://t.me/OtVeTsA']]      #URL
                #КИНО                       #АНИМЕ                  #ПРО100 КАНАЛ           ЕГЭ ОТВЕТЫ 2024
  
START_TEXT = '👋 Привет, самые крутые обои только у нас! Выбирай!👇'
WAITING_TEXT = 'Подожди немного⏳'
UNKNOWN_TEXT = 'Извините, я вас не понял.🧐'
EXCEPTION_TEXT = '😢Не получилось, попробуйте ещё раз!'
CONDITION_TEXT = 'Для работы бота нужно подписаться на каналы!🤖'
MAILING_TEXT = "WallPapper-bot"
THAT_IS_NOT_ALL_TEXT = 'Ещё не всё'
ALL_RIGHT_TEXT = 'Отлично! Теперь можешь пользоваться ботом!'
