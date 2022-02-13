# -*- coding: cp1251 -*-
import random
import time
from datetime import datetime

import SomeRandomAPI as SRA
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from translate import Translator

from credits import *

# test.networktts()
# test.network()
name = "�����"
list_greeting = ['Hi, ', "������, ", "��, ", "������ ����, ", "������, ��� ����? ", "������, ������! "]
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
comands = '/start /info /roll /anikdot /story /animal /joke /translate /set_timer /count /commands'
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


def loggerprintAZ(current_datetime, update=None, context=None):
    if update == None:
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


def start(update, context):  # �����
    current_datetime = datetime.now()
    chat = update.effective_chat.id
    context.bot.send_message(update.effective_chat.id, list_greeting[
        random.randint(0, len(list_greeting) - 1)] + " ���� ����� " + name + "! ������� /commands")
    print('start ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'start' + loggerprintAZ(current_datetime, update, context), context)


def info(update, context):  # ����
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, f"���� ����� {name}! ���� ������ AlexZapl!")
    print('info ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'info' + loggerprintAZ(current_datetime, update, context), context)


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


def roll(update, context):  # ��������� �����
    current_datetime = datetime.now()
    bot.send_animation(update.effective_chat.id,
                       'https://www.gifki.org/data/media/710/igralnaya-kost-animatsionnaya-kartinka-0079.gif', None,
                       'Text')
    time.sleep(0.5)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'������ ����� {random.randint(1, 6)}!')
    print('roll ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'roll' + loggerprintAZ(current_datetime, update, context), context)


def anikdot(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{anikdots[random.randint(0, len(anikdots) - 1)]}')
    print('anikdot ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'anikdot/' + loggerprintAZ(current_datetime, update, context), context)


def story(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{storys[random.randint(0, len(storys) - 1)]}')
    print('story ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'story' + loggerprintAZ(current_datetime, update, context), context)


def cmd(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=comands)
    print('commands ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'commands' + loggerprintAZ(current_datetime, update, context), context)


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

    print(f'animals {animls}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, f'animals {animls}' + loggerprintAZ(current_datetime, update, context), context)
    for i in range(0, animls):
        rand = random.randint(1, 7)
        if rand == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.cat())
        elif rand == 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.dog())
        elif rand == 3:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.panda())
        elif rand == 4:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.red_panda())
        elif rand == 5:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.birb())
        elif rand == 6:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.fox())
        elif rand == 7:
            context.bot.send_message(chat_id=update.effective_chat.id, text='�������')
            https2 = str(SRA.Img.koala())
        https3 = https2[10:]
        https = https3[:-2]
        bot.send_photo(update.effective_chat.id, https)
    if animls == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='���� ���� ���� ������ �������� /animal (����������). �������� /animal 5')


def joke(update, context):  # �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{jokes[random.randint(0, len(jokes) - 1)]}')
    print('joke ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'joke' + loggerprintAZ(current_datetime, update, context), context)


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


# def close(update, context):
# context.bot.send_message(chat_id=update.effective_chat.id, text=f'�������!', reply_markup=ReplyKeyboardRemove())


def unknown(update, context):  # ��� �������
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text="� �� ���� ���� �������!")
    print('UNKNOWN ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'UNKNOWN' + loggerprintAZ(current_datetime, update, context), context)


start_handler = CommandHandler('start', start)  # �����
info_handler = CommandHandler('info', info)  # ����
message_handler = CommandHandler('translate', message)  # �����
unknown_handler = MessageHandler(Filters.command, unknown)  # ��� �������
roll_handler = CommandHandler('roll', roll)  # �����
anikdot_handler = CommandHandler('anikdot', anikdot)  # �������
story_handler = CommandHandler('story', story)  # �������
cmd_handler = CommandHandler('commands', cmd)  # �������
fox_handler = CommandHandler('animal', animal)  # ����
joke_handler = CommandHandler('joke', joke)  # �����
# close_handler = CommandHandler('close', close)  # close
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

# dispatcher.add_handler(close_handler)  # �����-�������


dispatcher.add_handler(unknown_handler)  # ��� �������

updater.start_polling()
updater.idle()
