"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
   Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open("task_1.txt", "w", encoding="utf-8") as f:
    while True:
        text = input()
        if len(text) == 0:
            break
        else:
            f.write(text)
            f.write("\n")

print("end")
