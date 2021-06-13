"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
   Вывести каждое слово с новой строки.
   Строки необходимо пронумеровать.
   Если в слово длинное, выводить только первые 10 букв в слове.
"""

max_chars = 10
data = input('Введите слова, разделенные пробелами: ')
list_data = data.split()
for index, item in enumerate(list_data):
    item = item if len(item) <= max_chars else item[:max_chars]
    print(f"{index + 1}: {item}")
print("end")
