class KaraokeBar:
    def __init__(self, name, room_list, till, entry_fee):
        self.name = name
        self.room_list = room_list
        self.till = till
        self.entry_fee = entry_fee
        self.drinks_list = []

    def collect_entry_fee(self, guest):
        self.till += self.entry_fee
        guest.pay_entry_fee(self.entry_fee)
    
    def add_drink(self, drink):
        self.drinks_list.append(drink)
    
    def count_drinks(self):
        return len(self.drinks_list)

    def sell_drink(self, guest, drink):
        if self.count_drinks == 0:
            return
        if self.guest_can_afford_drink(guest, drink):
            self.drinks_list.remove(drink)
            guest.buy_drink(drink)
            self.till += drink.price

    def guest_can_afford_drink(self, guest, drink):
        return guest.sufficient_funds(drink)