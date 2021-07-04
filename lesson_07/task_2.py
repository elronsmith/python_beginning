"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
   Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
   К типам одежды в этом проекте относятся пальто и костюм.
   У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
   Это могут быть обычные числа: V и H, соответственно.
   Для определения расхода ткани по каждому типу одежды использовать формулы:
     для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
   Реализовать общий подсчет расхода ткани.
   Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
     проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self._v = V

    def get_consumption(self):
        return self._v / 6.5 + 0.5

    @property
    def value(self):
        return self._v


class Suit(Clothes):
    def __init__(self, H):
        self._h = H

    def get_consumption(self):
        return self._h * 2 + 0.3

    @property
    def value(self):
        return self._h


coat = Coat(65)
print("coat:", coat.value, coat.get_consumption())
suit = Suit(4)
print("suit:", suit.value, suit.get_consumption())

array1 = [Coat(65), Coat(65)]
print("array1:", sum([v.get_consumption() for v in array1]))

array2 = [Coat(65), Suit(4)]
print("array2:", sum([v.get_consumption() for v in array2]))

array3 = [Suit(4), Suit(4)]
print("array3:", sum([v.get_consumption() for v in array3]))
print("end")
