from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

NICKNAME = 'AlexZapl'

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
                                              S###S                                


                                                                                ''')

current_datetime = datetime.now()
print('Day', current_datetime.day, '  ',
      str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second))

bot_token = '5268805778:AAHjHzJlQL1es8cbXs2CQFVu5aRPKNTc0hY'
keyboard = [
    [InlineKeyboardButton("Понедельник", callback_data='1'), InlineKeyboardButton("Вторник", callback_data='2')],
    [InlineKeyboardButton("Среда", callback_data='3'), InlineKeyboardButton("Четверг", callback_data='4')],
    [InlineKeyboardButton("Пятница", callback_data='5')]]
bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Это бот для расписания! Ничего не забывай! Доска: /showwall")


def help(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Лишь попроси бота, и он поможет тебе с расписанием и некоторыми предметами!")


def get_data_from_file(day):
    f = open(day, "r", encoding='UTF-8')
    data = f.read()
    f.close()
    return data


def get_data_from_file_n(day):
    f = open(day, "r")
    data = f.read()
    f.close()
    return data


def get_day(update, context):
    update.message.reply_text('Выбери день недели', reply_markup=InlineKeyboardMarkup(keyboard))


def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "1":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("mon.txt"))
    elif query.data == "2":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("tue.txt"))
    elif query.data == "3":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("wed.txt"))
    elif query.data == "4":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("thu.txt"))
    elif query.data == "5":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("fri.txt"))
    else:
        context.bot.send_message(update.effective_chat.id, "Нет такого дня пока что!")


def write_to_wall(update, context):
    if str(update.message.from_user['username']) == NICKNAME:
        wall = open('wall.txt', 'a')
        result = ''
        for arg in context.args:
            result += arg + ' '
        wall.write(str(update.message.from_user['username']) + ": " + result + '\n')
        wall.close()
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f"Ты не {NICKNAME}!")


def show_wall(update, context):
    if str(update.message.from_user['username']) == NICKNAME:
        context.bot.send_message(update.effective_chat.id, get_data_from_file_n("wall.txt"))
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f"Ты не {NICKNAME}!")


def show_log(update, context):
    if str(update.message.from_user['username']) == NICKNAME:
        context.bot.send_message(update.effective_chat.id, get_data_from_file_n("log.txt"))
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f"Ты не {NICKNAME}!")


write_to_wall_handler = CommandHandler('writewall', write_to_wall)
show_wall_handler = CommandHandler('showwall', show_wall)

dispatcher.add_handler(write_to_wall_handler)
dispatcher.add_handler(show_wall_handler)

log_handler = CommandHandler('logs', show_log)
dispatcher.add_handler(log_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

get_day_handler = CommandHandler('getday', get_day)
dispatcher.add_handler(get_day_handler)

button_handler = CallbackQueryHandler(button)
# dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()