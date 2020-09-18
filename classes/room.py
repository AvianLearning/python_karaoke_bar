class Room:
    
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []
    
    def check_in_guest(self, guest):
        self.guest_list.append(guest)