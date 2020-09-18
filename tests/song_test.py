import unittest
from classes.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Isn't it Pythonic?", "Alanis Morissette")
        self.song_2 = Song("Little Red Rooster", "Jimi Hendrix")

    def test_can_find_song_by_name(self):
        self.assertEqual("Isn't it Pythonic?", self.song_1.title)
    
    def test_can_find_song_by_artist(self):
        self.assertEqual("Alanis Morissette", self.song_1.title)
        self.assertEqual("Jimi Hendrix", self.song_2.title)