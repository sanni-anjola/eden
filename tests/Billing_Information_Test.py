import unittest

from models.Billing_Information import Billing_Information


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self) -> None:
        self.billing_Information = Billing_Information("08023344455", "Blessing Ayo", "Iyana Ipaja")

    def test_billing_information_has_recievers_phone_number(self):
        self.assertEqual(self.billing_Information.recievers_phone_number, "08023344455")

    def test_billing_information_has_recievers_name(self):
        self.assertEqual(self.billing_Information.reciever_name, "Blessing Ayo")

    def test_billing_information_has_delivery_address(self):
        self.assertEqual(self.billing_Information.delivery_address, "Iyana Ipaja")


if __name__ == '__main__':
    unittest.main()
