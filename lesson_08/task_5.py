"""
5. Продолжить работу над первым заданием.
   Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
   Для хранения данных о наименовании и количестве единиц оргтехники,
     а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""

import task_4


class Subdivision:
    def __init__(self, name):
        self.name = name


class WarehouseImpl(task_4.AWarehouse):
    def __init__(self):
        self.subdivisions = {}

    def add_equipment(self, subdivision_name, equipment):
        subdivision = self.subdivisions.get(subdivision_name)
        if subdivision is None:
            subdivision = []
            self.subdivisions[subdivision_name] = subdivision
        subdivision.append(equipment)

    def get_equipments(self, subdivision_name):
        return self.subdivisions.get(subdivision_name)

    def del_equipments(self, subdivision_name, index):
        subdivision = self.subdivisions.get(subdivision_name)
        if isinstance(subdivision, list):
            if index in range(0, len(subdivision)):
                del subdivision[index]


if __name__ == '__main__':
    warehouse = WarehouseImpl()
    printer = task_4.Printer("Canon", "C1", 1, ["white"])
    warehouse.add_equipment("sklad", printer)
    print(warehouse.get_equipments("sklad"))
    warehouse.del_equipments("sklad", 0)
    print(warehouse.get_equipments("sklad"))
    print("end")
