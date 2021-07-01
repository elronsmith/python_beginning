"""
4. Реализуйте базовый класс Car.
   - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
   - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
   - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
   - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
from enum import Enum


class Direction(Enum):
    Left = "налево"
    Right = "направо"


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction: Direction):
        print(f"машина повернула {direction.value}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    __max_speed = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.__max_speed:
            print("превышение скорости")
        return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    __max_speed = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.__max_speed:
            print("превышение скорости")
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def start_car(car: Car, direction: Direction):
    print("---")
    print(f"машина: {car.name}")
    car.go()
    print(f"скорость: {car.show_speed()}")
    car.turn(direction)
    car.stop()


townCar = TownCar(80, "yellow", "TownCar")
sportCar = SportCar(100, "red", "SportCar")
workCar = WorkCar(50, "green", "WorkCar")
policeCar = PoliceCar(90, "white", "PoliceCar")

start_car(townCar, Direction.Left)
start_car(sportCar, Direction.Left)
start_car(workCar, Direction.Right)
start_car(policeCar, Direction.Right)
print("end")
