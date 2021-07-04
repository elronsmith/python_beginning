"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
   который должен принимать данные (список списков) для формирования матрицы.
   Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
   Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
   Результатом сложения должна быть новая матрица.
   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        s = ''
        for row in self._matrix:
            line = ' '.join([str(i) for i in row])
            s += line + "\n"
        return s

    def __add__(self, other):
        result = []
        for row_index in range(len(self._matrix)):
            self_row = self._matrix[row_index]
            other_row = other[row_index]
            result_row = []
            result.append(result_row)
            for cell_index in range(len(self_row)):
                result_row.append(self_row[cell_index] + other_row[cell_index])
        return Matrix(result)

    def __getitem__(self, index):
        return self._matrix[index]


m1 = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
print("end")
