"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
   Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

with open("task_5.txt", "w+", encoding="utf-8") as f:
    f.write(" ".join([str(v) for v in range(5)]))
    f.seek(0)
    summa = sum(list(map(lambda x: int(x), f.read().split())))
    print(f"Сумма чисел в файле: {summa}")

print("end")
