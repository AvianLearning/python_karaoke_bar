import unittest
from classes.guest import Guest 
from classes.room import Room
from classes.karaoke_bar import KaraokeBar

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Colin the Crooner", 62, 34.23)
        self.room_1 = Room("Lizard Lounge", 3)
        self.room_2 = Room("Viper's Nest", 10)
        self.room_3 = Room("Clucking Hell", 15)
        room_list = [self.room_1, self.room_2, self.room_3]
        self.karaoke_bar = KaraokeBar("The Hit Re-Factory", room_list, 100.00, 10.00)

    def test_can_find_guest_by_name(self):
        self.assertEqual("Colin the Crooner", self.guest_1.name)

    def test_entry_fee_deducted_from_guest_wallet(self):
        self.guest_1.pay_entry_fee(self.karaoke_bar.entry_fee)
        self.assertEqual(24.23, round(self.guest_1.wallet, 2))
