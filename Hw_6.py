__author__ = "Виталий Варщук"

import math

# Задание-1:
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати,
# нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то
# написать, что такой треугольник нельзя создать и сделать exit(1)


class Triangle:
    def __init__(self, A, B, C):
        self.Ax = A[0]
        self.Ay = A[1]
        self.Bx = B[0]
        self.By = B[1]
        self.Cx = C[0]
        self.Cy = C[1]

        self.lines = self.sides()

        if not self.lines[0] + self.lines[1] > self.lines[2] and \
        self.lines[2] + self.lines[0] > self.lines[1] and \
        self.lines[1] + self.lines[2] > self.lines[0]:
            print("Такой треугольник создать нельзя")
            exit(1)

    def sides(self):
        self.AB = math.sqrt((self.Ax - self.Bx) ** 2 + (self.Ay - self.By) ** 2)
        self.BC = math.sqrt((self.Bx - self.Cx) ** 2 + (self.By - self.Cy) ** 2)
        self.CA = math.sqrt((self.Cx - self.Ax) ** 2 + (self.Cy - self.Ay) ** 2)
        return [round(self.AB, 1), round(self.BC, 1), round(self.CA, 1)]

    def perimeter(self):
        return sum(self.lines)

    def area(self):
        p = self.perimeter() / 2
        S = math.sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.CA))
        return round(S, 1)


print("\nЗадание-1")

A = (0, 0)
B = (3, 3)
C = (3, 0)

triangle = Triangle(A, B, C)

print(triangle.sides())
print(triangle.perimeter())
print(triangle.area())

# Задание-2:
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно)
# комплексными числами \ матрицами \ светофор \ микроволновка

print("\nЗадание-2")
