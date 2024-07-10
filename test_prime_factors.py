from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self):
        self.prime_factor = PrimeFactor()

    def test_get_prime_numbers_from_2_to_20(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19],
                         self.prime_factor.get_prime_numbers_from_2_to_number(20))

    def test_prime_factor_of_1(self):
        self.assertEqual([], self.prime_factor.get_prime_factors(1))

    def test_prime_factor_of_2(self):
        self.assertEqual([2], self.prime_factor.get_prime_factors(2))

    def test_prime_factor_of_5(self):
        self.assertEqual([5], self.prime_factor.get_prime_factors(5))

    def test_prime_factor_of_10(self):
        self.assertEqual([2, 5], self.prime_factor.get_prime_factors(10))

    def test_prime_factor_of_15(self):
        self.assertEqual([3, 5], self.prime_factor.get_prime_factors(15))

    def test_prime_factor_of_20(self):
        self.assertEqual([2, 5], self.prime_factor.get_prime_factors(20))
