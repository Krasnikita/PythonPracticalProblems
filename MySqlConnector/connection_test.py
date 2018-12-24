# работает. без конфига

import mysql.connector
from mysql.connector import Error

def insert_book(title, isbn):
    query = "INSERT INTO books(title,isbn) VALUES(%s,%s)"
    args = (title, isbn)

    try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       database='python',
                                       user='root',
                                       password='se_pHANTOM0708')

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
   insert_book('Over a cookoe','10814391870')

if __name__ == '__main__':
    main()
