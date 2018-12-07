from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

#import mysql.connector
#conn = mysql.connector.connect(user='root', password='se_pHANTOM0708', host='127.0.0.1', database='python')

#cur = conn.cursor()
#query = ('CREATE TABLE users_new (a INTEGER PRIMARY KEY, b VARCHAR(10));')
#query = ('DROP TABLE users_new;')
#query = ('ALTER TABLE users ADD COLUMN lastname INTEGER;')
#query = ('INSERT INTO users(id,firstname) VALUES (9,"Кто-то еще 32");')

#cur.execute(query)

#for (id, firstname) in cur:
#  print("{}, {}".format(id, firstname))

#cur.close()
#conn.close()

# Другой способ
#import mysql.connector

#cnx = mysql.connector.connect(user='root', password='se_pHANTOM0708', host='127.0.0.1', database='python')

#name = "Никита"

#def checkname(name):
#	yourname = str(input('Введите имя:'))
#
#	if yourname == name:
#		print ('Привет,', yourname, "!")

#	else:
#		print ('Пробуем еще раз, гражданина')

#try:
#   cursor = cnx.cursor()
   #тут пишем запрос
#   cursor.execute('ALTER TABLE users ADD COLUMN c INTEGER;')
#  result = cursor.fetchall()
#  print(result)
#finally:
#    cnx.close()


#checkname(name)
