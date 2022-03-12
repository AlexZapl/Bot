# -*- coding: cp1251 -*-
from telegram import Bot, Poll
from telegram.ext import Updater, CommandHandler, PollAnswerHandler, PollHandler

NICKNAME = 'AlexZapl'
bot_token = '5268805778:AAHV_sHCDNf0QfJL9JxFB1b3bGCubL0CCwI'

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def poll(update, context):
    questions = ["Отлично", "Очень хорошо", "Неплохо", "Так себе"]
    message = context.bot.send_poll(update.effective_chat.id, "Как ты?", questions, is_anonymous=False,
                                    allows_multiple_answers=True)
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    context.bot_data.update(payload)


def receive_poll_answer(update, context):
    answer = update.poll_answer
    poll_id = answer.poll_id

    context.bot_data[poll_id]["answers"] += 1

    if context.bot_data[poll_id]["answers"] == 3:
        context.bot.stop_poll(
            context.bot_data[poll_id]["chat_id"], context.bot_data[poll_id]["message_id"]
        )






poll_handler = CommandHandler('poll', poll)
receive_poll_answer_handler = PollAnswerHandler(receive_poll_answer)
dispatcher.add_handler(poll_handler)
dispatcher.add_handler(receive_poll_answer_handler)

updater.start_polling()
updater.idle()
