"""
4. Пользователь вводит целое положительное число.
   Найдите самую большую цифру в числе.
   Для решения используйте цикл while и арифметические операции.
"""

number = input("Введите целое положительное число:")
maximum = 0
while True:
    a = int(number) % 10
    number = str(int(number) // 10)
    if a > maximum:
        maximum = a
    if number == "0":
        break

print(f"самая большая цифра в числе это {maximum}")
print("end")
