import unittest

from models.Product import Product


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self) -> None:
        self.product = Product("5_000", "2332", "television", "324", "electronic", "5%")

    def test_product_has_price(self):
        self.assertEqual(self.product.price, "5_000")

    def test_product_has_product_id(self):
        self.assertEqual(self.product.product_id, "2332")

    def test_product_has_product_name(self):
        self.assertEqual(self.product.product_name, "television")

    def test_product_has_product_description(self):
        self.assertEqual(self.product.product_description, "324")

    def test_product_has_product_category(self):
        self.assertEqual(self.product.product_category, "electronic")

    def test_product_has_discount(self):
        self.assertEqual(self.product.discount, "5%")


if __name__ == '__main__':
    unittest.main()
