#http://taskcode.ru/linear/loan
#Рассчитать месячные выплаты (m) и суммарную выплату (s) по кредиту.

#О кредите известно, что он составляет n рублей, берется на y лет, под p процентов.

#Месячные выплаты находятся по формуле:
#m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)), где p выражается в долях единицы, а не процентах.

#открываем на запись файл 

user = str(input('Введите ваше имя:'))
with open('storage.txt', 'a') as file:

# заводим переменные

  years = int(input('Введите полных лет на кредит, который вы берете:'))
    # Data validation for the variable "percentage"
  while True:
     percentage = float(input('Годовая процентная ставка в формате Х.Х:'))
     if 0 <= percentage <= 1000:
         break
     else:
        print("Введите число больше 0 и меньше 1000")
  credit_sum = int(input('Введите сумму кредита на руки'))

#пересчитываем

  percentage = percentage/100
  monthly_percentage = percentage/12 
  months = years*12
  koef = ((monthly_percentage*(1+monthly_percentage)**months) / (((1+monthly_percentage)**months)-1))
  monthly_payment = credit_sum * koef
  sum = monthly_payment*months

  #вывод

  print("Ежемесячный платеж: ", "%.2f" % monthly_payment)
  print("Сумма с переплатой: ", "%.2f" % sum)

  sum = int(sum*100)/100
  #Запись
  file.write("Пользователь: " + user + "\n")
  file.write("Сумма кредита: " + str(credit_sum) + "\n")
  file.write("Процентная ставка: " + str(percentage) + "\n")
  
  file.write("Сумма с переплатой: " + str(sum) + "\n" + "\n")

  #СДЕЛАНО дополнительно: 1. сократить количество символов до 2х после запятой

  #СДЕЛАНО #+валидация вводимых данных 
  
  #СДЕЛАНО 2. записывать с пронумерованным в порядке очереди пользователем (в идеале в табличном виде - пользователь, сумма, процент, платеж, с переплатой 