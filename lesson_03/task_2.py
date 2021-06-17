"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
   имя, фамилия, год рождения, город проживания, email, телефон.
   Функция должна принимать параметры как именованные аргументы.
   Реализовать вывод данных о пользователе одной строкой.
"""


def func(firstname, lastname, birthdate, city, email=None, phone=None):
    print(firstname, lastname, birthdate, city, email, phone)


func(firstname="Ivan", lastname="Ivanov", birthdate="01.01.2000", city="Moscow")

user = {"firstname": "Ivan",
        "lastname": "Ivanov",
        "birthdate": "01.01.2000",
        "city": "Moscow",
        "email": "ivan@email.com",
        "phone": "81234567890"}
func(**user)
print("end")
