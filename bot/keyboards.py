# -*- coding: utf8 -*-
from telebot.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import calendar
import datetime
from config import months
import calendar

def sel_distr():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("Мирабадский")
    b2=KeyboardButton("Мирзо Улугбекский")
    b3=KeyboardButton("Олмазарский")
    b4=KeyboardButton("Сергелийский")
    b5=KeyboardButton("Учтепинский")
    b6=KeyboardButton("Чиланзарский")
    b7=KeyboardButton("Шайхантохурский")
    b8=KeyboardButton("Юнусабадский")
    b9=KeyboardButton("Яшнабадский")
    b10=KeyboardButton("Яккасарайский")
    b11=KeyboardButton("⬅️ Назад")
    kb.row(b1,b2)
    kb.row(b3,b4)
    kb.row(b5,b6)
    kb.row(b7,b8)
    kb.row(b9,b10)
    kb.row(b11)
    return kb

def sel_type():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("🏘 Вторичный рынок")
    b2=KeyboardButton("🏙 Новостройки")
    b3=KeyboardButton("💰 Хочу продать свою недвижимость")
    b4=KeyboardButton("💡 Как это работает?")
    #bb=KeyboardButton("⬅️ Назад")
    kb.row(b1,b2)
    kb.row(b3)
    kb.row(b4)
    #kb.row(bb)
    return kb

def sel_rooms():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("1⃣-комнатные")
    b2=KeyboardButton("2⃣-комнатные")
    b3=KeyboardButton("3⃣-комнатные")
    b4=KeyboardButton("4⃣-комнатные")
    b5=KeyboardButton("5⃣-комнатные")
    bb=KeyboardButton("⬅️ Назад")
    kb.row(b1,b2)
    kb.row(b3,b4)
    kb.row(b5)
    kb.row(bb)
    return kb

def sel_sost():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b=KeyboardButton("С ремонтом")
    b1=KeyboardButton("Без ремонта")
    bb=KeyboardButton("⬅️ Назад")
    kb.row(b,b1)
    kb.row(bb)
    return kb

def fin():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("Посмотреть")
    b2=KeyboardButton("Главное меню")
    b3=KeyboardButton("Зарегистрироваться")
    kb.row(b1)
    kb.row(b2)
    kb.row(b3)
    return kb

def fin2():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("🎥 Посмотреть")
    b2=KeyboardButton("📲 Главное меню")
    kb.row(b1)
    kb.row(b2)
    return kb

def fin3():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("📲 Главное меню")
    kb.row(b1)
    return kb

def change(lon,lat):
    kb=InlineKeyboardMarkup()
    b=InlineKeyboardButton("♻️ Обновить",callback_data="obnov")
    b1=InlineKeyboardButton("⬅️ Предыдущая",callback_data="prev")
    b2=InlineKeyboardButton("Следующая ➡️",callback_data="next")
    b4=InlineKeyboardButton("🆗 То, что надо!",callback_data="calendar")
    kb.row(b4)
    if lon!="-----" and lat!="-----":
        coord="#"+lon+"#"+lat
        b3=InlineKeyboardButton("🌎 Показать на карте",callback_data=coord)
        kb.row(b3)
    kb.row(b1,b2)
    return kb

def closing():
    kb=InlineKeyboardMarkup()
    b1=InlineKeyboardButton("❌ Закрыть",callback_data="closing")
    kb.row(b1)
    return kb

def calend(k):
    now=datetime.datetime.now()
    cal_kb=InlineKeyboardMarkup(row_width=7)
    b_list=[]
    y,m=0,0
    if now.month+k>12:
        y+=1
        m=(now.month+k)-12
    else:
        m=now.month+k
    t=months[calendar.month_abbr[m]]+" "+str(now.year+y)
    cal_kb.row(InlineKeyboardButton(t,callback_data=' '))
    for i in range(1,calendar.monthrange(now.year+y,m)[1]+1):
        if k==0:
            if i<now.day:
                b_list.append(InlineKeyboardButton(' ',callback_data=" "))
            else:
                b_list.append(InlineKeyboardButton(str(i),callback_data=str(i)))
        else:
            b_list.append(InlineKeyboardButton(str(i),callback_data=str(i)))
    for i in range(0,23,7):
        cal_kb.row(b_list[i],b_list[i+1],b_list[i+2],b_list[i+3],b_list[i+4],b_list[i+5],b_list[i+6])
    if calendar.monthrange(now.year+y,m)[1]==29:
        cal_kb.row(b_list[-1])
    elif calendar.monthrange(now.year+y,m)[1]==30:
        cal_kb.row(b_list[-2],b_list[-1])
    elif calendar.monthrange(now.year+y,m)[1]==31:
        cal_kb.row(b_list[-3],b_list[-2],b_list[-1])
    cal_kb.row(InlineKeyboardButton("⬅️",callback_data="calend_prev"),InlineKeyboardButton("➡️",callback_data="calend_next"))
    cal_kb.row(InlineKeyboardButton("❌ Закрыть",callback_data="closing"))
    return cal_kb

def cont():
    phone=KeyboardButton("📞 Отправить контакт",request_contact=True)
    back=KeyboardButton('◀️ Назад')
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(phone)
    kb.row(back)
    return kb

def not_found():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b2=KeyboardButton("📲 Главное меню")
    kb.row(b2)
    return kb    

def himself():
    kb=InlineKeyboardMarkup()
    b1=InlineKeyboardButton("Мирабадский",callback_data="Мирабадский")
    b2=InlineKeyboardButton("Мирзо Улугбекский",callback_data="Мирзо Улугбекский")
    b3=InlineKeyboardButton("Олмазарский",callback_data="Олмазарский")
    b4=InlineKeyboardButton("Сергелийский",callback_data="Сергелийский")
    b5=InlineKeyboardButton("Учтепинский",callback_data="Учтепинский")
    b6=InlineKeyboardButton("Чиланзарский",callback_data="Чиланзарский")
    b7=InlineKeyboardButton("Шайхантохурский",callback_data="Шайхантохурский")
    b8=InlineKeyboardButton("Юнусабадский",callback_data="Юнусабадский")
    b9=InlineKeyboardButton("Яшнабадский",callback_data="Яшнабадский")
    b10=InlineKeyboardButton("Яккасарайский",callback_data="Яккасарайский")
    b11=InlineKeyboardButton("⬅️ Назад",callback_data="⬅️ Назад")
    kb.row(b1,b2)
    kb.row(b3,b4)
    kb.row(b5,b6)
    kb.row(b7,b8)
    kb.row(b9,b10)
    kb.row(b11)
    return kb

def kv():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    b1=KeyboardButton("Зарегистрироваться.")
    b2=KeyboardButton('◀️ Назад.')
    kb.row(b1)
    kb.row(b2)
    return kb