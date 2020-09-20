import unittest
from classes.karaoke_bar import KaraokeBar
from classes.room import Room 
from classes.guest import Guest

class TestKaraokeBar(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Lizard Lounge", 3)
        self.room_2 = Room("Viper's Nest", 10)
        self.room_3 = Room("Clucking Hell", 15)
        room_list = [self.room_1, self.room_2, self.room_3]
        self.karaoke_bar = KaraokeBar("The Hit Re-Factory", room_list, 100.00, 10.00)

    def test_karaoke_bar_can_collect_entry_fee(self):
        guest_1 = Guest("Colin the Crooner", 62, 34.23)
        self.karaoke_bar.collect_entry_fee(guest_1)
        self.assertEqual(110.00, self.karaoke_bar.till) 

        