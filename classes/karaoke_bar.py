class KaraokeBar:
    def __init__(self, name, room_list, till, entry_fee):
        self.name = name
        self.room_list = room_list
        self.till = till
        self.entry_fee = entry_fee

    def collect_entry_fee(self, guest):
        self.till += self.entry_fee
        guest.pay_entry_fee(self.entry_fee)


