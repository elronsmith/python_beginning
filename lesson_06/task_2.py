"""
2. Реализовать класс Road (дорога).
   - определить атрибуты: length (длина), width (ширина);
   - значения атрибутов должны передаваться при создании экземпляра класса;
   - атрибуты сделать защищёнными;
   - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
   - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
   - проверить работу метода.
   Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _weight_kg = 25
    _thickness_cm = 5

    def get_massa_t(self):
        result_kg = self._thickness_cm * (self._width_m * self._length_m * self._weight_kg)
        return int(result_kg / 1000)

    def __init__(self, length_m, width_m):
        self._length_m = length_m
        self._width_m = width_m


road = Road(5000, 20)
print(road.get_massa_t(), "т")
print("end")
