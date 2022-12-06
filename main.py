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
    [InlineKeyboardButton("Шутка!", callback_data='1'), InlineKeyboardButton("Анекдот", callback_data='2'),
     InlineKeyboardButton("История", callback_data='3')],
    [InlineKeyboardButton("Игральная кость", callback_data='4')],
    [InlineKeyboardButton("Животное", callback_data='5')],
    [InlineKeyboardButton("Оцени бота!", callback_data='RW_GET')]]
keyboard2 = [
    [InlineKeyboardButton("Старт!", callback_data='1_1'), InlineKeyboardButton("Инфа.", callback_data='2_1')],
    [InlineKeyboardButton("Команды", callback_data='3_1')],
    [InlineKeyboardButton("Оцени бота!", callback_data='RW_GET')]]
rwkb = [
    [InlineKeyboardButton("Да!", callback_data='RW_Y')],
    [InlineKeyboardButton("Нет!", callback_data='RW_N')]]
name = "Алиса"
list_greeting = ['Hi, ', "Привет, ", "Ку, ", "Привет друг, ", "Привет, как дела? ", "Привет, Хозяин! "]


def loggerprintAZ(current_datetime, update=0, context=None):
    if update == 0:
        get = f'Day {current_datetime.day}', str(current_datetime.hour) + ':' + str(
            current_datetime.minute) + ':' + str(current_datetime.second)
    else:
        get = str(update.message.from_user['username']), f'Day {current_datetime.day}', str(
            current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second)
    return str(get)


def write_to_log(update, log=None, context=None):
    wall = open('log.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(str(update.message.from_user['username']) + ": " + str(log) + '\n')
    wall.close()


def write_to_logb(update, log=None, context=None):
    wall = open('log.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(str(log) + '\n')
    wall.close()


def write_rewiev(update, log, context=None):
    wall = open('rw.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(log + '\n')
    wall.close()

anikdots = [
    'Маньяк опрыскал деньги ядом и пожертвовал их детскому дому. Погибло двадцать депутатов, два мэра и один министр. Дети не пострадали.',
    '— Вовочка, ты вот написал в своём сочинении, что тебе нравится мальчик из нашего класса и он даже поцеловал тебя, скажи, это правда? \nИ тут Вовочка вдруг понял как опасно списывать у Машеньки!',
    "Новый учитель, придя в класс, обнаружил, что одного мальчика дразнят Мойше-дурачок. На перемене он спросил ребят, почему они его так обзывают. \n — Да он и вправду дурачок, господин учитель. Если дать ему большую монету в пять шекелей и маленькую в десять, он выберет пять, потому что думает, что она больше. Вот, смотрите... \n Парень достает две монеты и предлагает Мойше выбрать. Тот, как всегда, выбирает пять. Учитель с удивлением спращивает: \n — Почему же ты выбрал монету в пять шекелей, а не в десять? \n — Посмотрите, она же больше, господин учитель! \n После уроков учитель подошел к Мойше. \n — Неужели ты не понимаешь, что пять шекелей больше только по размерам, но на десять шекелей можно купить больше? \n — Конечно понимаю, госпосдин учитель. \n — Так почему же ты выбираешь пять? \n — Потому что, если я выберу десять, они перестанут давать мне деньги!",
    'Когда рухнул "Железный занавес", в каждой квартире граждан бывшего СССР появилась железная дверь.',
    'У нас на работе четкое разделение труда: одни много работают, другие много получают. И главное, никакой путаницы.',
    'Зачем депутатам зарплата в 800 тысяч, если они утверждают, что можно запросто прожить на 7 тысяч рублей?',
    "Модернизация по нашему — это когда лампочки стоят в пять раз дороже сэкономленной ими электроэнергии.",
    'Злые языки утверждают, что у кассы казино в Монако появилось объявление на русском языке:\nГерои труда России обслуживаются в порядке общей очереди.',
    'Мой муж — пилот, графика работы никакого нет, рейсы в любое время дня и ночи (чаще ночи), а у меня стандартная пятидневка 9-18. Всегда встаю поцеловать его и помахать в окошко. Стою в коридоре заспанная, на голове творческий беспорядок, кутаюсь в толстый махровый халат, с таким же взлохмаченным и сонным котом на руках - чучундра, в общем, та ещё). А он недавно сказал, что именно в эти моменты особенно сильно понимает, как любит меня.',
    'Будьте как погода... Ей абсолютно всё равно, нравится она кому-то или нет!',
    '- А можно я с пары уйду?\n- Иди, если надо.\n- А Вы отмечать не будете?\n- Я на работе не пью.',
    'Авторадио провело розыгрыш на лучший ответ: "Кто носит три носка?"\nСреди ответов, которые преимущественно сводились к "чернобыльцы", победителем стала девочка - "Моя бабушка. У неё правая нога мерзнет".']
storys = [
    '''О женской логике.\nНелёгкая судьба металлургов занесла нас однажды в Казахстан, в город Темиртау.\nПоселились мы в гостинице "Steel", которая курировалась местным меткомбинатом. Столовались, естественно, там же, в ресторане при гостинице.\nКаждый ужин, на протяжении трёх дней, Андрей заказывал себе грибной бульон с пампушками. Очень его нахваливал, но мы с Серёгой, попав в оазис казахской и индийской кухни, систематически Андрюху игнорировали. Наконец, на четвертый день мы, таки, решили попробовать это чудо казахской кулинарии. Хлебнув по паре ложек, мы встретились друг с другом глазами.\n- Кубик - заключил Сергей.\n- Мивина, однозначно, согласился я.\nМимо нас как раз пробегала официантка.\n- Девушка, можно вас на минутку?\nСимпатичная казашка остановилась перед нашим столом.\n- Скажите, пожалуйста, а этот бульон из кубиков? - взял быка за рога Серёга.\nДевушка попыталась расширить свои неширокие глаза.\n-Да! Правда, вкусно?\n- Да просто офигенно за три с половиной евро - грустно ответил Сергей.\nВесь вечер, пока не разошлись по номерам, мы стебались над Андреем. По-моему, он даже на нас слегка обиделся. И при вечернем созвоне с жёнами, мы не забыли упомянуть этот вопиющий случай.\nУтром мы встретились с Серёгой в курилке. Андрей зашёл чуть позже и нарвался на наши самые искренние извинения. Ожидая от двух матёрых инженеров любого подвоха, Андрюха потребовал объяснений.\n- Понимаешь в чем дело, мы же вчера с женами вечером общались, ну и рассказали про твой бульончик.\n- Ну и что? - напрягся Андрей.\n- Ничего. Просто наши жены, независимо друг от друга, ответили одно и то же.\n- Ну? Что ответили-то?\n- Да сказали, что мы придурки, и, если, человек прожил на свете тридцать с лихером лет и никогда до сих пор не ел эту хрень, то над ним не смеяться - ему завидовать надо!''',
    '''Объявление в газете, бесплатной, в почтовом ящике, требования к кандидату написаны с меня, подробности при встрече. Офис небольшой, в промышленной зоне, принимает коммерческий директор, расспрашивает о знаниях в области абразивных камней, охлаждающей жидкости, отвечаю складно и впопад.\n- Дождёмся генерального, поговорите с ним.\nСпустя полчаса генеральный приглашает к себе в кабинет, коммерческий излагает суть нашего общения, вопрос ко мне:\n- Пьёте?\nВ голове мысли разные, но отвечаю так:\n- Конечно же, нет. Ну, может быть, иногда, и то по праздникам.\nВопрос уточняется:\n- Можете ли вы пить, не теряя головы и самообладания, и, желательно, долго не пьянея?\n- ?!\n- Понимаете, специфика нашего бизнеса подразумевает продажу абразивных камней, и всего, что с ними связано, на крупнейшие предприятия. Так как рынок уже занят, работаем напрямую с главными инженерами этих заводов. Вы приглашаете на презентацию нашей продукции того же главного инженера в ресторан. Задача - перепить собеседника, и, как результат, наша продукция используется на заводе. Все расходы, подарки жене и так далее за наш счёт. У нас сейчас просто кризис, один сотрудник в запое, другой под капельницей, третий собрался увольняться...''',
    '''Бабушка водится с ребёнком. Мелкому 3 месяца от роду. Лежит на развивающем коврике, над ним висят игрушки-погремушки, в том числе - жираф. Бабушка лежит рядом с внуком, теребит жирафа и приговаривает (я слушаю из соседней комнаты):\n- Вот идёт жирафчик, он живёт в Африке. На жирафчике едут бедуины, везут контрабанду с этой... как его... марихуаной! Продадут они марихуану, купят игрушки своим деткам. Вот едут они, едут, приехали на границу. Поймали пограничники бедуинов, груз забрали, а их... расстреляли! Теперь пограничники сами марихуану будут продавать и своим деткам игрушки покупать.\nМожет, зря мы бабушке новый телек подарили?''',
    '''На аукционе в Лондоне продавали с молотка первое издание партитуры одного из ранних балетов Стравинского.\nЖелающих приобрести эту редкостную вещь было много, но один из присутствующих – какой-то старый седой господин – все время набавлял цену.\nНаконец, партитура, действительно, досталась ему за три тысячи фунтов стерлингов.\nРепортеры окружили нового собственника партитуры.\n– Игорь Стравинский, – отрекомендовался он журналистам и добавил: – Я никогда не представлял себе, что за собственную партитуру придется платить вдвое больше того, что когда-то в молодости я получил за весь балет!''',
    '''У меня еще под вечер пошел дождь, который потом превратился в снег.\nКотюнчик сидит дома, и протяжно мяукает. К нему подбежишь, он сразу к выходной двери, и снова: "мурр-мяу", и на тебя глядит. Дверь откроешь: "ну, беги, дескать, если так хочешь" - отходит внутрь. Через пять минут снова мяучит свое жалобное.\nТакое ощущение, что он требует, чтобы я ему отключил снег и создал благоприятные условия на улице.\nВот неужели он в наше всемогущество настолько поверил?\nДаже неловко как-то перед ним, и не объяснишь ведь, что выключить свет и погоду - это разные вещи.\nЭх...''',
    '''3 мая 1945 года рота капитана Л. Никсона (506-й парашютный полк 101–й дивизии ВДВ США) вошла без боя в городок Оберзальцберг, где находились загородные резиденции верхушки Третьего Рейха - Бормана, Геринга, Гиммлера. Прежде чем подоспела военная полиция, бравые десантники вывезли к себе в расположение части пять грузовиков элитного алкоголя (может, они вывезли чего ещё, но это не доказано).\nИ немедленно выпили. Стоимость спиртного подсчитали уже потом, по пустым бутылкам.\nУтро 4 мая вошло в историю американской армии как "Похмелье на миллион долларов".''',
    '''Слово опера по-армянски звучит так же, как и во многих других языках – опера.\nОднако многие ереванцы думают, что это армянское слово и оно требует перевода.  \nУбедился в этом, наблюдая сцену в маршрутке.\nВодитель на вопросы пассажиров о конечной всем отвечает:\n— Опера.\nНа остановке в боковое окно просовывается симпатичное славянское личико и по-русски интересуется тем же.\nВодила после небольшой паузы выдает, как ему кажется, на русском:\n— Опер!''',
    '''Отрицательной чертой, приписываемой туристам, был вандализм. Сведения о разграблении памятников туристами неоднократно отмечались современниками. Известный адвокат А.Ф.Кони, описывая Дворец правосудия в Париже, вспоминал:\n"В этой комнате устроена в настоящее время скромная часовня, стены которой пришлось выкрасить темной масляной краской, во избежание тех надписей, которыми туристы хотят связать свои ничтожные имена с местами, где разыгрывались исторические события. Пришлось унести из этой комнаты и кресло королевы, чтобы спасти его остатки от тех же туристов, бессмысленно вырезавших из него кусочки себе на память".''',
    '''Было вчера.\nСижу дома, никого не трогаю, починяю примус.\nЗаваливает младшенький , и с порога старшему: "А ты не знаешь, кто Марка убил"?\nЯ знаю, что у старшего был одноклассник Марк, думаю, что вообще гопота местная берега попутала.\nМаму этого Марка знаю, речь уже скорбную сложил, чтобы позвонить ей, посочувствовать.\nСука, как меня только дёрнуло подробности спросить...\nОт жеж жопа была бы. Оказалось, что тот сраный Марк - это персонаж онлайн игры.\nНу как так-то, а?''']
comands = '''
/start - - Старт!
/info - - Инфа
/roll - - Бросок игральной кости
/anekdot - - Расскажу анекдот
/story - - Расскажу историю
/animal - - Рандомный зверь
/commands - - Все команды.
/joke - - Шутка!
/translate - (слово) - перевод
/set_timer - (секунды) - таймер
/count - (текст с пробелами!) - счётчик слов
/cancel - - Отменить.
/review - - Отзыв!
/wiki - (что искать?) - поиск в Вики'''
jokes = [
    'О ПАССАЖИРАХ С НИЗКИМ РЕЙТИНГОМ\nЦитата: «Идея неплохая. К людям с хорошим рейтингом приезжают водители с хорошим рейтингом. Согласитесь, в эту сторону идея работает. Она абсолютно не работает в обратную сторону. Получается, к людям с плохим рейтингом приезжают водители с плохим рейтингом. То есть прямо сейчас где-то по Санкт-Петербургу ублюдок едет за ублюдком. Они оба очень злые, потому что у них в телефонах написано, что они ублюдки. И „Яндекс“ думает, что из этого получится что-то хорошее».',
    'О СПАЛЬНЫХ РАЙОНАХ И ГОТИКЕ\nЦитата: «Кто живёт в некрасивых домах? Похлопайте, пожалуйста. Просто я недавно задумался, что если положить фотографии всех мест, где я провёл большую часть своей жизни… Фотографию моего дома, фотографию школы, института. Если вот так в ряд положить, это очень похоже на тот момент в фильме, знаете, когда детектив понимает, почему герой стал серийным убийцей: „А, оказывается, у тебя не было выбора! Ты должен был стать серийным убийцей, больше никем ты не мог стать!“\nМне нравится готика, готические соборы. И я недавно узнал одно из главных правил построения готики: рядом с готическим собором ты должен чувствовать себя ничтожеством. Потому что готический собор настолько возвышенный и прекрасный. И я подумал, что с моим домом это тоже работает. Я тоже чувствую себя ничтожеством, но только потому, что это мой дом».',
    'О ПРОФЕССИИ ПРОТАПТЫВАТЕЛЯ ДОРОЖЕК\nЦитата: «Я нашла в интернете вакансию „протаптыватель тропинок“. Для благоустройства экопарка требуется персонал для создания тропинок естественного происхождения. Абсолютная правда. Зарплата от 35 до 50 тысяч рублей, обучение бесплатное, на месте. Думаю, самое короткое обучение. Просто идите! Вряд ли там говорят „забудьте всё, чему вас учили в школе, институте“. \nНо главное, вакансия не просто есть, она „освободилась“! Интересно, что случилось с предыдущим сотрудником? Думаю, вряд ли он ушёл сам. Стоптал ноги до колена или протоптал тропинку не туда? Я сразу представила его разговор с начальником. Он сидит, и начальник ему говорит: „Мне кажется, вы топчетесь на одном месте. Я вас увольняю, уходите“. А он такой: „Я не пойду, я не на работе!“».',
    'ОБ АРХИТЕКТУРЕ ТЕЛЬ-АВИВА\nЦитата: «Когда играешь в компьютерную игру и у тебя комп слабый, ты ставишь настройки графики на минимум. И все здания — чисто геометрические фигуры без каких-либо текстур, теней, освещения.\nИ точно так же, когда ты находишься в Израиле. Смотришь по сторонам — и такой: „Где детали?“. Я не могу. Я жил всю жизнь в архитектуре европейской. Добавьте деталей! Хочется выйти на улицу и крикнуть: „Где гаргульи? Поставьте гаргулий уже, в конце-то концов! Где узоры? Можете сделать узоры? Это сталинка? Это не сталинка! Мы в центре, должны быть сталинки!“».',
    'О КУЛЬТУРНОМ ДОСУГЕ И «МАКДОНАЛДСЕ»\nЦитата: «Знаете этот момент, когда к вам приезжает друг из другого города и просит показать ему город? И вы показываете ему места, в которых сами не были никогда. Типа: Москва — это Третьяковка. И вы идёте в Третьяковку, и ты не можешь найти вход, потому что там несколько зданий.\nМосквичам вообще плевать на места. Ну, они не в курсе ничего. У меня подруга живёт в Тюмени, она знает больше про Москву. Она как-то прилетела, мы встретились, и она говорит: „Куда пойдём?“ Я задумался, а она такая: „Сейчас в Москве Дни японской культуры, можно туда. А потом — вечеринка-сет разных диджеев из разных стран. Можно туда“. И я такой: „А потом — в "Макдоналдс"!».',
    'О БЕЛЬЕ В ПОЕЗДАХ И О ПРОВОДНИЦАХ\nЦитата: «Вы вообще знали, что мы не обязаны сдавать бельё проводницам? Похлопайте, кто знал! А чё вы не рассказали остальным? Мы живём в страхе. Я вообще не понимаю, каким образом это работает, потому что они приходят такие: „Сдаём бельё, через семь часов приезжаем“. Ну, там же пространственно-временной континуум тоже у них сломался почему-то. И ты такой: „Да, госпожа, пожалуйста, заберите, не трогайте меня“.\nЯ, значит, сел на эту тахту расстеленную, сижу и думаю: „Сейчас ты получишь у меня, конечно! Давай, заходи, я информацию знаю“. Вооружён, как говорится. Она заходит и говорит: „Молодой человек, бельё сдаём“. Я говорю: „Тебе надо, ты и забирай!“\nВы бы видели! У неё башка закрутилась, как у демона, типа: „А-а-а-а! Откуда ты знаешь?“ Она поползла по потолку, клянусь, к своим подругам: „Нам надо убить его, он всем расскажет!“».', ]
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
        context.bot.send_message(update.effective_chat.id, "Пока что этого нет!!")


button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)


def write_to_txt_log(update, log, context=None):
    wall = open('log.txt.txt', 'a')
    # for arg in context.args:
    #    result += arg + ' '
    wall.write(str(update.message.from_user['username']) + ": " + log + '\n')
    wall.close()


def start(update, context):  # старт
    current_datetime = datetime.now()
    chat = update.effective_chat.id
    context.bot.send_message(update.effective_chat.id, list_greeting[
        random.randint(0, len(list_greeting) - 1)] + " Меня зовут " + name + "! Команды /commands",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    print('start ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'start' + loggerprintAZ(current_datetime, update, context), context)


def info(update, context):  # инфа
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, f"Меня зовут {name}! Меня создал AlexZapl!",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    print('info ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'info' + loggerprintAZ(current_datetime, update, context), context)


def startb(update, context):  # старт
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, list_greeting[
        random.randint(0, len(list_greeting) - 1)] + " Меня зовут " + name + "! Команды /commands",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    write_to_logb(f"start ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def infob(update, context):  # инфа
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, f"Меня зовут {name}! Меня создал AlexZapl!",
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    write_to_logb(f"info ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def message(update, context):  # ответ
    current_datetime = datetime.now()
    en = Translator(from_lang='ru', to_lang="en")
    ru = Translator(to_lang="ru")
    note = ''
    for arg in context.args:
        note += arg + ' '
    if note == '' or note == None:
        context.bot.send_message(update.effective_chat.id, 'Нельзя переводить ничего!')
        return
    print('\n\n', note)
    en_trans = en.translate(note)
    ru_trans = ru.translate(note)
    # print(f'Перевод на английский: {en_trans}, На русский: {ru_trans}')
    print(f'Перевод на английский: {en_trans}')
    # context.bot.send_message(update.effective_chat.id, f'Перевод на английский: {en_trans}, На русский: {ru_trans}')
    context.bot.send_message(update.effective_chat.id, f'Перевод на английский: {en_trans}')
    print('translate ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), '\n')
    write_to_log(update, 'translate' + loggerprintAZ(current_datetime, update, context) + f'Text: {note}', context)


def mess(update, context):  # лог
    current_datetime = datetime.now()
    text = update.message.text
    write_to_txt_log(update, 'Text' + loggerprintAZ(current_datetime, update, context) + f'Text: {text}', context)
    print('mess ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), f'Text: {text}')


def roll(update, context):  # игральная кость
    current_datetime = datetime.now()
    bot.send_animation(update.effective_chat.id,
                       'https://www.gifki.org/data/media/710/igralnaya-kost-animatsionnaya-kartinka-0079.gif', None,
                       'Text')
    time.sleep(0.5)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Выпало число {random.randint(1, 6)}!')
    print('roll ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'roll' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('Ещё интересное!', reply_markup=InlineKeyboardMarkup(keyboard))


def anikdot(update, context):  # аникдот
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{anikdots[random.randint(0, len(anikdots) - 1)]}')
    print('anekdot ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'anekdot' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('Ещё интересное!', reply_markup=InlineKeyboardMarkup(keyboard))


def story(update, context):  # история
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{storys[random.randint(0, len(storys) - 1)]}')
    print('story ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'story' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('Ещё интересное!', reply_markup=InlineKeyboardMarkup(keyboard))


def rollb(update, context):  # игральная кость
    current_datetime = datetime.now()
    bot.send_animation(update.effective_chat.id,
                       'https://www.gifki.org/data/media/710/igralnaya-kost-animatsionnaya-kartinka-0079.gif', None,
                       'Text')
    time.sleep(0.5)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Выпало число {random.randint(1, 6)}!',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(f"roll ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def anikdotb(update, context):  # аникдот
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{anikdots[random.randint(0, len(anikdots) - 1)]}',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(f"anekdot ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def storyb(update, context):  # история
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{storys[random.randint(0, len(storys) - 1)]}',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(f"story ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def cmd(update, context):  # команды
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=comands)
    print('commands ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'commands' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('Интересное:', reply_markup=InlineKeyboardMarkup(keyboard))
    update.message.reply_text('Штучки!:', reply_markup=InlineKeyboardMarkup(keyboard2))


def cmdb(update, context):  # команды
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=comands)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Интересное:',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    context.bot.send_message(chat_id=update.effective_chat.id, text='Штучки!:',
                             reply_markup=InlineKeyboardMarkup(keyboard2))
    write_to_logb(f"commands ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def animal(update, context):  # текст-вопросы
    current_datetime = datetime.now()

    animls = ''
    for arg in context.args:
        animls += arg + ' '
        break
    if animls == '':
        animls = 1
    else:
        animls = int(animls)

    print(f'animals {animls}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context), 'Старт')
    write_to_log(update, f'animals {animls}' + loggerprintAZ(current_datetime, update, context), context)
    for i in range(1, animls + 1):
        rand = random.randint(1, 7)
        if rand == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это кот/кошка!')
            https2 = str(SRA.Img.cat())
        elif rand == 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это собака!')
            https2 = str(SRA.Img.dog())
        elif rand == 3:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это панда!')
            https2 = str(SRA.Img.panda())
        elif rand == 4:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это красная панда!')
            https2 = str(SRA.Img.red_panda())
        elif rand == 5:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это птичка!')
            https2 = str(SRA.Img.birb())
        elif rand == 6:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это лиса!')
            https2 = str(SRA.Img.fox())
        elif rand == 7:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это коала!')
            https2 = str(SRA.Img.koala())
        https3 = https2[10:]
        https = https3[:-2]
        print(f'animals {animls}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context),
              f'\n{i}/{animls} : {https}')
        bot.send_photo(update.effective_chat.id, https)
    if animls == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Если было мало можешь написать /animal (количество). Например /animal 5')
    update.message.reply_text('Ещё интересное!', reply_markup=InlineKeyboardMarkup(keyboard))


def animalb(update, context):  # текст-вопросы
    current_datetime = datetime.now()

    animls = 1

    for i in range(1, animls + 1):
        rand = random.randint(1, 7)
        if rand == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это кот/кошка!')
            https2 = str(SRA.Img.cat())
        elif rand == 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это собака!')
            https2 = str(SRA.Img.dog())
        elif rand == 3:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это панда!')
            https2 = str(SRA.Img.panda())
        elif rand == 4:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это красная панда!')
            https2 = str(SRA.Img.red_panda())
        elif rand == 5:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это птичка!')
            https2 = str(SRA.Img.birb())
        elif rand == 6:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это лиса!')
            https2 = str(SRA.Img.fox())
        elif rand == 7:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Милашка, это коала!')
            https2 = str(SRA.Img.koala())
        https3 = https2[10:]
        https = https3[:-2]
        print(
            f"animal ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}') \n{i}/{animls} : {https}")
        write_to_logb(f"animal ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}') \n{i}/{animls} : {https}")
        bot.send_photo(update.effective_chat.id, https, reply_markup=InlineKeyboardMarkup(keyboard))


def joke(update, context):  # команды
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{jokes[random.randint(0, len(jokes) - 1)]}')
    print('joke ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'joke' + loggerprintAZ(current_datetime, update, context), context)
    update.message.reply_text('Ещё интересное!', reply_markup=InlineKeyboardMarkup(keyboard))


def jokeb(update, context):  # команды
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{jokes[random.randint(0, len(jokes) - 1)]}',
                             reply_markup=InlineKeyboardMarkup(keyboard))
    write_to_logb(f"joke ('?', 'Day {current_datetime.day}', {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}')")


def alarm(context):
    current_datetime = datetime.now()
    job = context.job
    context.bot.send_message(job.context, 'ДЗЗЗЫНЬ! Время прошло!')


def set_timer(update, context):
    current_datetime = datetime.now()
    due = ''
    for arg in context.args:
        due += arg + ' '
        break
    if due == '' or due == None:
        context.bot.send_message(update.effective_chat.id, 'Нельзя ставить пустой таймер!')
        return
    due = int(due)
    if due < 0:
        context.bot.send_message(update.effective_chat.id, 'Нельзя ставить таймер меньше 0 секунд!')
        return
    context.job_queue.run_once(alarm, due, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, f'Таймер установлен на {due} секунд')
    print(f'timer {due}', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, f'timer {due}' + loggerprintAZ(current_datetime, update, context), context)


def counter(update, context):
    current_datetime = datetime.now()
    text = str(context.args)
    text2 = text.split(" ")
    lenned = len(text2)
    print(f'\n\n {text} \n {text2}')
    print(lenned, 'words         ', loggerprintAZ(current_datetime, update, context), '\n')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Тут {lenned} слова!")
    write_to_log(update, f'len' + loggerprintAZ(current_datetime, update, context) + f'Text: {text}', context)


def quiz(update, context):
    context.bot.send_message(update.effective_chat.id, 'Понравился бот?', reply_markup=InlineKeyboardMarkup(rwkb))


def rwY(update, context):
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, 'Спасибо!')
    write_rewiev(update,
                 f'(Day {current_datetime.day} {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}) Text: Yes',
                 context)


def rwN(update, context):
    current_datetime = datetime.now()
    context.bot.send_message(update.effective_chat.id, 'Жаль :(')
    write_rewiev(update,
                 f'(Day {current_datetime.day} {current_datetime.hour}:{current_datetime.minute}:{current_datetime.second}) Text: No',
                 context)


def wiki(update, context):
    current_datetime = datetime.now()
    if context.args[0] == "" or context.args[0] == None:
        print('Нельзя отправить ничего!')
    else:
        wikipedia.set_lang("ru")
        context.bot.send_message(update.effective_chat.id, "Русский язык:")
        for i in range(0, 1):
            # проверим выводом в консоль, что мы получаем запросом, потом можно закомментировать или удалить
            print('wiki ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context),
                  f"Args: {context.args[0]}")
            write_to_log(update, 'wiki' + loggerprintAZ(current_datetime, update, context) + f"Args: {context.args[0]}",
                         context)

            path = fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\wiki\RU\{context.args[0]}_find_result.txt"

            # получить резюме страницы найденной по запросу
            in_file = wikipedia.summary(context.args[0])
            # открываем файл для записи найденного результата
            file_wiki = open(path, 'w', encoding="utf-8")
            file_wiki.write(f'{context.args[0]}\n=====================\n{in_file}')
            file_wiki.close()
            # получаем первое предложение до точки в найденном материале для вывода в чат
            in_chat = in_file.split(".")[0]
            context.bot.send_message(update.effective_chat.id, in_chat)
            # считываем файл в двоичном формате для отправки полного результат поиска в час в виде файла
            sending_file = open(path, 'rb')
            # отправка файла
            context.bot.send_document(update.effective_chat.id, sending_file)
            sending_file.close()

        wikipedia.set_lang("en")
        context.bot.send_message(update.effective_chat.id, "Англиский язык:")
        for i in range(0, 1):
            path = fr"C:\Users\alexz\PycharmProjects\Kodland M2Y1\M1Y1\Bot\wiki\EN\{context.args[0]}_find_result.txt"

            # получить резюме страницы найденной по запросу
            in_file = wikipedia.summary(context.args[0])
            # открываем файл для записи найденного результата
            file_wiki = open(path, 'w', encoding="utf-8")
            file_wiki.write(f'{context.args[0]}\n=====================\n{in_file}')
            file_wiki.close()
            # получаем первое предложение до точки в найденном материале для вывода в чат
            in_chat = in_file.split(".")[0]
            context.bot.send_message(update.effective_chat.id, in_chat)
            # считываем файл в двоичном формате для отправки полного результат поиска в час в виде файла
            sending_file = open(path, 'rb')
            # отправка файла
            context.bot.send_document(update.effective_chat.id, sending_file)
            sending_file.close()


def unknown(update, context):  # нет команды
    current_datetime = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я не знаю этой команды!")
    print('UNKNOWN ', update.effective_chat.id, loggerprintAZ(current_datetime, update, context))
    write_to_log(update, 'UNKNOWN' + loggerprintAZ(current_datetime, update, context), context)


mess_handler = MessageHandler(Filters.text, mess)  # лог
# dispatcher.add_handler(mess_handler)  # лог
start_handler = CommandHandler('start', start)  # старт
info_handler = CommandHandler('info', info)  # инфа
message_handler = CommandHandler('translate', message)  # текст
unknown_handler = MessageHandler(Filters.command, unknown)  # нет команды
roll_handler = CommandHandler('roll', roll)  # кость
anikdot_handler = CommandHandler('anekdot', anikdot)  # аникдот
story_handler = CommandHandler('story', story)  # история
cmd_handler = CommandHandler('commands', cmd)  # команды
fox_handler = CommandHandler('animal', animal)  # лиса
joke_handler = CommandHandler('joke', joke)  # шутка
set_handler = CommandHandler("set_timer", set_timer)  # таймер
count_handler = CommandHandler('count', counter)  # счетчик слов
dispatcher.add_handler(count_handler)  # счетчик слов
dispatcher.add_handler(set_handler)  # таймер
dispatcher.add_handler(start_handler)  # старт
dispatcher.add_handler(info_handler)  # инфа
dispatcher.add_handler(message_handler)  # текст
dispatcher.add_handler(roll_handler)  # кость
dispatcher.add_handler(anikdot_handler)  # аникдот
dispatcher.add_handler(story_handler)  # история
dispatcher.add_handler(cmd_handler)  # команды
dispatcher.add_handler(fox_handler)  # текст-вопросы
dispatcher.add_handler(joke_handler)  # шутка

quiz_handler = CommandHandler('review', quiz)
dispatcher.add_handler(quiz_handler)

wiki_handler = CommandHandler('wiki', wiki)  # wiki
dispatcher.add_handler(wiki_handler)  # wiki

dispatcher.add_handler(unknown_handler)  # нет команды

updater.start_polling()
updater.idle()
