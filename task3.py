# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

num = int(input('Введите количество чисел для списка: '))
list = []
for i in range(1, num + 1):
    a = randint(1, num + 1)
    list.append(a)
print(list)

newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)
