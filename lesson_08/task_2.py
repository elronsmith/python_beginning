"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
   Проверьте его работу на данных, вводимых пользователем.
   При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivideException(Exception):
    def __init__(self, message):
        self.message = message


def divide(a, b):
    if b == 0:
        raise ZeroDivideException("ZeroDivideException: деление на ноль")
    return a / b


try:
    result = divide(5, 2)
    print(result)
    result = divide(5, 0)
    print(result)
except ZeroDivideException as e:
    print(e)

print("end")
