import unittest
from classes.guest import Guest 
from classes.karaoke_bar import KaraokeBar

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Colin the Crooner", 62, 34.23)

    def test_can_find_guest_by_name(self):
        self.assertEqual("Colin the Crooner", self.guest_1.name)

    def test_entry_fee_deducted_from_guest_wallet(self):
        fee = 10.00
        self.guest_1.pay_entry_fee(fee)
        self.assertEqual(24.23, round(self.guest_1.wallet, 2))
