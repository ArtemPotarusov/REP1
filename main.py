import telebot
from telebot import types
from logging import exception

API_TOKEN = '5692562755:AAHdYZZx-Zc774qePhPaX-S2ReGIl9mPFRA'

bot = telebot.TeleBot(API_TOKEN)


class User:
    def __init__(self, name):
        self.name = name
        self.ans1 = None
        self.ans2 = None
        self.ans3 = None
        self.ans4 = None
        self.ans5 = None
        self.ans6 = None
        self.ans7 = None
        self.k = 0


user_dict = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
    Привет. Я бот по Mass Effect.
Тебе предстоит ответить на 7 вопросов по этой замечательной вселенной.    
Начнём?
Капитан Шепард спрашивает, как тебя зовут?""")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('SW KOTOR', 'Dragon Age', 'Baldurs Gate')
        msg = bot.reply_to(message, """\
        Благодаря какой из этих игр появилась Mass Effect?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_1_step)
    except Exception as e:
        bot.reply_to(message, 'Could u try again?')


def process_1_step(message):
    try:
        chat_id = message.chat.id
        ans1 = message.text
        user = user_dict[chat_id]
        user.ans1 = ans1

        if (ans1 == u'SW KOTOR') or (ans1 == u'Dragon Age') or (ans1 == u'Baldurs Gate'):
            user.ans1 = ans1
            if (ans1 == u'SW KOTOR'):
                user.k += 1

        else:
            raise Exception("Unknown game")
        # bot.send_message(chat_id, "Nice to meet u, " + user.name + '\n Game: ' + user.ans)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Science Fiction X', 'System Shock', 'Neverwinter years')
        msg = bot.reply_to(message, """\
        Как планировали назвать первую часть Mass Effect?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_2_step)


    except Exception as e:
        bot.reply_to(message, 'Could u try again?')


def process_2_step(message):
    try:
        chat_id = message.chat.id
        ans2 = message.text
        user = user_dict[chat_id]
        user.ans2 = ans2
        if (ans2 == u'Science Fiction X') or (ans2 == u'System Shock') or (ans2 == u'Neverwinter years'):
            user.ans2 = ans2
            if (ans2 == u'Science Fiction X'):
                user.k += 1
        else:
            raise Exception("Unknown game")

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Летучие мыши', 'Крокодилы', 'Вараны')
        msg = bot.reply_to(message, """\
        С каких животных создавались кроганы?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_3_step)

    except Exception as e:
        bot.reply_to(message, 'Could u try again?')

def process_3_step(message):
    try:
        chat_id = message.chat.id
        ans3 = message.text
        user = user_dict[chat_id]
        user.ans3 = ans3

        if (ans3 == u'Летучие мыши') or (ans3 == u'Крокодилы') or (ans3 == u'Вараны'):
            user.ans3 = ans3
            if (ans3 == u'Летучие мыши'):
                user.k += 1
        else:
            raise Exception("Unknown game")
        # bot.send_message(chat_id, "Nice to meet u, " + user.name + '\n Game: ' + user.ans)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Клинт Иствуд', 'Марлон Брандо', 'Генри Фонда')
        msg = bot.reply_to(message, """\
        С какого актера рисовали внешность Мордина Солуса?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_4_step)


    except Exception as e:
        bot.reply_to(message, 'Could u try again?')


def process_4_step(message):
    try:
        chat_id = message.chat.id
        ans4 = message.text
        user = user_dict[chat_id]
        user.ans4 = ans4
        if (ans4 == u'Клинт Иствуд') or (ans4 == u'Марлон Брандо') or (ans4 == u'Генри Фонда'):
            user.ans4 = ans4
            if (ans4 == u'Клинт Иствуд'):
                user.k += 1
        else:
            raise Exception("Unknown game")
        # bot.send_message(chat_id, "Nice to meet u, " + user.name + '\n Game: ' + user.ans)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Саларианцы', 'Азари', 'Турианцы')
        msg = bot.reply_to(message, """\
        Какая раса из игры должна была стать самой сексуальной?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_5_step)

    except Exception as e:
        bot.reply_to(message, 'Could u try again?')

def process_5_step(message):
    try:
        chat_id = message.chat.id
        ans5 = message.text
        user = user_dict[chat_id]
        user.ans5 = ans5
        if (ans5 == u'Саларианцы') or (ans5 == u'Азари') or (ans5 == u'Турианцы'):
            user.ans5 = ans5
            if (ans5 == u'Азари'):
                user.k += 1
        else:
            raise Exception("Unknown game")

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Миранда', 'Тали', 'Лиара')
        msg = bot.reply_to(message, """\
        Какая из этих партнерш шепарда принадлежит человеческой расе?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_6_step)

    except Exception as e:
        bot.reply_to(message, 'Could u try again?')


def process_6_step(message):
    try:
        chat_id = message.chat.id
        ans6 = message.text
        user = user_dict[chat_id]
        user.ans6 = ans6

        if (ans6 == u'Миранда') or (ans6 == u'Тали') or (ans6 == u'Лиара'):
            user.ans6 = ans6
            if (ans6 == u'Миранда'):
                user.k += 1
        else:
            raise Exception("Unknown game")
        # bot.send_message(chat_id, "Nice to meet u, " + user.name + '\n Game: ' + user.ans)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Гет', 'Азари', 'Кварианец')
        msg = bot.reply_to(message, """\
        Название этого бота является отсылкой к какому из персонажей?""", reply_markup=markup)
        bot.register_next_step_handler(msg, process_7_step)


    except Exception as e:
        bot.reply_to(message, 'Could u try again?')


def process_7_step(message):
    try:
        chat_id = message.chat.id
        ans7 = message.text
        user = user_dict[chat_id]
        user.ans7 = ans7
        if (ans7 == u'Гет') or (ans7 == u'Азари') or (ans7 == u'Кварианец'):
            user.ans7 = ans7
            if (ans7 == u'Гет'):
                user.k += 1
        else:
            raise Exception("Unknown game")
        bot.send_message(chat_id, "Nice to meet u, " + user.name + '\n Q1: ' + user.ans1
                         + '\n Q2: ' + user.ans2 + '\n Q3: ' + user.ans3
                         + '\n Q4: ' + user.ans4 + '\n Q5: ' + user.ans5 + '\n Q6: ' + user.ans6
                         + '\n Q7: ' + user.ans7 + '\n U have riched ' + str(user.k) + ' of 7')

    except Exception as e:
        bot.reply_to(message, 'Could u try again?')


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()
