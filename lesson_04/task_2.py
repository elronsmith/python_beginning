"""
2. Представлен список чисел.
   Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
   Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
   Для формирования списка использовать генератор.
   Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
   Результат: [12, 44, 4, 10, 78, 123].
"""

source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(source)
result = [source[i] for i in range(1, len(source)) if source[i] > source[i - 1]]
print(result)
print("end")
