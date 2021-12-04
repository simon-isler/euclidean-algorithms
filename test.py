import unittest
from algorithm import *


class EuclideanAlgorithms(unittest.TestCase):
    a = 1581
    b = 1479

    def test_gcd(self):
        self.assertEqual(gcd(self.a, self.b), 51)
        self.assertEqual(gcd(self.b, self.a), 51)

    def test_extended_euclidean_algorithm(self):
        x, y = extended_euclidean_algorithm(self.a, self.b)
        self.assertEqual(x, -14)
        self.assertEqual(y, 15)
        self.assertEqual(x * self.a + y * self.b, gcd(self.a, self.b))  # –14∙1581 + 15∙1479 = 51

        # tests that the greater number of the params a and b gets multiplied with x
        x, y = extended_euclidean_algorithm(self.b, self.a)
        self.assertEqual(x, -14)
        self.assertEqual(y, 15)
        self.assertEqual(x * self.a + y * self.b, gcd(self.a, self.b))  # –14∙1581 + 15∙1479 = 51
