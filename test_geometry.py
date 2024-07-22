import unittest
from geometry import Circle, Triangle, calculate_area
import math


class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle._is_right_triangle())

    def test_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle._is_right_triangle())

    def test_calculate_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), math.pi * 25)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6)


if __name__ == '__main__':
    unittest.main()
