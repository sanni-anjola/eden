class Billing_Information:
    def __init__(self, recievers_phone_number, reciever_name, delivery_address, credit_card_information=None):
        self.recievers_phone_number = recievers_phone_number
        self.reciever_name = reciever_name
        self.delivery_address = delivery_address
        self.credit_card_information = credit_card_information