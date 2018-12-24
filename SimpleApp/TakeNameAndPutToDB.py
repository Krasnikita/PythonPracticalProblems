import mysql.connector
from mysql.connector import Error

def insert_user(id, firstname):
    query = "INSERT INTO usersnew2(firstname) VALUES(%s,%s)"
    args = (firstname)

    try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       database='python',
                                       user='root',
                                       password='se_pHANTOM0708')

        cursor = conn.cursor()
        cursor.execute(query, args)
#lastrowid определяет номер последней вставки в БД
        if cursor.lastrowid:
            print(' ', cursor.lastrowid)
        else:
            print('Записано успешно')

        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


firstname = str(input('Введите имя:'))

insert_user(firstname)
