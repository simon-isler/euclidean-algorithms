import unittest
from algorithm import *


class EuclideanAlgorithms(unittest.TestCase):
    x = 1581
    y = 1479

    def test_gcd(self):
        self.assertEqual(gcd(self.x, self.y), 51)

    def test_extended_euclidean_algorithm(self):
        a, b = extended_euclidean_algorithm(self.x, self.y)
        self.assertEqual(a, -14)
        self.assertEqual(b, 15)

        self.assertEqual(-14 * self.x + 15 * self.y, gcd(self.x, self.y))  # –14∙1581 + 15∙1479 = 51
