import unittest
from classes.room import Room 
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room_1 = Room("Lizard Lounge")
       self.guest_1 = Guest("Colin the Crooner", 62, 34.23)
       self.guest_2 = Guest("Sadie the Screamer", 38, 62.89)
       self.guest_3 = Guest("Tuneless Wanda", 22, 29.99)
       self.guest_4 = Guest("Robin the Rocker", 54, 9.34)
       self.song_1 = Song("Isn't it Pythonic?", "Alanis Morissette")
       self.song_2 = Song("Little Red Rooster", "Jimi Hendrix")
       self.song_3 = Song("Computer Love", "Kraftwerk")
       self.song_4 = Song("Don't Fear the Repo", "Blue Oyster Cult")

    def test_room_has_name(self):
        self.assertEqual("Lizard Lounge", self.room_1.name)
    
    def test_room_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_room_can_check_in_multiple_guests(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(3, len(self.room_1.guest_list))
    
    def test_room_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(2, len(self.room_1.guest_list))
        
    def test_can_add_songs_to_room_song_list(self):
        self.room_1.add_song_to_song_list(self.song_1)
        self.room_1.add_song_to_song_list(self.song_2)
        self.room_1.add_song_to_song_list(self.song_3)
        self.room_1.add_song_to_song_list(self.song_4)
        self.assertEqual(4, len(self.room_1.song_list))

    def test_room_cannot_fill_over_capacity(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.assertEqual(3, len(self.room_1.guest_list))
