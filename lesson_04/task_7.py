"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
   При вызове функции должен создаваться объект-генератор.
   Функция должна вызываться следующим образом: for el in fact(n).
   Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
   Подсказка: факториал числа n — произведение чисел от 1 до n.
   Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from functools import reduce


def fact(n):
    for i in range(1, n + 1):
        d = ' * '.join((str(c) for c in range(1, i + 1)))
        f = reduce(lambda a, b: a * b, (v for v in range(1, i + 1)))
        print(f"{i}! = {d} = {f}")
        yield f


n = 4
for el in fact(n):
    pass
print("end")
