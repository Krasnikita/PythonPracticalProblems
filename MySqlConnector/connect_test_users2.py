# работает. без конфига

import mysql.connector
from mysql.connector import Error

def insert_user(id, firstname):
    query = "INSERT INTO usersnew(id, firstname) VALUES(%s,%s)"
    args = (id, firstname)

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


#def main():
#   insert_user('1234081','10814391870')
#
#if __name__ == '__main__':
#    main()
