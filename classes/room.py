class Room:
    
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []
    
    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_song_list(self, song):
        self.song_list.append(song)
    
    