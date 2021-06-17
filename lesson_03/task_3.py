"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
   и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    li = [a, b, c]
    minimum = min(li)
    summa = sum(li)
    return summa - minimum


print(my_func(
    a=1,
    b=3,
    c=5
))
print("end")
