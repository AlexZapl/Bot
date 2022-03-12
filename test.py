from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from datetime import datetime

NICKNAME = 'AlexZapl'
bot_token = '5268805778:AAHjHzJlQL1es8cbXs2CQFVu5aRPKNTc0hY'
bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

current_datetimef = datetime.now()
print('Day', current_datetimef.day, '  ',
      str(current_datetimef.hour) + ':' + str(current_datetimef.minute) + ':' + str(current_datetimef.second))
print('''
                                                   SS###&&&&&##SS               
                                                ##&&&&&&&&&&&&&&&&#S                
                  SSS####SSSS                S#&&&&&&&&&&&&&&&&&&&&&#S                
             S##&&&&&&&&&&&&&&&##S         #&&&&&&&&&&&&&&&&&&&&&&&&&&#                
           #&&&&&&&&&&&&&&&&&&&&&&&#S    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S                
         #&&&&&&&&&&&&&&&&&&&&&&&&&&&&##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S                
       #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S                
      #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S 
     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##&&&&&&&&&&&&&&&&&#
   #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#      S&&&&&&&&&&&&&&&
   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S         &&&&&&&&&&&&&&
  S&&##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#  #&&&&&          #&&&&&&&&&&&&&
  S&&*&&&&&&&&&&&&&&&&#SSSS#&&&&&&&# S&&&&&&#  S&&&&&#        #&&&&&&&&&&&&&&
  S&SS&&#&&&&&&&&&&&#        #&&&&&#  S&&&&#   S&&&&&&&SSSSS#&&&&&&&&&&&&&&&&
  S#*&&#*&&&&&&&&&&&          &&&&&&S         S&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S
   S&&*#&##&&&&&&&&#         &&&&&&&&#S   S#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&SS
   &&S*&&*#&&&&&&&&&#S     S&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#SS
   S&&*#&SS&&&&&&&&&&&&&##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S 
    #S*&&*#&&S#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S  
     #&SS&&#*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&SS   
      &&*#&&*#&&&S&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#    
       SS&&#*&&&SS&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#     
        S&&*#&&&*#&&S&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#                
         S#*&&&#*&&#*&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#                
           &&&*S&&SS&&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&SS                
             S#&*&&&*#&&SS&&&##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                
               &&#*&&&*#&&&S#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#S                
                 #SS&&&*&&&&*#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&S                
                   S&&#*&&&#*&&&S&&&#&&&&&&&&&&&&&&&&&&&&&&&&&#                
                     S*S&&&SS&&#S&&&S&&&&&&&&&&&&&&&&&&&&&&&&S                
                        S#&*#&&SS&&#S&&#&&&&&&&&&&&&&&&&&&&#                
                            #&&S#&&#S&&S&&#&&&&&&&&&&&&&&&S                
                              S*S&&SS&#*&&S&&#&&&&&&&&&&#                                
                                  SS#&&S&&#&&&&&&&&&&&&S                                
                                      S#&&&&&&&&&&&&&#                                
                                          S##&&&&&&#                                
                                              S###S                                ''')

current_datetime = datetime.now()
print('Day', current_datetime.day, '  ',
      str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second))
GENDER = 0
PHOTO = 1
BIO = 2
VIDEO = 3

def start(update, context):
    reply_keyboard = [['Мужчина', 'Женщина']]
    update.message.reply_text('Добрый день! Вас приветствует Компания PineApple! Укажите свой пол, вы мужчина или женщина?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return GENDER


def gender(update, context):
    update.message.reply_text('Отлично! Теперь отправьте нам свою фотографию, мы заведем личную карточку, или отправьте /skip если хотите пропустить этот шаг')

    return PHOTO


def photo(update, context):
    user = str(update.message.from_user['username'])
    photo_file = update.message.document.get_file()
    photo_file.download(user + '_photo.jpg')
    update.message.reply_text(
        'Отлично! Вы сегодня прекрасно выглядите! Теперь отправьте краткое сообщение о себе, или отправьте /skip если хотите пропустить этот шаг')

    return BIO


def skip_photo(update, context):
    update.message.reply_text('Значит без фото! Окей, отправьте краткое сообщение о себе или отправьте /skip.')

    return BIO


def bio (update, context):
    #Будет принимать краткое текстовое резюме
    user = str(update.message.from_user['username'])
    bio_file = update.message.text
    update.message.reply_text(
        'Отлично! Теперь отправьте краткое видеосообщение о себе, или отправьте /skip если хотите пропустить этот шаг')

    return VIDEO


def skip_bio(update, context):
    update.message.reply_text('Значит без БИО! Окей, отправьте краткое видеосообщение о себе или отправьте /skip.')

    return VIDEO


def video (update, context):
    #Будет принимать видеорезюме
    user = str(update.message.from_user['username'])
    photo_file = update.message.document.get_file()
    photo_file.download(user + '_video.mp4')
    update.message.reply_text(
        'Отлично! Мы с вами свяжемся!')


def skip_video(update, context):
    update.message.reply_text('Значит без видео! Окей, мы свами свяжемся')


def cancel(update, context):
    update.message.reply_text('Надеюсь вы еще нам напишите - возможно мы нуждаемся именно в вас!')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
gender_handler = MessageHandler(Filters.regex('^(Мужчина|Женщина)$'), gender)
photo_handler = MessageHandler(Filters.document.category("image"), photo)
skip_photo_handler = CommandHandler('skip', skip_photo)
bio_handler = MessageHandler(Filters.text, bio)
skip_bio_handler = CommandHandler('skip', skip_bio)
video_handler = MessageHandler(Filters.document.category("image"), photo)
skip_video_handler = CommandHandler('skip', skip_video)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        GENDER: [gender_handler],
        PHOTO: [photo_handler, skip_photo_handler],
        BIO: [bio_handler, skip_bio_handler],
        VIDEO: [video_handler, skip_video_handler],
    }, fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()