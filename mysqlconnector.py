import mysql.connector
cnx = mysql.connector.connect(user='root', password='se_pHANTOM0708', host='127.0.0.1', database='sakila')

try:
   cursor = cnx.cursor()
   #тут пишем запрос
   cursor.execute('SELECT * from city;')
   result = cursor.fetchall()
   print (result)
finally:
    cnx.close()
