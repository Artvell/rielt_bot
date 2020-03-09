# -*- coding: utf8 -*-
import telebot
from config import *
from database import *
from keyboards import *
import calendar as cal
from time import sleep
""
bot = telebot.TeleBot(token)
filt={} #id:[filters]
districts=["Мирабадский","Мирзо Улугбекский","Олмазарский","Сергелийский","Учтепинский","Чиланзарский","Шайхантохурский","Юнусабадский","Яшнабадский","Яккасарайский"]
rooms={"1⃣-комнатные":1,"2⃣-комнатные":2,"3⃣-комнатные":3,"4⃣-комнатные":4,"5⃣-комнатные":5}
res={} #id:[[],[],[]]
n={} #id:number
calend_info={}
kv_id={}
indic={}
pos={} #id:number
fsm={} #id:number
isn={}
name_writing={}
u_name={}
u_phone={}
u_status={}
u_distr={}
u_day={}
dop={}
files={}

def con(l):
    c=''
    for b in l:
        c+=str(b)+','
    c=c[:-1]
    return c

def sales(t,k,user_id):
    print(str(k)+'/'+str(t))
    k=int(k)
    t=int(t)
    if k==0:
        if user_id in res:
            spisok=res[user_id]
        else:
            f=get_from_ua(1,'filt','user_id',user_id)[0][0].split(',')
            if t==1:
                res[user_id]=get_from_db('uid,district,orient,room_number,floor,condition_of_repair,price,photo,longitude,latitude,street,square,dop_id,mater',f)
                spisok=res[user_id]
            else:
                res[user_id]=get_from_db('uid,district,street,builder,reput,compl,date,price,ostat,parking,security,child,uprava,photo,longitude,latitude,dop_id,struct,file_id',f)
                spisok=res[user_id]
                
    else:
        f=get_from_ua(1,'filt','user_id',user_id)[0][0].split(',')
        if t==1:
            res[user_id]=get_from_db('uid,district,orient,room_number,floor,condition_of_repair,price,photo,longitude,latitude,street,square,dop_id,mater',f)
            spisok=res[user_id]
        else:
            res[user_id]=get_from_db('uid,district,street,builder,reput,compl,date,price,ostat,parking,security,child,uprava,photo,longitude,latitude,dop_id,struct,file_id',f)
            spisok=res[user_id] 
    maxim=len(spisok)
    num=pos[user_id]
    print(num)
    print(spisok)
    if num==maxim:
        num=0
        n[user_id]=0
        pos[user_id]=0
    elif num==-1:
        num=maxim-1
        n[user_id]=maxim-1
        pos[user_id]=maxim-1
    if t==1:
        print("num=",num)
        print(spisok)
        uid=spisok[num][0]
        kv_id[user_id]=uid
        dist=spisok[num][1]
        ori=spisok[num][2] if spisok[num][2]!='-----' else 'Не указан'
        r=spisok[num][3]
        fl=spisok[num][4]
        cr=spisok[num][5] if spisok[num][5]!='-----' else 'Без ремонта'
        p=spisok[num][6]
        ph=spisok[num][7]# if spisok[num][7]!='-----' else 
        lon=spisok[num][8]
        lat=spisok[num][9]
        street=spisok[num][10]
        square=spisok[num][11]
        dop_id=spisok[num][12]
        mater=spisok[num][13]
        text=f"ID: <b>{uid}</b>\nРайон: <b>{dist}</b>\nУлица: <b>{street}</b>\nОриентир: <b>{ori}</b>\nКомнат: <b>{r}</b>\nОбщая площадь: <b>{square}</b>\nЭтаж/Этажность: <b>{fl}</b>\nМатериал: <b>{mater}</b>\nСостояние: <b>{cr}</b>\nЦена: <b>{p}</b>"
        if ph!="-----":
            image=f'<a href="{ph}"> ‏ </a>'
            text=text+image
    else:
        print("num=",num)
        print(spisok)
        uid=spisok[num][0]
        kv_id[user_id]=uid
        dist=spisok[num][1]
        street=spisok[num][2]
        builder=spisok[num][3]
        reput=spisok[num][4]
        compl=spisok[num][5]
        date=spisok[num][6]
        p=spisok[num][7]
        ostat=spisok[num][8]# if spisok[num][7]!='-----' else 
        parking=spisok[num][9]
        security=spisok[num][10]
        child=spisok[num][11]
        uprav=spisok[num][12]
        ph=spisok[num][13]
        lon=spisok[num][14]
        lat=spisok[num][15]
        dop_id=spisok[num][16]
        struct=spisok[num][17]
        files[user_id]=spisok[num][18]
        print("!!!!!!!",files)
        text=f"ID: <b>{uid}</b>\nРайон: <b>{dist}</b>\nУлица: <b>{street}</b>\nЗастройщик: <b>{builder}</b>\nРепутация: <b>{reput}</b>\nНазвание Ж/К: <b>{compl}</b>\nГод: <b>{date}</b>\nЦена: <b>{p}</b>\nПлощадь: <b>{ostat}</b> кв.м.\nПаркинг: <b>{parking}</b> а/м\nОхрана: <b>{security}</b>\nДетский двор: <b>{child}</b>\nИнфраструктура: <b>{struct}</b>\nОбслуживает: <b>{uprav}</b>"
        if ph!="-----":
            image=f'Подробнее см. <a href="{ph}">здесь</a>'
            text=text+"\n"+image
    dop[user_id]=dop_id                
    return text,lon,lat

@bot.message_handler(content_types=["document"])
def doc(message):
    file_id=message.document.file_id
    if message.from_user.id==372762453 or message.from_user.id==498099441 or message.from_user.id==145109083:
        bot.send_message(message.from_user.id,file_id)
    #bot.send_document(message.from_user.id,file_id,caption="SKDSKSKDSDKSLDKLSKD",reply_markup=cont())    

@bot.message_handler(commands=['start'])
def start_message(message):
    if is_new(message.from_user.id):
        bot.send_message(message.from_user.id,"Здравствуйте.\nС помощью Merade House™ Вы легко можете сравнить несколько квартир в привлекательном районе, выбрать день просмотра и заказать обратный звонок напрямую от собственника недвижимости или от застройщика.\nА мы проверим документы на недвижимость и убедимся, что всё в порядке.",parse_mode="HTML")
        bot.send_message(message.from_user.id,"Что Вам больше нравится?",reply_markup=sel_type())
    else:
        if is_registered(message.from_user.id):
            bot.send_message(message.from_user.id,"<b>Здравствуйте!</b>\nРад, что вы вернулись! Посмотрим варианты?",parse_mode="HTML",reply_markup=fin2())
        else:
            bot.send_message(message.from_user.id,"<b>Здравствуйте!</b>\nРад, что вы вернулись! Посмотрим варианты?",parse_mode="HTML",reply_markup=fin())

@bot.message_handler(func=lambda message: message.text == "💡 Как это работает?")
def offerta(message):
    text=f'Пользовательское соглашение.\n<a href="{offerta_url}"> ‏ </a>'
    bot.send_message(message.from_user.id,text,parse_mode="HTML",reply_markup=fin3())

@bot.message_handler(func=lambda message: message.text == "💰 Хочу продать свою недвижимость")
def sale_own(message):
    if is_registered(message.from_user.id):
        bot.send_message(message.from_user.id,"В каком районе ваша квартира?",reply_markup=himself())
    else:
        bot.send_message(message.from_user.id,"Зарегистрируйтесь, чтобы отправить заявку.",reply_markup=kv())

@bot.message_handler(func=lambda message: message.text == "⬅️ Назад")
def back_steppp(message):
    user_id=message.from_user.id
    st=fsm[user_id]
    if st==1:
        bot.send_message(message.from_user.id,"Что Вам больше нравится?",reply_markup=sel_type())
    elif st==2:
        bot.send_message(user_id,"Выберите район:",reply_markup=sel_distr())
    elif st==3:
        bot.send_message(message.from_user.id,"Сколько комнат вам нужно?",reply_markup=sel_rooms())
    fsm[user_id]-=1


#0:аренда,продажа 1:район 2:комнаты 3:ремонт
@bot.message_handler(func=lambda message: message.text == "🏘 Вторичный рынок")
def sale(message):
    user_id=message.from_user.id
    fsm[user_id]=1
    filt[user_id]=[1]
    bot.send_message(user_id,"Выберите район:",reply_markup=sel_distr())

@bot.message_handler(func=lambda message: message.text == "🏙 Новостройки")
def rent(message):
    user_id=message.from_user.id
    fsm[user_id]=1
    filt[user_id]=[2]
    bot.send_message(user_id,"Выберите район:",reply_markup=sel_distr())

@bot.message_handler(func=lambda message: message.text in districts)
def d(message):
    fsm[message.from_user.id]=2
    if len(filt[message.from_user.id])==1:
        filt[message.from_user.id].append(message.text)
    elif len(filt[message.from_user.id])==2:
        filt[message.from_user.id][1]=message.text
    if filt[message.from_user.id][0]==1:
        bot.send_message(message.from_user.id,"Сколько комнат вам нужно?",reply_markup=sel_rooms())
    else:
        u_status[message.from_user.id]=4
        res[message.from_user.id]=get_from_db('uid,district,street,builder,reput,compl,date,price,ostat,parking,security,child,uprava,photo,longitude,latitude,dop_id,struct,file_id',filt[message.from_user.id])
        ff=con(filt[message.from_user.id])
        add_new_user(message.from_user.id,ff)
        if len(res[message.from_user.id])==0:
            bot.send_message(message.from_user.id,"Нам жаль, что все квартиры с такими параметрами уже куплены. Мы постараемся найти интересующие Вас квартиры в ближайшее время",reply_markup=not_found())
        else:
            bot.send_message(message.from_user.id,"Мы подобрали для Вас несколько вариантов. Вам интересно?",reply_markup=fin2())
        #bot.send_message(message.from_user.id,"Спасибо")        

@bot.message_handler(func=lambda message: message.text in rooms)
def room(message):
    fsm[message.from_user.id]=3
    if len(filt[message.from_user.id])==2:
        filt[message.from_user.id].append(rooms[message.text])
    elif len(filt[message.from_user.id])==3:
        filt[message.from_user.id][2]=rooms[message.text]
    if filt[message.from_user.id][0]==1:
        bot.send_message(message.from_user.id,"С ремонтом или без?",reply_markup=sel_sost())

    
@bot.message_handler(func=lambda message:message.text=="С ремонтом" or message.text=="Без ремонта")
def sost(message):
    if len(filt[message.from_user.id])==3:
        filt[message.from_user.id].append(message.text)
    elif len(filt[message.from_user.id])==4:
        filt[message.from_user.id][3]=message.text
    print(filt[message.from_user.id])
    if filt[message.from_user.id][0]==1:
        res[message.from_user.id]=get_from_db('uid,district,orient,room_number,floor,condition_of_repair,price,photo,longitude,latitude,street,square,dop_id,mater',filt[message.from_user.id])
    else:
        res[message.from_user.id]=get_from_db('uid,district,street,builder,reput,compl,date,price,ostat,parking,security,child,uprava,photo,longitude,latitude,dop_id,struct,file_id',filt[message.from_user.id])
    ff=con(filt[message.from_user.id])
    add_new_user(message.from_user.id,ff)
    if len(res[message.from_user.id])==0:
        bot.send_message(message.from_user.id,"Нам жаль, что все квартиры с такими параметрами уже куплены. Мы постараемся найти интересующие Вас квартиры в ближайшее время",reply_markup=not_found())
    else:
        if is_registered(message.from_user.id):
            bot.send_message(message.from_user.id,"Мы подобрали для Вас несколько вариантов. Вам интересно?",reply_markup=fin2())
        else:
            bot.send_message(message.from_user.id,"Найдены квартиры!",reply_markup=fin())
    
@bot.message_handler(func=lambda message: message.text=="🎥 Посмотреть")
def main(message):
    user_id=message.from_user.id
    pos[user_id]=0
    if user_id in filt:
        t,lo,lat=sales(filt[user_id][0],0,user_id)
    else:
        filt[user_id]=get_from_ua(1,'filt','user_id',user_id)[0][0].split(',')
        t,lo,lat=sales(int(filt[user_id][0]),0,user_id)
    if t!="По вашему запросу ничего не найдено!":
        if int(filt[user_id][0])==1:
            bot.send_message(message.from_user.id,t,reply_markup=change(lo,lat),parse_mode="HTML")
        else:
            file_id=files.get(user_id,res[user_id][0][18])
            if file_id!="-----":
                bot.send_document(user_id,file_id,caption=t,reply_markup=change(lo,lat),parse_mode="HTML")
            else:
                bot.send_message(message.from_user.id,t,reply_markup=change(lo,lat),parse_mode="HTML")
        n[user_id]=1
    else:
        bot.send_message(message.from_user.id,t,reply_markup=not_found(),parse_mode="HTML")
    #get_from_ua(1,'filt','user_id',user_id)[0]

@bot.message_handler(func=lambda message: message.text=="Зарегистрироваться")
def reg(message):
    user_id=message.from_user.id
    if is_registered(user_id):
        bot.send_message(user_id,"Вы уже зарегистрированы!",reply_markup=fin2())
    else:
        bot.send_message(user_id,"Пожалуйста, отправьте свои контакты",reply_markup=cont())
    @bot.message_handler(content_types=["contact"])
    def phone(message):
        bot.send_message(user_id,"Принято! Пожалуйста, введите ваше имя.")
        phone = message.contact.phone_number
        isn[message.from_user.id]=0
        @bot.message_handler(content_types=["text"])
        def names(message):
            if isn[message.from_user.id]==0:
                update_user(user_id,message.text,phone)
                bot.send_message(user_id,"Вы успешно зарегистрированы! Спасибо!",reply_markup=fin2())
                isn[message.from_user.id]=1

@bot.message_handler(func=lambda message: message.text=="Зарегистрироваться.")
def reg2(message):
    user_id=message.from_user.id
    add_new_user(message.from_user.id,"-,-,-,-,-,-")
    bot.send_message(user_id,"Пожалуйста, отправьте свои контакты",reply_markup=cont())
    @bot.message_handler(content_types=["contact"])
    def phon(message):
        bot.send_message(user_id,"Принято! Пожалуйста, введите ваше имя.")
        phone = message.contact.phone_number
        isn[message.from_user.id]=0
        @bot.message_handler(content_types=["text"])
        def name(message):
            if isn[message.from_user.id]==0:
                update_user(user_id,message.text,phone)
                bot.send_message(user_id,"Вы успешно зарегистрированы! Спасибо!\n\nВыберите район, в котором находится ваша квартира.",reply_markup=himself())
                isn[message.from_user.id]=1    

@bot.message_handler(func=lambda message: message.text == "◀️ Назад")
def back(message):
    bot.send_message(message.from_user.id,"Посмотрим квартиры?",reply_markup=fin2())

@bot.message_handler(func=lambda message: message.text == "◀️ Назад.")
def reset2(message):
    bot.send_message(message.from_user.id,"Что Вам больше нравится?",reply_markup=sel_type())

@bot.message_handler(func=lambda message: message.text=="📲 Главное меню")
def reset(message):
    bot.send_message(message.from_user.id,"Что Вам больше нравится?",reply_markup=sel_type())

@bot.callback_query_handler(func=lambda c: c.data[0] == "#")
def map(callback_query: telebot.types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    c = callback_query
    x, y = c.data.split("#")[1], c.data.split("#")[2]
    bot.send_location(user_id, float(x), float(y),reply_markup=closing())
    
@bot.callback_query_handler(func=lambda c: c.data=="closing")
def cls(callback_query: telebot.types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    c=callback_query
    bot.delete_message(callback_query.from_user.id,callback_query.message.message_id)

@bot.callback_query_handler(func=lambda c: c.data == "calendar")
def calendar(callback_query: telebot.types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    if is_registered(user_id):
        #bot.delete_message(user_id,callback_query.message.message_id)
        mes = bot.send_message(user_id, "Пожалуйста, выберите день просмотра:", reply_markup=calend(0))
        calend_info[user_id] = [mes.message_id, 0]
    else:
        bot.answer_callback_query(callback_query_id=callback_query.id,text="Зарегистрируйтесь, чтоб выбрать день для просмотра",show_alert=True,cache_time=5)

@bot.callback_query_handler(func=lambda c: c.data == "calend_next")
def cal_next(callback_query: telebot.types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    if calend_info[user_id][1] < 2:
        calend_info[user_id][1] += 1
        bot.edit_message_reply_markup(user_id, message_id=calend_info[user_id][0], reply_markup=calend(calend_info[user_id][1]))


@bot.callback_query_handler(func=lambda c: c.data == "calend_prev")
def cal_prev(callback_query: telebot.types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    if calend_info[user_id][1] > 0:
        calend_info[user_id][1] -= 1
        bot.edit_message_reply_markup(user_id, message_id=calend_info[user_id][0], reply_markup=calend(calend_info[user_id][1]))

@bot.message_handler(func=lambda message:u_status.get(message.from_user.id,0)==2)
def name(message):
    u_name[message.from_user.id]=message.text
    user_id=message.from_user.id
    tip=filt[user_id][0]
    update_user(message.from_user.id,message.text,u_phone.get(message.from_user.id))
    if int(tip)==1:
        bot.send_message(user_id,"Спасибо.\nМы беспокоимся о безопасности сделки, поэтому наши сотрудники проверят документы этой квартиры, затем мы пригласим Вас на просмотр квартиры",reply_markup=fin2())
    else:
        bot.send_message(user_id,"Спасибо.\nМы пригласим Вас на просмотр жилого комплекса и предоставим подробные сведения о том, как приобрести недвижимость в офисе застройщика.",reply_markup=fin2())
    u_status[user_id]=0
    day=u_day.get(user_id)
    now = datetime.datetime.now()
    ind = 0
    if now.month + calend_info[user_id][1] > 12:
        ind = now.month + calend_info[user_id][1] - 12
    else:
        ind = now.month + calend_info[user_id][1]
    month = months[cal.month_abbr[ind]]
    
    uid=kv_id[user_id]
    #callback_data[user_id] = [day, month]
    phone,name,dist=get_from_ua(1,'phone,name,filt','user_id',user_id)[0]
    distr=dist.split(',')[1]
    print(distr)
    typ='Вторичный рынок' if int(tip)==1 else "Новостройки" 
    t=f"Тип: {typ}\nID: {uid}\nДата: {month},{day}\nИмя: {name}\nТелефон: {phone}"
    print(dist)
    adms=get_from_ua(2,'admin_id','district',distr)
    for i in range(len(adms)):
        try:
            print(adms[i][0])
            bot.send_message(adms[i][0],t)
        except Exception as e:
            print(11,e)
            continue
    bot.send_message(372762453,t)
    bot.send_message(145109083,t)
    if dop[user_id]!=0:
        bot.send_message(dop[user_id],t) 

@bot.message_handler(func=lambda message:name_writing.get(message.from_user.id,0)==1 and u_status.get(message.from_user.id,0)!=2)
def nname(message):
    u_name[message.from_user.id]=message.text
    update_user(message.from_user.id,message.text,u_phone.get(message.from_user.id))
    print(111)
    name_writing[message.from_user.id]=0
    bot.send_message(message.from_user.id,"Спасибо.\nМы свяжемся с вами чтобы определить рыночную стоимость Вашей квартиры, организовать рекламу и поиск покупателя",reply_markup=fin3())
    print(333)
    phone,name=get_from_ua(1,'phone,name','user_id',message.from_user.id)[0]
    distr=u_distr.get(message.from_user.id)
    t=f"Хочет продать квартиру.\nРайон: {distr}\nИмя:{name}\nТелфон: {phone}"
    adms=get_from_ua(2,'admin_id','district',distr)
    for i in range(len(adms)):
        try:
            bot.send_message(adms[i][0],t)
        except Exception:
            continue
    bot.send_message(372762453,t)
    bot.send_message(145109083,t)
    if dop[user_id]!=0:
        bot.send_message(dop[user_id],t)

@bot.message_handler(content_types=["contact"],func=lambda message:u_status.get(message.from_user.id,0)==1)
def phone1(message):
    user_id=message.from_user.id
    bot.send_message(message.from_user.id,"Принято! Пожалуйста, введите ваше имя!",reply_markup=fin3())
    phone = message.contact.phone_number
    u_phone[message.from_user.id]=phone
    u_status[user_id]=2

@bot.message_handler(content_types=["contact"],func=lambda message:u_status.get(message.from_user.id,0)!=1)
def phone(message):
    bot.send_message(message.from_user.id,"Принято! Пожалуйста, введите ваше имя.",reply_markup=fin3())
    phone = message.contact.phone_number
    u_phone[message.from_user.id]=phone
    #update_user(user_id,"-----",phone)
    name_writing[message.from_user.id]=1



   

@bot.callback_query_handler(func=lambda c: c.data in days)
def call(callback_query: telebot.types.CallbackQuery):
    user_id = callback_query.from_user.id
    tip=filt[user_id][0]
    if int(tip)==1:
        text="Ваши персональные данные, такие как имя и номер, будут переданы собственнику недвижимости или его представителю для организации просмотра квартиры"
    else:
        text="Ваши персональные данные, такие как имя и номер, будут переданы застройщику или его представителю, чтобы пригласить Вас в офис застройщика"
    bot.answer_callback_query(callback_query_id=callback_query.id,text=text,show_alert=True,cache_time=5)
    if isn.get(user_id,0)==0:
        bot.send_message(user_id,"Пожалуйста, отправьте свои контакты",reply_markup=cont())
        isn[user_id]=0
        phone=u_phone.get(user_id)
        name=u_name.get(user_id)
    else:
        if int(tip)==1:
            bot.send_message(user_id,"Спасибо.\nМы беспокоимся о безопасности сделки, поэтому наши сотрудники проверят документы этой квартиры, затем мы пригласим Вас на просмотр квартиры",reply_markup=fin2())
        else:
            bot.send_message(user_id,"Спасибо.\nМы пригласим Вас на просмотр жилого комплекса и предоставим подробные сведения о том, как приобрести недвижимость в офисе застройщика.",reply_markup=fin2())
    day = callback_query.data
    u_status[user_id]=1
    u_day[user_id]=day
    bot.delete_message(user_id,callback_query.message.message_id)


@bot.callback_query_handler(func=lambda c: c.data=="obnov")
def obn(callback_query: telebot.types.CallbackQuery):
    user_id=callback_query.from_user.id
    pos[user_id]=0
    if user_id in filt:
        t,lo,lat=sales(int(filt[user_id][0]),0,user_id)
    else:
        filt[user_id]=f=get_from_ua(1,'filt','user_id',user_id)[0][0].split(',')
        t,lo,lat=sales(int(filt[user_id][0]),1,user_id)
    bot.delete_message(user_id,callback_query.message.message_id)
    bot.send_message(user_id,t,reply_markup=change(lo,lat),parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data=="prev")
def pr(callback_query: telebot.types.CallbackQuery):
    user_id = callback_query.from_user.id
    pos[user_id]-=1
    print(pos[user_id])
    t,lo,lat=sales(int(filt[user_id][0]),0,user_id)
    if int(filt[user_id][0])==1:
        bot.edit_message_text(chat_id=user_id,message_id=callback_query.message.message_id,text=t,reply_markup=change(lo,lat),parse_mode="HTML")
    else:
        file_id=files.get(user_id,res[user_id][0][18])
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&",file_id)
        bot.delete_message(user_id,callback_query.message.message_id)
        if file_id!="-----":
            bot.send_document(user_id,file_id,caption=t,reply_markup=change(lo,lat),parse_mode="HTML")
        else:
            bot.send_message(message.from_user.id,t,reply_markup=change(lo,lat),parse_mode="HTML")

@bot.callback_query_handler(func=lambda c: c.data=="next")
def nxt(callback_query: telebot.types.CallbackQuery):
    user_id = callback_query.from_user.id
    pos[user_id]+=1
    t,lo,lat=sales(int(filt[user_id][0]),0,user_id)
    if int(filt[user_id][0])==1:
        bot.edit_message_text(chat_id=user_id,message_id=callback_query.message.message_id,text=t,reply_markup=change(lo,lat),parse_mode="HTML")
    else:
        file_id=files.get(user_id,res[user_id][0][18])
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&",file_id)
        bot.delete_message(user_id,callback_query.message.message_id)
        if file_id!="-----":
            bot.send_document(user_id,file_id,caption=t,reply_markup=change(lo,lat),parse_mode="HTML")
        else:
            bot.send_message(message.from_user.id,t,reply_markup=change(lo,lat),parse_mode="HTML")


@bot.callback_query_handler(func=lambda c: c.data in districts)
def sal_kv_distr(callback_query: telebot.types.CallbackQuery):
    text="Информация, которую мы получаем от вас может быть использована, чтобы:\n1. Связаться с Вами\n2. Определить рыночную стоимость недвижимости\n3. Настроить рекламу\n4. Гарантировать безопасность сделки"
    bot.answer_callback_query(callback_query_id=callback_query.id,text=text,show_alert=True,cache_time=5)
    user_id = callback_query.from_user.id
    if isn.get(user_id,0)==0:
        add_new_user(user_id,"-,-,-,-,-,-")
        bot.send_message(user_id,"Пожалуйста, отправьте свои контакты",reply_markup=cont())
        isn[user_id]=0
        phone=u_phone.get(user_id)
        name=u_name.get(user_id)
        if isn[user_id]==0:
            update_user(user_id,name,phone)
            isn[user_id]=1
    else:
        bot.send_message(user_id,"Спасибо.\nМы свяжемся с вами чтобы определить рыночную стоимость Вашей квартиры, организовать рекламу и поиск покупателя",reply_markup=fin3())   
    distr=callback_query.data
    u_distr[user_id]=distr
    #bot.send_message(372762453,t)
    bot.delete_message(user_id,callback_query.message.message_id)
    #bot.send_message(user_id,"Ищете себе квартиру?",reply_markup=sel_type())

@bot.callback_query_handler(func=lambda c: c.data=="⬅️ Назад")
def bc(callback_query: telebot.types.CallbackQuery):
    user_id = callback_query.from_user.id
    bot.delete_message(user_id,callback_query.message.message_id)
    bot.send_message(user_id,"Что Вам больше нравится?",reply_markup=sel_type())
bot.polling()
