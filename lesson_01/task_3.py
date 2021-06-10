"""
3. Узнайте у пользователя число n.
   Найдите сумму чисел n + nn + nnn.
   Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number = input("Введите число:")
n = int(number)
n2 = int(number * 2)
n3 = int(number * 3)

result = n + n2 + n3
print(f"сумма чисел {n} + {n2} + {n3} = {result}")
print("end")
