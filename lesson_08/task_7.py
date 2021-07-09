"""
7. Реализовать проект «Операции с комплексными числами».
   Создайте класс «Комплексное число».
   Реализуйте перегрузку методов сложения и умножения комплексных чисел.
   Проверьте работу проекта.
   Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
   Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f"ComplexNumber({self.a} - {abs(self.b)}i)"
        return f"ComplexNumber({self.a} + {self.b}i)"

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        x1 = self.a * other.a
        x2 = self.a * other.b
        x3 = self.b * other.a
        x4 = self.b * other.b
        return ComplexNumber(x1 + x4*-1, x2 + x3)


z1 = ComplexNumber(1, -1)
z2 = ComplexNumber(3, 6)
print("z1 =", z1)
print("z2 =", z2)
z3 = z1 + z2
print("z1 + z2 =", z3)
z4 = z1 * z2
print("z1 * z2 =", z4)
print("end")
