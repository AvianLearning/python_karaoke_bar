import unittest
from classes.karaoke_bar import KaraokeBar
from classes.room import Room 
from classes.guest import Guest
from classes.drink import Drink

class TestKaraokeBar(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Lizard Lounge", 3)
        self.room_2 = Room("Viper's Nest", 10)
        self.room_3 = Room("Clucking Hell", 15)
        room_list = [self.room_1, self.room_2, self.room_3]
        self.karaoke_bar = KaraokeBar("The Hit Re-Factory", room_list, 100.00, 10.00)
        self.drink_1 = Drink("Singha", 5.00)
        self.drink_2 = Drink("Cobra", 4.95)
        self.drink_3 = Drink("Tiger", 4.50)
        self.drink_4 = Drink("Blue WKD", 5.50)
        self.drink_5 = Drink("Red, red wine", 5.95)
        self.drink_6 = Drink("Tequila Sunrise", 8.75)

    def test_karaoke_bar_can_collect_entry_fee(self):
        guest_1 = Guest("Colin the Crooner", 34.23, "Chicken Payback")
        self.karaoke_bar.collect_entry_fee(guest_1)
        self.assertEqual(110.00, self.karaoke_bar.till) 

    def test_entry_fee_reduces_guest_wallet(self):
        self.guest_2 = Guest("Sadie the Screamer", 62.89, "Ruby Tuesday")
        self.karaoke_bar.collect_entry_fee(self.guest_2)
        self.assertEqual(110.00, self.karaoke_bar.till)
        self.assertEqual(52.89, self.guest_2.wallet)   

    def test_can_add_drink_to_drinks_list(self):
        pass