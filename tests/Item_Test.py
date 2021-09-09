import unittest

from models.Item import Item


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def setUp(self) -> None:
        self.item = Item("1", "bicycle")

    def test_item_has_quantity_of_product(self):
        self.assertEqual(self.item.quantity_of_product, 1)

    def test_item_has_product(self):
        self.assertEqual(self.item.product, "bicycle")


if __name__ == '__main__':
    unittest.main()
