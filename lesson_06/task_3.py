"""
3. Реализовать базовый класс Worker (работник).
   - определить атрибуты: name, surname, position (должность), income (доход);
   - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
   - создать класс Position (должность) на базе класса Worker;
   - в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
   - проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
"""
комментарий к задаче:
т.к. указано "создать класс Position (должность) на базе(!) класса Worker" 
        а не "создать класс Position (должность) унаследованный от класса Worker"
то в конструктор передаётся именно экземпляр класса Worker
"""

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_wage(self):
        return self._income["wage"]

    def get_bonus(self):
        return self._income["bonus"]


class Position:
    def __init__(self, worker):
        self.__worker = worker

    def get_full_name(self):
        return f"{self.__worker.name} {self.__worker.surname}"

    def get_total_income(self):
        wage = self.__worker.get_wage()
        bonus = self.__worker.get_bonus()
        return wage + bonus


worker = Worker("Иван", "Иванов", "Работяга", {"wage": 10000, "bonus": 1000})
position = Position(worker)
print(f"Имя сотрудника: {position.get_full_name()}")
print(f"Доход с учетом премии: {position.get_total_income()}р")
print("end")
