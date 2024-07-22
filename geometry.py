import math


class Shape:
    def area(self):
        raise NotImplementedError("Подклассы должны включать в себя метод area!")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _is_a_triangle(self):
        return (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b)

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def _is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


def calculate_area(shape: Shape):
    return shape.area()
