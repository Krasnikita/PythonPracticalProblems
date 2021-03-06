#http://taskcode.ru/function/array
#Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем. Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать. Вывод значений элементов массива должен происходить в основной ветке программы.

#Пояснение к задаче и алгоритм решения

#В основной ветке программы:

#    Считать два значения - минимум и максимум диапазона.
#    Вызвать функцию (или процедуру в Pascal), передав в качестве аргументов ссылку на массив, минимум и максимум.
#    В цикле вывести на экран значения массива.

# В функции (процедуре) массив заполняется случайными числами.

## Подкключаем рандомайзер
## random.randint(<Начало>, <Конец>) — возвращает псевдослучайное целое число в диапазоне от <Начало> до <Конец>:
## Подключаем массивы

import random
with open('storage.txt', 'a') as file:
    n = 50 

    def func (a, min, max):
        for i in range (n):
            a[i] = int(random.randint (min, max))
#>>>> вообще не вкурил, что это такое, но без этого не работает(!), видимо, обозначает, с какого значения должно "стартовать" a 
    a = [0]*n
    min = int(input('Введите число ОТ: '))
    max = int(input('Введите число ДО: '))
    func (a,min,max)
    print ("Случайные числа: ", a)
    file.write ('Исходные данные: ' + str(min) + ' | ' + str(max) + '\n' + 'Результат операции:' + str(a) + '\n')
