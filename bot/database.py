# -*- coding:utf-8 -*-
from con_to_db import getConnection

def get_from_db(n,l):#запрос,условие
    print(n)
    c=l[0]
    q=l[1]
    if len(l)>2:
        t=l[2]
        k=l[3]
    c=int(c)
    connection=getConnection()
    if c==1:
        if k=="С ремонтом":
            sql=f"SELECT {n} FROM Rielt_sale WHERE (district LIKE '%{q}%') AND (room_number like '%{t}%') AND (condition_of_repair!='Без ремонта' AND condition_of_repair!='-----') AND (status=0)"
        else:
            sql=f"SELECT {n} FROM Rielt_sale WHERE (district LIKE '%{q}%') AND (room_number like '%{t}%') AND (condition_of_repair like '%-----%' OR condition_of_repair like '%{k}%') AND (status=0)"
    elif c==2:
        sql=f"SELECT {n} FROM Rielt_new_builds WHERE (district LIKE '%{q}%')"
    try:
        print(sql)
        cursor=connection.cursor()
        cursor.execute(sql)
        keys=[b[0] for b in cursor.description]
        result=[]
        for row in cursor:
            result.append([row[key] for key in keys])
        connection.close()
        return result
    except Exception as e:
        print("gfd"+str(e))
        connection.close()

def get_from_ua(c,n,t,q):
    connection=getConnection()
    if c==1:
        sql=f"SELECT {n} FROM Rielt_users WHERE {t}={q}"
    elif c==2:
        sql=f"SELECT {n} FROM Rielt_admins WHERE {t}='{q}'"
    try:
            cursor=connection.cursor()
            cursor.execute(sql)
            keys=[b[0] for b in cursor.description]
            result=[]
            for row in cursor:
                result.append([row[key] for key in keys])
            connection.close()
            return result
    except Exception as e:
            print("gfu"+str(e))
            connection.close()

def add_new_user(user_id,filt):
    connection=getConnection()
    if is_new(user_id):
        sql=f"INSERT INTO Rielt_users (name,phone,status,user_id,filt) VALUES('-----','-----',0,{user_id},'{filt}');"
    else:
        sql=f"UPDATE Rielt_users SET filt='{filt}' WHERE user_id={user_id}"
    try:
        cursor=connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()

def update_user(user_id,name,phone):
    connection=getConnection()
    sql=f"UPDATE Rielt_users SET name='{name}',phone='{phone}',status=1 WHERE user_id={user_id}"
    try:
        cursor=connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()
        
def is_new(user_id):
    connection=getConnection()
    sql=f"SELECT * FROM Rielt_users WHERE user_id={user_id}"
    try:
        cursor=connection.cursor()
        cursor.execute(sql)
        keys=[b[0] for b in cursor.description]
        result=[]
        for row in cursor:
            result.append([row[key] for key in keys])
        connection.close()
        return 0 if len(result)!=0 else 1
    except Exception as e:
        print(e)
        connection.close()
        return -2

def is_registered(user_id):
    connection=getConnection()
    sql=f"SELECT status FROM Rielt_users WHERE user_id={user_id}"
    try:
        cursor=connection.cursor()
        cursor.execute(sql)
        keys=[b[0] for b in cursor.description]
        result=[]
        for row in cursor:
            result.append([row[key] for key in keys])
        connection.close()
        #print(result)
        return 1
    except Exception as e:
        print(e)
        connection.close()
        return -2

#print(get_from_ua(1,'phone,name,district','user_id',user_id)[0])