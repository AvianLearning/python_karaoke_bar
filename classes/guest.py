class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name 
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay_entry_fee(self, entry_fee):
        self.wallet -= entry_fee

    def found_favourite_song(self, song_list):
        for song in song_list:
            if song.title == self.favourite_song:
                return "Choooon!"
            
            return "Awww, not the best :-("

    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price

    def sufficient_funds(self, drink):
        if self.wallet >= drink.price:
            return True

