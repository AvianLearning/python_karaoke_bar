class KaraokeBar:
    def __init__(self, name, room_list, till):
        self.name = name
        self.room_list = room_list
        self.till = till

    def collect_entry_fee(self, guest, entry_fee):
        self.till += entry_fee
        guest.pay_entry_fee(entry_fee)


