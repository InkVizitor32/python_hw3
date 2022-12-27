# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


n = int(input('Введите количество чисел в строке '))

import random
from random import random, randrange, randint

list=[randint(1,5) for i in range(n)] 
print(*list)
sum = 0
i = 1
while i < len(list):
    sum = sum + list[i]
    i +=2
print(sum)