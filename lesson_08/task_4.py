"""
4. Начните работу над проектом «Склад оргтехники».
   Создайте класс, описывающий склад.
   А также класс «Оргтехника», который будет базовым для классов-наследников.
   Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
   В базовом классе определите параметры, общие для приведённых типов.
   В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class AWarehouse:
    pass


class AEquipment:
    def __init__(self, company_name, model_name, weight):
        self.company_name = company_name
        self.model_name = model_name
        self.weight = weight


class Printer(AEquipment):
    def __init__(self, company_name, model_name, weight, print_colors):
        super().__init__(company_name, model_name, weight)
        self.colors = print_colors

    def __str__(self):
        return f"Printer({self.company_name}, {self.model_name}, {self.weight}, {self.colors})"


class Scanner(AEquipment):
    def __init__(self, company_name, model_name, weight, has_wifi):
        super().__init__(company_name, model_name, weight)
        self.has_wifi = has_wifi


class Xerox(AEquipment):
    def __init__(self, company_name, model_name, weight, has_sdcard):
        super().__init__(company_name, model_name, weight)
        self.has_sdcard = has_sdcard
