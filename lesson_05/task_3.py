"""
3. Создать текстовый файл (не программно).
   Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
   Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
   Выполнить подсчёт средней величины дохода сотрудников.
   Пример файла:
   Иванов 23543.12
   Петров 13749.32
"""

min_salary = 20000.0

def get_name_salary(line):
    data_user = line.split()
    name = data_user[0]
    salary = data_user[1]
    return name, float(salary)


with open("task_3.txt", "r", encoding="utf-8") as f:
    mid_salary = 0
    lines_count = 0
    total_salary = 0
    for line in f:
        lines_count += 1
        name, salary = get_name_salary(line)
        if salary < min_salary:
            print(name)
        total_salary += salary
    mid_salary = total_salary / lines_count
    print(f"Средняя величина дохода сотрудников: {mid_salary:.2f}р")
print("end")
