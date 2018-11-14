import json 
InputData = input(str('Ожидаю json на вход: '))
StoredData = json.loads(InputData)

#def json_validator(InputData):
#    try:
#        json.loads(InputData)
#        return True
#    except ValueError as error:
#        print("invalid json: %s" % error)
#        return False

with open('storage_json.txt', 'a') as file:

#рассчитать future value компаунд-счета

    def monthly_compound (p,n,r,pmt):
        r_month = float(r/100/12)
        n_month = float(n*12)
        fv = pmt*((((1+r_month)**n_month)-1)/r_month) + p*((1+r_month)**n_month)
        return fv
    
#Рассчитать месячные выплаты (pay_monthly)

    def bank_account (percentage,months,credit_sum):

        monthly_percentage = percentage/12/100 
        koef = ((monthly_percentage*(1+monthly_percentage)**months) / (((1+monthly_percentage)**months)-1))
        pay_monthly = credit_sum * koef
        return pay_monthly

    function_credit = StoredData["function_credit"]

    if function_credit:

        years = int(StoredData["Полных лет на кредит"])
        months = years*12
        credit_sum = int(StoredData["Сумма кредита на руки"])
        percentage = float(StoredData["Годовых"])
      
        fin_credit = int(bank_account(percentage,months,credit_sum)*100)/100
        print(str(fin_credit))
        file.write("Входные данные:" + '\n' + "сумма кредита: " + str(credit_sum) + '\n' +  "Полных лет на кредит: "+ str(years) + '\n' + "Процентов годовых: " + str(percentage) + '\n' + "Результат, ежемесячный платеж => " + str(fin_credit))

# Добавить вид print("Сумма с переплатой: ", "%.2f" % sum) 
    else:
      
        p = int(StoredData["Первоначальный взнос"])
        n = int(StoredData["Количество лет"])
        r = float(StoredData["Годовая ставка"])
        pmt = int(StoredData["Ежемесячный платеж"])

        fin = int(monthly_compound (p,n,r,pmt)*100)/100
        print (str(fin))
        file.write()

#4. дописать сохрание исходных условий (переменных функции) и результат в файл => done 
#3. Ввести валидацию json (выводить "невалидный json" если ошибки) => not done 
#1. проверить результаты вычислений
#2. проверить комбинации результатов
