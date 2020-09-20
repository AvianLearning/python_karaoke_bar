class Guest:

    def __init__(self, name, wallet):
        self.name = name 
        self.wallet = wallet

    def pay_entry_fee(self, entry_fee):
        self.wallet -= entry_fee
