"""
6. Сформировать (не программно) текстовый файл.
   В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
   Сюда должно входить и количество занятий.
   Необязательно, чтобы для каждого предмета были все типы занятий.
   Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
   Вывести его на экран.
   Примеры строк файла:
   Информатика:   100(л)   50(пр)   20(лаб).
   Физика:   30(л)   —   10(лаб)
   Физкультура:   —   30(пр)   —
   Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def parse_lection_count(text):
    start = text.index("(")
    return int(text[:start])


def get_lection_name_count(line):
    lines = line.split(":")
    lection_name = lines[0]
    lection_counts = lines[1].split()
    lection_counts = [parse_lection_count(v) for v in lection_counts if '(' in v]
    return lection_name, sum(lection_counts)


my_dict = {}

with open("task_6.txt", "r", encoding="utf-8") as f:
    for line in f:
        lection_name, lection_count = get_lection_name_count(line)
        my_dict[lection_name] = lection_count

print("Название предмета и общее количество занятий по нему:")
print(my_dict)
print("end")
