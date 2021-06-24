"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
   выполнить подсчёт строк и слов в каждой строке.
"""

lines_count = 0
lines = []

with open("task_2.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines_count += 1
        words = line.split()
        lines.append(len(words))

print(f"Кол-во строк: {lines_count}")
for i in range(len(lines)):
    print(f"строка {i + 1} ,  кол-во слов: {lines[i]}")
print("end")
