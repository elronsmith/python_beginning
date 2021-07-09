"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
   В рамках класса реализовать два метода.
   Первый, с декоратором @classmethod.
   Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
   Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
   Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    @classmethod
    def format(cls, text):
        d, m, y = text.split("-")
        return cls(Date.correct_day(int(d)), Date.correct_month(int(m)), Date.correct_year(int(y)))

    @staticmethod
    def correct_day(day):
        if day < 1:
            return 1
        elif day > 31:
            return 31
        else:
            return day

    @staticmethod
    def correct_month(month):
        if month < 1:
            return 1
        elif month > 12:
            return 12
        else:
            return month

    @staticmethod
    def correct_year(year):
        if year < 1:
            return 1
        elif year > 2050:
            return 2050
        else:
            return year


print(str(Date.format("0-0-0")) == "Date(1, 1, 1)")
print(str(Date.format("01-02-2023")) == "Date(1, 2, 2023)")
print(str(Date.format("32-13-2060")) == "Date(31, 12, 2050)")
print("end")
