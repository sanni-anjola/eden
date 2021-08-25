import unittest

from models.Credit_Card_Information import Credit_Card_Information


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self) -> None:
        self.credit_card_information = Credit_Card_Information("233", "2025", "08", "0123444233", "saving", "verve")

    def test_Credit_Card_Information_has_cvv_card(self):
        self.assertEqual(self.credit_card_information.cvv_card, "233")

    def test_Credit_Card_Information_has_card_expiration_year(self):
        self.assertEqual(self.credit_card_information.card_expiration_year, "2025")

    def test_Credit_Card_Information_has_card_expiration_month(self):
        self.assertEqual(self.credit_card_information.card_expiration_month, "08")

    def test_Credit_Card_Information_has_credit_card_number(self):
        self.assertEqual(self.credit_card_information.credit_card_number, "0123444233")

    def test_Credit_Card_Information_has_name_on_card(self):
        self.assertEqual(self.credit_card_information.name_on_card, "saving")

    def test_Credit_Card_Information_has_card_type(self):
        self.assertEqual(self.credit_card_information.card_type, "verve")


if __name__ == '__main__':
    unittest.main()
