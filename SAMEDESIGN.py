import telebot
from telebot import types
import re

token = ('5612181357:AAELwoHnlUrrmJy-al1LtS685Lzg9GcEqpg')     ####
bot = telebot.TeleBot(token)
chat_id = ('1465233793')        ####
#chat_id = ('-810293417')       ####
isorder = bool()
admin_ = (1465233793)
persons_ = [admin_, 985903973, 932623200, 1359616488] #person
isperson = bool()
banlist = [] #banned
isbanned = bool()
orderer = bool()
unban = str()
a = int()
s = str()
language = bool(False) # false = rus, true = eng

ban_vid = open('C:/Users/Стас/source/repos/SAMEDESIGN/SAMEDESIGN/ban.mp4', 'rb')

info_text = str()
info_text_rus = (str(f'<i>Информация.</i>\n\nSAME Design studio\n<b>дизайнер @samexwetus\nхудожник @brrrusher\nверстальщик/кодер @egorgalysko</b>\n<b>владелец бота @kraikos</b>\n\n<b>-Портфолио</b> https://t.me/+4slIEtdaVx42MmE6 \n<b>-Отзывы на LOLZ</b> https://zelenka.guru/threads/4443292/#post-34466943'))
info_text_eng = (str(f'<i>Information.</i>\n\nSAME Design studio\n<b>designer @samexwetus\npainter @brrrusher\nwebsite layout @egorgalysko</b>\n<b>bot owner @kraikos</b>\n\n<b>-Portfolio</b> https://t.me/+4slIEtdaVx42MmE6 \n<b>-Feedback on LOLZ</b> https://zelenka.guru/threads/4443292/#post-34466943'))

order_text = str()
order_text_rus = (str(f'<i>Оформление заказа.</i> \n\nОформление заказа включает в себя некоторые <b>правила:</b> \n\n-В самом начале заказа напишите <b>/order</b> \nНапишите минимальное <b>ТЗ</b>(техническое задание/суть заказа) \n\n-В случае некорректно заполненной информации <b>заказ не принимается!</b> \nВ случае <b>неадекватного</b>поведения (нецензурная брань, спам) вы будете <b>забанены.</b>'))
order_text_eng = (str(f'<i>Making an order.</i> \n\nMaking an order includes some <b>rules:</b> \n\n-At the beginning write <b>/order</b> \n-Write a main <b>task</b> (order description) \n\n-In case of incorrectly filled information  <b>the order will not accepted!</b> \n-In case of <b>unacceptable</b> behaviour (profanity, spam), you will be <b>banned.</b>'))

fin_text = str()
fin_text_rus = (str(f'✅ Заказ <b>успешно</b> оформлен. С Вами <b>скоро свяжутся</b>.'))
fin_text_eng = (str(f'✅ The order has <b>succesfully</b> placed. We will <b>contact with you soon</b>.'))

mainm_text = str()
mainm_text_rus = (str(f'<i>Главное меню.</i>\n<b>Здесь вы можете:</b>\n\n  <b>-Оформить заказ у студии SAME Design</b>\n  <b>-Просмотреть информацию/Оставить отзыв</b>'))
mainm_text_eng = (str(f'<i>Main menu.</i>\n<b>There you can:</b>\n\n  <b>-Place an order by SAME Design studio</b>\n  <b>-Check information/Leave a feedback</b>'))

texts_rus = [f'Оформить заказ', f'Информация', f'Назад', f'Вы не являетесь <u>авторизованным лицом</u>', f'Вы были </b>забанены<b>', f'Change the language', '@']
texts_eng = [f'Place an order', f'Information', f'Back', f'You are not <u>an authorized person.</u>', f'You has been <b>banned</b>', f'Сменить язык', '@']

texts = str([])

def rus():   
    info_text = info_text_rus
    order_text = order_text_rus
    fin_text = fin_text_rus
    mainm_text = mainm_text_rus
    texts = texts_rus

def eng():
    info_text = info_text_eng
    order_text = order_text_eng
    fin_text = fin_text_eng
    mainm_text = mainm_text_eng
    texts = texts_eng

info_text = info_text_rus
order_text = order_text_rus
fin_text = fin_text_rus
mainm_text = mainm_text_rus 
texts = texts_rus

#батоны
rus()
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
button0 = types.KeyboardButton(texts[0])
button1 = types.KeyboardButton(texts[1])
#button2 = types.KeyboardButton(texts[5])
markup.add(button0, button1)

remove = telebot.types.ReplyKeyboardRemove()

cancel = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
button2 = types.KeyboardButton(texts[2])
cancel.add(button2)

#функции

def initb():
    global a
    global banlist
    a = banlist.count('/ban')
    while not(a == 0):
        banlist.remove('/ban')
        a = a - 1
    
    a = 0

    while not(a == len(banlist)):

        banlist[a] = re.sub('[/|b|a|n| ]', '', banlist[a])
        a = a + 1
        if a == len(banlist):
            banlist = list(set(banlist))

@bot.message_handler(commands=['start']) #START
def start(message):
    orderer = False
    isperson = False
    isbanned = False
    start_text = (str(f'<b>Привет {message.from_user.first_name}👋, это бот Same Design - здесь вы можете:</b>\n\n  <b>-Оформить заказ у студии Same Design</b>\n  <b>-Просмотреть информацию/Оставить отзыв</b>'))
    bot.send_message (message.chat.id, start_text, parse_mode = 'html', reply_markup = markup)

def mainm(message):
    orderer = False
    isperson = False
    isbanned = False
    bot.send_message (message.chat.id, mainm_text, parse_mode = 'html', reply_markup = markup)

@bot.message_handler(commands=['ban']) #BAN
def ban(message):
    global isperson
    global banlist
    global a
    for person_ in persons_:
        if message.from_user.id == person_:
            isperson = True
            if isperson == True:
                bot.send_message(message.chat.id, '<u>Аккаунт с этим id заблокирован.</u>', parse_mode = 'html', reply_markup = cancel)
                banlist.append(message.text)

                while not(a == len(banlist)):

                    banlist[a] = re.sub('[/|b|a|n| ]', '', banlist[a])
                    a = a + 1
                if a == len(banlist):
                    banlist = list(set(banlist))

    if isperson == False:
            bot.send_message(message.chat.id, texts[3], parse_mode = 'html')

@bot.message_handler(commands=['banlist']) #BANLIST
def banlist_1(message):
    initb()
    bot.send_message(message.chat.id,'<u>Забаненные аккаунты:</u>\n' + str(banlist), parse_mode = 'html')
    if len(banlist) == 0:
        bot.send_message(message.chat.id,'<u>Забаненные аккаунты:</u>\n empty', parse_mode = 'html')

@bot.message_handler(commands=['unban']) #UNBAN
def unban(message):
    initb()
    global isperson
    global banlist
    global a
    a = 0
    for person_ in persons_:
        if message.from_user.id == person_:
            isperson = True
            if isperson == True:
                unban = re.sub('[/|u|n|b|a|n| ]', '', message.text)
                if len(banlist) > 0:
                    for banned in banlist:
                        print (banned)
                        if unban == banned:
                            banlist.remove(banned)
                            bot.send_message(message.chat.id, '<u>Аккаунт с этим id разблокирован.</u>', parse_mode = 'html', reply_markup = cancel)
                            a = a + 1
                    if a == 0:
                        bot.send_message(message.chat.id, '<u>Этого пользователя нету в /banlist.</u>', parse_mode = 'html', reply_markup = cancel)
                if len(banlist) == 0:
                    bot.send_message(message.chat.id, '<u>Список /banlist пуст.</u>', parse_mode = 'html', reply_markup = cancel)

@bot.message_handler(func=lambda message: message.text == 'Оформить заказ') #ORDER
def order(message):
    global isbanned
    if True:
        for banned in banlist:
            if message.from_user.id == int(banned):    #list of ban
                bot.send_message(message.chat.id, texts[4], parse_mode = 'html')
                bot.send_video(message.chat.id, ban_vid)
                isbanned = True
    if isbanned == False:
        isorder = True
        bot.send_message (message.chat.id, order_text, parse_mode = 'html', reply_markup = cancel)         

@bot.message_handler(commands=['order']) #PSYCHO
def psycho(message):
    #global orderer
    #if message.text == '/order':
        #orderer = True
        #print(orderer)
        #bot.send_message(message.chat.id, 'Извините, <b>пустые заказы не отправляются</b>', parse_mode = 'html', reply_markup = cancel)
    if not(message.text == 'Назад' or 'Back'):
        bot.send_message (chat_id, (f'\n@{message.from_user.username}, {message.from_user.id}:\n '+ message.text, 'utf-8'), parse_mode = 'html', reply_markup = remove) 
        bot.send_message (message.chat.id, fin_text, parse_mode = 'html', reply_markup = cancel)
        isorder = False

@bot.message_handler(func=lambda message: message.text == 'Информация') #INFO + CANCEL
def info(message):
    isorder = False
    isperson = False
    isbanned = False
    bot.send_message (message.chat.id, info_text, parse_mode = 'html', reply_markup = cancel)

@bot.message_handler(func=lambda message: message.text == 'Назад') #CANCEL
def cancel_1(message):
    isorder = False
    isperson = False
    isbanned = False
    mainm(message)

bot.polling(none_stop = True)

