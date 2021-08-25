import unittest

from models.Address import Address


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self) -> None:
        self.address = Address(312, "Herbert Macaulay Way", "Sabo Yaba", "Lagos", "Nigeria")

    def test_address_has_house_number(self):
        self.assertEqual(self.address.house_number, 312)

    def test_address_has_street_name(self):
        self.assertEqual(self.address.street_name, "Herbert Macaulay Way")

    def test_address_has_city_name(self):
        self.assertEqual(self.address.city_name, "Sabo Yaba")

    def test_address_has_state(self):
        self.assertEqual(self.address.state, "Lagos")

    def test_address_has_country_name(self):
        self.assertEqual(self.address.country_name, "Nigeria")


if __name__ == '__main__':
    unittest.main()
