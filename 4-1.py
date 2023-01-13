# 1 Пользователь вводит число, необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ round())

n = int(input('Введите целое число: '))

import math

def pi_num(n):
    p = math.pi  # функция вызова числа Пи.
    print(p)
    count = 0
    for i in str(p):
        while count <= n + 1:
            count += 1
            print(i, end = '')
            break


pi_num(n)