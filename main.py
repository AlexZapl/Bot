# -*- coding: cp1251 -*-
import random
import time
from datetime import datetime

import SomeRandomAPI as SRA
import wikipedia

wikipedia.set_lang("ru")
from PIL import Image, ImageFont, ImageDraw
from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from translate import Translator

from credits import *

# test.networktts()
# test.network()
keyboard = [
    [InlineKeyboardButton("�����!", callback_data='1'), InlineKeyboardButton("�������", callback_data='2'),
     InlineKeyboardButton("�������", callback_data='3')],
    [InlineKeyboardButton("��������� �����", callback_data='4')],
    [InlineKeyboardButton("��������", callback_data='5')],
    [InlineKeyboardButton("������� ���!", callback_data='6')],
    [InlineKeyboardButton("����� ����!", callback_data='RW_GET')]]
keyboard2 = [
    [InlineKeyboardButton("�����!", callback_data='1_1'), InlineKeyboardButton("����.", callback_data='2_1')],
    [InlineKeyboardButton("�������", callback_data='3_1')],
    [InlineKeyboardButton("����� ����!", callback_data='RW_GET')]]
rwkb = [
    [InlineKeyboardButton("��!", callback_data='RW_Y')],
    [InlineKeyboardButton("���!", callback_data='RW_N')]]
name = "�����"
list_greeting = ['Hi, ', "������, ", "��, ", "������ ����, ", "������, ��� ����? ", "������, ������! "]


def loggerprintAZ(current_datetime, update=0, context=None):
    if update == 0:
        get = f'Day {current_datetime.day}', str(current_datetime.hour) + ':' + str(
            current_datetime.minute) + ':' + str(current_datetime.second)
    else:
        get = str(update.message.from_user['username']), f'Day {current_datetime.day}', str(
            current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second)
    return str(get)


def write_to_log(update, log, context=None):
    wall = open('log.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(str(update.message.from_user['username']) + ": " + log + '\n')
    wall.close()

def write_to_logb(update, log, context=None):
    wall = open('log.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(log + '\n')
    wall.close()

def write_rewiev(update, log, context=None):
    wall = open('rw.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(log + '\n')
    wall.close()


class Memes:
    def set_meme_text(username, ts, bs):
        img = Image.open(fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\Meme\{username}_photo.jpg")
        rgb_img = img.convert("RGB")
        title_font = ImageFont.truetype('arial.ttf', 25)
        width, height = rgb_img.size
        meme = ImageDraw.Draw(rgb_img)
        meme.text(((width / 2 - width / 4), height / 4), ts, (0, 0, 0), font=title_font)
        meme.text(((width / 2 - width / 2.5), height - height / 4), bs, (0, 0, 0), font=title_font)
        rgb_img.save(fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\Meme\{username}_meme.jpg")

    PHOTO = 0
    TOP_STRING = 1
    BOT_STRING = 2
    VIDEO = 3

    bot = Bot(token=bot_token)
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    def start(update, context):
        current_datetime = datetime.now()
        context.bot.send_message(update.effective_chat.id, '����� ���������� � ��������� �����! ��������� ����, ����� ������ � ��� ��������!')
        print('Meme! ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
        write_to_log(update, 'Meme!' + loggerprintAZ(current_datetime, update, context), context)
        return 0

    def photo(update, context):
        user = str(update.effective_chat.id) + str(update.message.from_user['username'])
        photo_file = update.message.document.get_file()
        photo_file.download(fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\Meme\{user}_photo.jpg")
        update.message.reply_text(
            '�������! ������ ������ ������� ������� ��� ������� /skip ���� ������ ���������� ���� ���')
        return 1

    def top_string(update, context):
        global top_s
        update.message.reply_text('������ =) � ������ ����� ������ �������.')
        top_s = update.message.text
        return 2

    def skip_top_string(update, context):
        global top_s
        update.message.reply_text('����� ���� ��� ������ ���� �����.')
        top_s = ""
        return 2

    def bottom_string(update, context):
        user = str(update.effective_chat.id) + str(update.message.from_user['username'])
        update.message.reply_text('���� ���������')
        bot_s = update.message.text
        Memes.set_meme_text(user, top_s, bot_s)
        sending_img = open(fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\Meme\{user}_meme.jpg", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img,
                                  reply_markup=InlineKeyboardMarkup(keyboard))
        return ConversationHandler.END

    def cancel(update, context):
        update.message.reply_text('����! ���� �����, ���� �������� ���������!',
                                  reply_markup=InlineKeyboardMarkup(keyboard))
        return ConversationHandler.END

    photo_handler = MessageHandler(Filters.document.category("image"), photo)
    top_string_handler = MessageHandler(Filters.text & ~Filters.command, top_string)
    skip_top_string_handler = CommandHandler('skip', skip_top_string)
    bottom_string_handler = MessageHandler(Filters.text & ~Filters.command, bottom_string)
    cancel_handler = CommandHandler('cancel', cancel)


anikdots = [
    '������ �������� ������ ���� � ����������� �� �������� ����. ������� �������� ���������, ��� ���� � ���� �������. ���� �� ����������.',
    '� �������, �� ��� ������� � ���� ���������, ��� ���� �������� ������� �� ������ ������ � �� ���� ��������� ����, �����, ��� ������? \n� ��� ������� ����� ����� ��� ������ ��������� � ��������!',
    "����� �������, ����� � �����, ���������, ��� ������ �������� ������� �����-�������. �� �������� �� ������� �����, ������ ��� ��� ��� ��������. \n � �� �� � ������� �������, �������� �������. ���� ���� ��� ������� ������ � ���� ������� � ��������� � ������, �� ������� ����, ������ ��� ������, ��� ��� ������. ���, ��������... \n ������ ������� ��� ������ � ���������� ����� �������. ���, ��� ������, �������� ����. ������� � ���������� ����������: \n � ������ �� �� ������ ������ � ���� �������, � �� � ������? \n � ����������, ��� �� ������, �������� �������! \n ����� ������ ������� ������� � �����. \n � ������� �� �� ���������, ��� ���� ������� ������ ������ �� ��������, �� �� ������ ������� ����� ������ ������? \n � ������� �������, ��������� �������. \n � ��� ������ �� �� ��������� ����? \n � ������ ���, ���� � ������ ������, ��� ���������� ������ ��� ������!",
    '����� ������ "�������� �������", � ������ �������� ������� ������� ���� ��������� �������� �����.',
    '� ��� �� ������ ������ ���������� �����: ���� ����� ��������, ������ ����� ��������. � �������, ������� ��������.',
    '����� ��������� �������� � 800 �����, ���� ��� ����������, ��� ����� �������� ������� �� 7 ����� ������?',
    "������������ �� ������ � ��� ����� �������� ����� � ���� ��� ������ ������������� ��� ��������������.",
    '���� ����� ����������, ��� � ����� ������ � ������ ��������� ���������� �� ������� �����:\n����� ����� ������ ������������� � ������� ����� �������.',
    '��� ��� � �����, ������� ������ �������� ���, ����� � ����� ����� ��� � ���� (���� ����), � � ���� ����������� ���������� 9-18. ������ ����� ���������� ��� � �������� � ������. ���� � �������� ���������, �� ������ ���������� ����������, ������� � ������� �������� �����, � ����� �� ������������� � ������ ����� �� ����� - ��������, � �����, �� ���). � �� ������� ������, ��� ������ � ��� ������� �������� ������ ��������, ��� ����� ����.',
    '������ ��� ������... �� ��������� �� �����, �������� ��� ����-�� ��� ���!',
    '- � ����� � � ���� ����?\n- ���, ���� ����.\n- � �� �������� �� ������?\n- � �� ������ �� ���.',
    '��������� ������� �������� �� ������ �����: "��� ����� ��� �����?"\n����� �������, ������� ��������������� ��������� � "�����������", ����������� ����� ������� - "��� �������. � �� ������ ���� �������".']
storys = [
    '''� ������� ������.\n������� ������ ����������� ������� ��� ������� � ���������, � ����� ��������.\n���������� �� � ��������� "Steel", ������� ������������ ������� �������������. �����������, �����������, ��� ��, � ��������� ��� ���������.\n������ ����, �� ���������� ��� ����, ������ ��������� ���� ������� ������ � ����������. ����� ��� ����������, �� �� � ������, ����� � ����� ��������� � ��������� �����, �������������� ������� ������������. �������, �� ��������� ���� ��, ����, ������ ����������� ��� ���� ��������� ���������. ������� �� ���� �����, �� ����������� ���� � ������ �������.\n- ����� - �������� ������.\n- ������, ����������, ���������� �.\n���� ��� ��� ��� ��������� ����������.\n- �������, ����� ��� �� �������?\n����������� ������� ������������ ����� ����� ������.\n- �������, ����������, � ���� ������ �� �������? - ���� ���� �� ���� �����.\n������� ���������� ��������� ���� ��������� �����.\n-��! ������, ������?\n- �� ������ �������� �� ��� � ��������� ���� - ������� ������� ������.\n���� �����, ���� �� ��������� �� �������, �� ��������� ��� �������. ��-�����, �� ���� �� ��� ������ ��������. � ��� �������� ������� � �����, �� �� ������ ��������� ���� �������� ������.\n����� �� ����������� � ������ � �������. ������ ����� ���� ����� � �������� �� ���� ����� ��������� ���������. ������ �� ���� ������ ��������� ������ �������, ������� ���������� ����������.\n- ��������� � ��� ����, �� �� ����� � ������ ������� ��������, �� � ���������� ��� ���� ���������.\n- �� � ���? - �������� ������.\n- ������. ������ ���� ����, ���������� ���� �� �����, �������� ���� � �� ��.\n- ��? ��� ��������-��?\n- �� �������, ��� �� ��������, �, ����, ������� ������ �� ����� �������� � ������� ��� � ������� �� ��� ��� �� �� ��� �����, �� ��� ��� �� �������� - ��� ���������� ����!''',
    '''���������� � ������, ����������, � �������� �����, ���������� � ��������� �������� � ����, ����������� ��� �������. ���� ���������, � ������������ ����, ��������� ������������ ��������, ������������� � ������� � ������� ���������� ������, ����������� ��������, ������� ������� � ������.\n- ������� ������������, ���������� � ���.\n������ ������� ����������� ���������� � ���� � �������, ������������ �������� ���� ������ �������, ������ �� ���:\n- �����?\n� ������ ����� ������, �� ������� ���:\n- ������� ��, ���. ��, ����� ����, ������, � �� �� ����������.\n������ ����������:\n- ������ �� �� ����, �� ����� ������ � �������������, �, ����������, ����� �� ������?\n- ?!\n- ���������, ��������� ������ ������� ������������� ������� ���������� ������, � �����, ��� � ���� �������, �� ���������� �����������. ��� ��� ����� ��� �����, �������� �������� � �������� ���������� ���� �������. �� ����������� �� ����������� ����� ��������� ���� �� �������� �������� � ��������. ������ - �������� �����������, �, ��� ���������, ���� ��������� ������������ �� ������. ��� �������, ������� ���� � ��� ����� �� ��� ����. � ��� ������ ������ ������, ���� ��������� � �����, ������ ��� �����������, ������ �������� �����������...''',
    '''������� ������� � �������. ������� 3 ������ �� ����. ����� �� ����������� �������, ��� ��� ����� �������-����������, � ��� ����� - �����. ������� ����� ����� � ������, ������� ������ � ������������� (� ������ �� �������� �������):\n- ��� ��� ��������, �� ���� � ������. �� ��������� ���� �������, ����� ����������� � ����... ��� ���... ����������! �������� ��� ���������, ����� ������� ����� ������. ��� ���� ���, ����, �������� �� �������. ������� ������������ ��������, ���� �������, � ��... �����������! ������ ������������ ���� ��������� ����� ��������� � ����� ������ ������� ��������.\n�����, ��� �� ������� ����� ����� ��������?''',
    '''�� �������� � ������� ��������� � ������� ������ ������� ��������� ������ �� ������ ������� ������������.\n�������� ���������� ��� ���������� ���� ���� �����, �� ���� �� �������������� � �����-�� ������ ����� �������� � ��� ����� �������� ����.\n�������, ���������, �������������, ��������� ��� �� ��� ������ ������ ����������.\n��������� �������� ������ ������������ ���������.\n� ����� �����������, � ���������������� �� ����������� � �������: � � ������� �� ����������� ����, ��� �� ����������� ��������� �������� ������� ����� ������ ����, ��� �����-�� � ��������� � ������� �� ���� �����!''',
    '''� ���� ��� ��� ����� ����� �����, ������� ����� ����������� � ����.\n�������� ����� ����, � �������� �������. � ���� ���������, �� ����� � �������� �����, � �����: "����-���", � �� ���� ������. ����� ��������: "��, ����, �������, ���� ��� ������" - ������� ������. ����� ���� ����� ����� ������ ���� ��������.\n����� ��������, ��� �� �������, ����� � ��� �������� ���� � ������ ������������� ������� �� �����.\n��� ������� �� � ���� ������������� ��������� �������?\n���� ������� ���-�� ����� ���, � �� ��������� ����, ��� ��������� ���� � ������ - ��� ������ ����.\n��...''',
    '''3 ��� 1945 ���� ���� �������� �. ������� (506-� ���������� ���� 101�� ������� ��� ���) ����� ��� ��� � ������� �������������, ��� ���������� ���������� ���������� �������� �������� ����� - �������, �������, ��������. ������ ��� ��������� ������� �������, ������ ���������� ������� � ���� � ������������ ����� ���� ���������� �������� �������� (�����, ��� ������� ���� ���, �� ��� �� ��������).\n� ���������� ������. ��������� ��������� ���������� ��� �����, �� ������ ��������.\n���� 4 ��� ����� � ������� ������������ ����� ��� "�������� �� ������� ��������".''',
    '''����� ����� ��-�������� ������ ��� ��, ��� � �� ������ ������ ������ � �����.\n������ ������ �������� ������, ��� ��� ��������� ����� � ��� ������� ��������.  \n�������� � ����, �������� ����� � ���������.\n�������� �� ������� ���������� � �������� ���� ��������:\n� �����.\n�� ��������� � ������� ���� ������������� ����������� ���������� ������ � ��-������ ������������ ��� ��.\n������ ����� ��������� ����� ������, ��� ��� �������, �� �������:\n� ����!''',
    '''������������� ������, ������������� ��������, ��� ���������. �������� � ������������ ���������� ��������� ������������ ���������� ��������������. ��������� ������� �.�.����, �������� ������ ���������� � ������, ���������:\n"� ���� ������� �������� � ��������� ����� �������� �������, ����� ������� �������� ��������� ������ �������� �������, �� ��������� ��� ��������, �������� ������� ����� ������� ���� ��������� ����� � �������, ��� ������������� ������������ �������. �������� ������ �� ���� ������� � ������ ��������, ����� ������ ��� ������� �� ��� �� ��������, ������������ ���������� �� ���� ������� ���� �� ������".''',
    '''���� �����.\n���� ����, ������ �� ������, ������� ������.\n���������� ����������� , � � ������ ��������: "� �� �� ������, ��� ����� ����"?\n� ����, ��� � �������� ��� ������������ ����, �����, ��� ������ ������ ������� ������ ��������.\n���� ����� ����� ����, ���� ��� �������� ������, ����� ��������� ��, ���������������.\n����, ��� ���� ������ ������ ����������� ��������...\n�� ��� ���� ���� ��. ���������, ��� ��� ������ ���� - ��� �������� ������ ����.\n�� ��� ���-��, �?''']
comands = '''
/start - - �����!
/info - - ����
/roll - - ������ ��������� �����
/anekdot - - �������� �������
/story - - �������� �������
/animal - - ��������� �����
/commands - - ��� �������.
/joke - - �����!
/translate - (�����) - �������
/set_timer - (�������) - ������
/count - (����� � ���������!) - ������� ����
/meme - - ������ ���!
/cancel - - ��������.
/review - - �����!
/wiki - (��� ������?) - ����� � ����'''
jokes = [
    '� ���������� � ������ ���������\n������: ����� ��������. � ����� � ������� ��������� ��������� �������� � ������� ���������. �����������, � ��� ������� ���� ��������. ��� ��������� �� �������� � �������� �������. ����������, � ����� � ������ ��������� ��������� �������� � ������ ���������. �� ���� ����� ������ ���-�� �� �����-���������� ������� ���� �� ��������. ��� ��� ����� ����, ������ ��� � ��� � ��������� ��������, ��� ��� �������. � ������� ������, ��� �� ����� ��������� ���-�� �������.',
    '� �������� ������� � ������\n������: ���� ���� � ���������� �����? ����������, ����������. ������ � ������� ���������, ��� ���� �������� ���������� ���� ����, ��� � ����� ������� ����� ����� ����� ���������� ����� ����, ���������� �����, ���������. ���� ��� ��� � ��� ��������, ��� ����� ������ �� ��� ������ � ������, ������, ����� �������� ��������, ������ ����� ���� �������� �������: ��, �����������, � ���� �� ���� ������! �� ������ ��� ����� �������� �������, ������ ����� �� �� ��� �����!�\n��� �������� ������, ���������� ������. � � ������� ����� ���� �� ������� ������ ���������� ������: ����� � ���������� ������� �� ������ ����������� ���� ������������. ������ ��� ���������� ����� ��������� ����������� � ����������. � � �������, ��� � ���� ����� ��� ���� ��������. � ���� �������� ���� ������������, �� ������ ������, ��� ��� ��� ���.',
    '� ��������� �������������� �������\n������: �� ����� � ��������� �������� ��������������� ��������. ��� ��������������� �������� ��������� �������� ��� �������� �������� ������������� �������������. ���������� ������. �������� �� 35 �� 50 ����� ������, �������� ����������, �� �����. �����, ����� �������� ��������. ������ �����! ���� �� ��� ������� ��������� ��, ���� ��� ����� � �����, ���������. \n�� �������, �������� �� ������ ����, ��� ��������������! ���������, ��� ��������� � ���������� �����������? �����, ���� �� �� ���� ���. ������� ���� �� ������ ��� ��������� �������� �� ����? � ����� ����������� ��� �������� � �����������. �� �����, � ��������� ��� �������: ���� �������, �� ��������� �� ����� �����. � ��� ��������, �������. � �� �����: �� �� �����, � �� �� ������!��.',
    '�� ����������� ����-�����\n������: ������ ������� � ������������ ���� � � ���� ���� ������, �� ������� ��������� ������� �� �������. � ��� ������ � ����� �������������� ������ ��� �����-���� �������, �����, ���������.\n� ����� ��� ��, ����� �� ���������� � �������. �������� �� �������� � � �����: ���� ������?�. � �� ����. � ��� ��� ����� � ����������� �����������. �������� �������! ������� ����� �� ����� � ��������: ���� ��������? ��������� �������� ���, � �����-�� ������! ��� �����? ������ ������� �����? ��� ��������? ��� �� ��������! �� � ������, ������ ���� ��������!��.',
    '� ���������� ������ � �����������Ż\n������: ������� ���� ������, ����� � ��� ��������� ���� �� ������� ������ � ������ �������� ��� �����? � �� ����������� ��� �����, � ������� ���� �� ���� �������. ����: ������ � ��� �����������. � �� ���� � �����������, � �� �� ������ ����� ����, ������ ��� ��� ��������� ������.\n��������� ������ ������� �� �����. ��, ��� �� � ����� ������. � ���� ������� ���� � ������, ��� ����� ������ ��� ������. ��� ���-�� ���������, �� �����������, � ��� �������: ����� �����?� � ���������, � ��� �����: ������� � ������ ��� �������� ��������, ����� ����. � ����� � ���������-��� ������ ������� �� ������ �����. ����� �����. � � �����: �� ����� � � "����������"!�.',
    '� ����� � ������� � � �����������\n������: ��� ������ �����, ��� �� �� ������� ������� ����� �����������? ����������, ��� ����! � �� �� �� ���������� ���������? �� ���� � ������. � ������ �� �������, ����� ������� ��� ��������, ������ ��� ��� �������� �����: ����� �����, ����� ���� ����� ���������. ��, ��� �� ���������������-��������� ��������� ���� � ��� �������� ������-��. � �� �����: ���, �������, ����������, ��������, �� �������� �����.\n�, ������, ��� �� ��� ����� ������������, ���� � �����: ������� �� �������� � ����, �������! �����, ������, � ���������� �����. �������, ��� ���������. ��� ������� � �������: �������� �������, ����� ����. � ������: ����� ����, �� � �������!�\n�� �� ������! � �� ����� �����������, ��� � ������, ����: ��-�-�-�! ������ �� ������?� ��� �������� �� �������, �������, � ����� ��������: ���� ���� ����� ���, �� ���� ���������!��.', ]
reply_keybord = ['/anikdot', '/story',
                 '/animal']
# markup = ReplyKeyboardMarkup(reply_keybord, one_time_keyboard=False)

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "1":
        jokeb(update, context)
    elif query.data == "2":
        anikdotb(update, context)
    elif query.data == "3":
        storyb(update, context)
    elif query.data == "4":
        rollb(update, context)
    elif query.data == "5":
        animalb(update, context)
    elif query.data == "6":
        Memes.start(update, context)
    elif query.data == '1_1':
        startb(update, context)
    elif query.data == '2_1':
        infob(update, context)
    elif query.data == '3_1':
        cmdb(update, context)
    elif query.data == 'RW_Y':
        rwY(update, context)
    elif query.data == 'RW_N':
        rwN(update, context)
    elif query.data == 'RW_GET':
        quiz(update, context)
    else:
        context.bot.send_message(update.effective_chat.id, "���� ��� ����� ���!!")


button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)


def write_to_txt_log(update, log, context=None):
    wall = open('log.txt.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(str(update.message.from_user['username']) + ": " + log + '\n')
    wall.close()


def start(update, context):  # �����
    current_datetime = datetime.now()
    chat = update.effective_chat.id
    context.bot.send_message(update.effective_chat.id, list_greeting[
        random.randint(0, len(list_greeting) - 1)] + " ���� ����� " + name + "! ������� /commands",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    print('start ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'start' + loggerprintAZ(current_datetime, update, context), context)


def info(update, context):  # ����
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, f"���� ����� {name}! ���� ������ AlexZapl!",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    print('info ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'info' + loggerprintAZ(current_datetime, update, context), context)


def startb(update, context):  # �����
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, list_greeting[
        random.randint(0, len(list_greeting) - 1)] + " ���� ����� " + name + "! ������� /commands",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    write_to_logb(f"start ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def infob(update, context):  # ����
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, f"���� ����� {name}! ���� ������ AlexZapl!",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    write_to_logb(
        f"info ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def message(update, context):  # �����
    current_datetime = datetime.now()
    en = Translator(from_lang='ru', to_lang="en")
    ru = Translator(to_lang="ru")
    note = ''
    for arg in context.args:
        note += arg + ' '
    if note == '' or note == None:
        context.bot.send_message(update.effective_chat.id, '������ ���������� ������!')
        return
    print('\n\n', note)
    en_trans = en.translate(note)
    ru_trans = ru.translate(note)
    # print(f'������� �� ����������: {en_trans}, �� �������: {ru_trans}')
    print(f'������� �� ����������: {en_trans}')
    # context.bot.send_message(update.effective_chat.id, f'������� �� ����������: {en_trans}, �� �������: {ru_trans}')
    context.bot.send_message(update.effective_chat.id, f'������� �� ����������: {en_trans}')
    print('translate ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), '\n')
    write_to_log(update, 'translate' + loggerprintAZ(current_datetime, update, context) + f'Text: {note}', context)


def mess(update, context):  # ���
    current_datetime = datetime.now()
    text = update.message.text
    write_to_txt_log(update, 'Text' + loggerprintAZ(current_datetime, update, context) + f'Text: {text}', context)
    print('mess ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), f'Text: {text}')


def roll(update, context):  # ��������� �����
    current_datetime = datetime.now()
    bot.send_animation(update.effective_chat.id,
                       'https://www.gifki.org/data/media/710/igralnaya-kost-animatsionnaya-kartinka-0079.gif', None,
                       'Text')
    time.sleep(0.5)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'������ ����� {random.randint(1, 6)}!')
    print('roll ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'roll' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('��� ����������!', reply_markup=InlineKeyboardMarkup(keyboard))


def anikdot(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{anikdots[random.randint(0, len(anikdots) - 1)]}')
    print('anekdot ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'anekdot' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('��� ����������!', reply_markup=InlineKeyboardMarkup(keyboard))


def story(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{storys[random.randint(0, len(storys) - 1)]}')
    print('story ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'story' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('��� ����������!', reply_markup=InlineKeyboardMarkup(keyboard))


def rollb(update, context):  # ��������� �����
    current_datetime = datetime.now()
    bot.send_animation(update.effective_chat.id,
                       'https://www.gifki.org/data/media/710/igralnaya-kost-animatsionnaya-kartinka-0079.gif', None,
                       'Text')
    time.sleep(0.5)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'������ ����� {random.randint(1, 6)}!',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(
        f"roll ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def anikdotb(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{anikdots[random.randint(0, len(anikdots) - 1)]}',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(
        f"anekdot ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def storyb(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{storys[random.randint(0, len(storys) - 1)]}',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(
        f"story ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def cmd(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=comands)
    print('commands ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'commands' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('����������:', reply_markup=InlineKeyboardMarkup(keyboard))
    update.message.reply_text('������!:', reply_markup=InlineKeyboardMarkup(keyboard2))


def cmdb(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=comands)
    context.bot.send_message(chat_id=update.effective_chat.id, text='����������:',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    context.bot.send_message(chat_id=update.effective_chat.id, text='������!:',
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    write_to_logb(
        f"commands ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def animal(update, context):  # �����-�������
    current_datetime = datetime.now()

    animls = ''
    for arg in context.args:
        animls += arg + ' '
        break
    if animls == '':
        animls = 1
    else:
        animls = int(animls)

    print(f'animals {animls}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), '�����')
    write_to_log(update, f'animals {animls}' + loggerprintAZ(current_datetime, update, context), context)
    for i in range(1, animls+1):
        rand = random.randint(1, 7)
        if rand == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ���/�����!')
            https2 = str(SRA.Img.cat())
        elif rand == 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ������!')
            https2 = str(SRA.Img.dog())
        elif rand == 3:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� �����!')
            https2 = str(SRA.Img.panda())
        elif rand == 4:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ������� �����!')
            https2 = str(SRA.Img.red_panda())
        elif rand == 5:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ������!')
            https2 = str(SRA.Img.birb())
        elif rand == 6:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ����!')
            https2 = str(SRA.Img.fox())
        elif rand == 7:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� �����!')
            https2 = str(SRA.Img.koala())
        https3 = https2[10:]
        https = https3[:-2]
        print(f'animals {animls}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context),
              f'\n{i}/{animls} : {https}')
        bot.send_photo(update.effective_chat.id, https)
    if animls == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='���� ���� ���� ������ �������� /animal (����������). �������� /animal 5')
    update.message.reply_text('��� ����������!', reply_markup=InlineKeyboardMarkup(keyboard))


def animalb(update, context):  # �����-�������
    current_datetime = datetime.now()

    animls = 1

    for i in range(1, animls + 1):
        rand = random.randint(1, 7)
        if rand == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ���/�����!')
            https2 = str(SRA.Img.cat())
        elif rand == 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ������!')
            https2 = str(SRA.Img.dog())
        elif rand == 3:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� �����!')
            https2 = str(SRA.Img.panda())
        elif rand == 4:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ������� �����!')
            https2 = str(SRA.Img.red_panda())
        elif rand == 5:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ������!')
            https2 = str(SRA.Img.birb())
        elif rand == 6:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� ����!')
            https2 = str(SRA.Img.fox())
        elif rand == 7:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������, ��� �����!')
            https2 = str(SRA.Img.koala())
        https3 = https2[10:]
        https = https3[:-2]
        print(f"animal ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}') \n{i}/{animls} : {https}")
        bot.send_photo(update.effective_chat.id, https, reply_markup=InlineKeyboardMarkup(keyboard))


def joke(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{jokes[random.randint(0, len(jokes) - 1)]}')
    print('joke ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'joke' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('��� ����������!', reply_markup=InlineKeyboardMarkup(keyboard))


def jokeb(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{jokes[random.randint(0, len(jokes) - 1)]}',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(
        f"joke ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def alarm(context):
    current_datetime = datetime.now()
    job = context.job
    context.bot.send_message(job.context, '�������! ����� ������!')


def set_timer(update, context):
    current_datetime = datetime.now()
    due = ''
    for arg in context.args:
        due += arg + ' '
        break
    if due == '' or due == None:
        context.bot.send_message(update.effective_chat.id, '������ ������� ������ ������!')
        return
    due = int(due)
    if due < 0:
        context.bot.send_message(update.effective_chat.id, '������ ������� ������ ������ 0 ������!')
        return
    context.job_queue.run_once(alarm, due, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, f'������ ���������� �� {due} ������')
    print(f'timer {due}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, f'timer {due}' + loggerprintAZ(current_datetime, update, context), context)


def counter(update, context):
    current_datetime = datetime.now()
    text = str(context.args)
    text2 = text.split(" ")
    lenned = len(text2)
    print(f'\n\n {text} \n {text2}')
    print(lenned, 'words         ', loggerprintAZ(current_datetime, update, context), '\n')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"��� {lenned} �����!")
    write_to_log(update, f'len' + loggerprintAZ(current_datetime, update, context) + f'Text: {text}', context)


def quiz(update, context):
    context.bot.send_message(update.effective_chat.id, '���������� ���?', reply_markup=InlineKeyboardMarkup(rwkb))

def rwY(update, context):
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, '�������!')
    write_rewiev(update, f'(Day {current_datetime.day} {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}) Text: Yes', context)


def rwN(update, context):
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, '���� :(')
    write_rewiev(update, f'(Day {current_datetime.day} {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}) Text: No', context)

def wiki(update, context):
    current_datetime = datetime.now()
    if context.args[0] == "" or context.args[0] == None:
        print('������ ��������� ������!')
    else:
        #�������� ������� � �������, ��� �� �������� ��������, ����� ����� ���������������� ��� �������
        print('wiki ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), f"Args: {context.args[0]}")
        write_to_log(update, 'wiki' + loggerprintAZ(current_datetime, update, context) + f"Args: {context.args[0]}", context)

        path = fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\wiki\{context.args[0]}_find_result.txt"

        #�������� ������ �������� ��������� �� �������
        in_file = wikipedia.summary(context.args[0])
        #��������� ���� ��� ������ ���������� ����������
        file_wiki = open(path, 'w', encoding="utf-8")
        file_wiki.write(f'{context.args[0]}\n=====================\n{in_file}')
        file_wiki.close()
        #�������� ������ ����������� �� ����� � ��������� ��������� ��� ������ � ���
        in_chat = in_file.split(".")[0]
        context.bot.send_message(update.effective_chat.id, in_chat)
        #��������� ���� � �������� ������� ��� �������� ������� ��������� ������ � ��� � ���� �����
        sending_file = open(path, 'rb')
        #�������� �����
        context.bot.send_document(update.effective_chat.id, sending_file)
        sending_file.close()

def unknown(update, context):  # ��� �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text="� �� ���� ���� �������!")
    print('UNKNOWN ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'UNKNOWN' + loggerprintAZ(current_datetime, update, context), context)


mess_handler = MessageHandler(Filters.text, mess)  # ���
# dispatcher.add_handler(mess_handler)  # ���
start_handler = CommandHandler('start', start)  # �����
info_handler = CommandHandler('info', info)  # ����
message_handler = CommandHandler('translate', message)  # �����
unknown_handler = MessageHandler(Filters.command, unknown)  # ��� �������
roll_handler = CommandHandler('roll', roll)  # �����
anikdot_handler = CommandHandler('anekdot', anikdot)  # �������
story_handler = CommandHandler('story', story)  # �������
cmd_handler = CommandHandler('commands', cmd)  # �������
fox_handler = CommandHandler('animal', animal)  # ����
joke_handler = CommandHandler('joke', joke)  # �����
set_handler = CommandHandler("set_timer", set_timer)  # ������
count_handler = CommandHandler('count', counter)  # ������� ����
dispatcher.add_handler(count_handler)  # ������� ����
dispatcher.add_handler(set_handler)  # ������
dispatcher.add_handler(start_handler)  # �����
dispatcher.add_handler(info_handler)  # ����
dispatcher.add_handler(message_handler)  # �����
dispatcher.add_handler(roll_handler)  # �����
dispatcher.add_handler(anikdot_handler)  # �������
dispatcher.add_handler(story_handler)  # �������
dispatcher.add_handler(cmd_handler)  # �������
dispatcher.add_handler(fox_handler)  # �����-�������
dispatcher.add_handler(joke_handler)  # �����

meme_start_handler = CommandHandler('meme', Memes.start)

conv_handler = ConversationHandler(
    entry_points=[meme_start_handler],
    states={
        Memes.PHOTO: [Memes.photo_handler],
        Memes.TOP_STRING: [Memes.top_string_handler, Memes.skip_top_string_handler],
        Memes.BOT_STRING: [Memes.bottom_string_handler],
    }, fallbacks=[Memes.cancel_handler])

dispatcher.add_handler(conv_handler)

quiz_handler = CommandHandler('review', quiz)
dispatcher.add_handler(quiz_handler)

wiki_handler = CommandHandler('wiki', wiki)  # wiki
dispatcher.add_handler(wiki_handler)  # wiki

dispatcher.add_handler(unknown_handler)  # ��� �������

updater.start_polling()
updater.idle()
