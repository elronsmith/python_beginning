"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
   При нечетном количестве элементов последний сохранить на своем месте.
   Для заполнения списка элементов необходимо использовать функцию input().
"""

items = input("Введите слова через пробел: ").split()
print(items)
half_size = len(items) // 2
for i in range(half_size):
    first = i * 2
    second = i * 2 + 1
    items[first], items[second] = items[second], items[first]
print(items)
print("end")
