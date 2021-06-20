"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
   В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
   Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys

size = len(sys.argv)
hours = 0
price = 0
bonus = 0

if size < 3:
    print("Ошибка: нужно ввести 2 значения")
    exit(0)
if size >= 3:
    try:
        hours = int(sys.argv[1])
        price = int(sys.argv[2])
    except:
        print("Ошибка: нужно вводить целые числа")
        exit(0)
if size > 3:
    try:
        bonus = int(sys.argv[3])
    except:
        print("Ошибка: нужно вводить целые числа")
        exit(0)

result = hours * price + bonus
print(f"З/П сотрудника {result}р")
print("end")
