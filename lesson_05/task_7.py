"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
   в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
   Пример строки файла: firm_1   ООО   10000   5000.
   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
   Если фирма получила убытки, в расчёт средней прибыли её не включать.
   Далее реализовать список.
   Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
   Если фирма получила убытки, также добавить её в словарь (со значением убытков).
   Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
   Итоговый список сохранить в виде json-объекта в соответствующий файл.
   Пример json-объекта:
   [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
   Подсказка: использовать менеджер контекста.
"""
import json

firms = {}
average_profit = 0

with open("task_7.txt", "r", encoding="utf-8") as f:
    total_profit = 0
    profits_count = 0
    for line in f:
        lines = line.split()
        firm_name = lines[0]
        incoming = int(lines[2])
        outgoing = int(lines[3])
        firms[firm_name] = incoming - outgoing
        profit = incoming - outgoing
        if profit > 0:
            profits_count += 1
            total_profit += profit
    average_profit = total_profit // profits_count

print(firms)
print(f"average profit: {average_profit}")

with open("task_7.json", "w") as f:
    result = [firms, {"average_profit": average_profit}]
    json.dump(result, f)
print("end")
