import unittest
from classes.room import Room 
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room_1 = Room("Lizard Lounge")
       self.guest_1 = Guest("Colin the Crooner", 62, 34.23)
       self.guest_2 = Guest("Sadie the Screamer", 38, 62.89)
       self.guest_3 = Guest("Tuneless Wanda", 22, 29.99)

    def test_room_has_name(self):
        self.assertEqual("Lizard Lounge", self.room_1.name)
    
    def test_room_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))