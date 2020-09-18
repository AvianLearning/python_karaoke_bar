import unittest
from classes.room import Room 

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room1 = Room("Lizard Lounge")

    def test_room_has_name(self):
        self.assertEqual("Lizard Lounge", self.room1.name)