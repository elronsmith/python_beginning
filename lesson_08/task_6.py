"""
6. Продолжить работу над вторым заданием.
   Реализуйте механизм валидации вводимых пользователем данных.
   Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
   Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
"""
!!! Т.к. нужно передавать кол-во принтеров, то у класса AEquipment не может быть идентификатора
"""
import task_5
import task_4


class SuperWarehouseImpl(task_5.WarehouseImpl):
    def add_equipment(self, subdivision_name, equipment, count):
        if isinstance(count, int):
            for c in range(count):
                super().add_equipment(subdivision_name, equipment)


warehouse = SuperWarehouseImpl()
printer = task_4.Printer("Canon", "C1", 1, ["white"])
warehouse.add_equipment("sklad", printer, 5)
print(warehouse.get_equipments("sklad"))
print("end")
