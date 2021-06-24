"""
4. Создать (не программно) текстовый файл со следующим содержимым:
   One - 1
   Two - 2
   Three - 3
   Four - 4
   Напишите программу, открывающую файл на чтение и считывающую построчно данные.
   При этом английские числительные должны заменяться на русские.
   Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
f_in = open("task_4.txt", "r", encoding="utf-8")
f_out = open("task_4_out.txt", "w", encoding="utf-8")

for line in f_in:
    lines = line.replace("\n", "").split()
    n = lines[len(lines) - 1]
    translate = my_dict.get(int(n))
    new_line = line.replace(n, translate)
    f_out.write(new_line)

f_in.close()
f_out.close()
print("end")
