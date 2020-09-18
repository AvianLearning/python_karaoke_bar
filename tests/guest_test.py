import unittest
from classes.guest import Guest 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Colin the Crooner", 62, 34.23)

    def test_can_find_guest_by_name(self):
        self.assertEqual("Colin the Crooner", self.guest1.name)
