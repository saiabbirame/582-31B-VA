# CLASS 1
class Playlist:
    def __init__(self, name, song_count = 0):
        self.name = name
        self.song_count = song_count

    def add_song(self):
        self.song_count += 1

    def remove_song(self):
        self.song_count -= 1

    def show_info(self):
        print(self.name, "-", self.song_count, "songs")

# TEST
playlist = Playlist("Your Playlist")
playlist.add_song()
playlist.add_song()
playlist.remove_song()
playlist.show_info()

# CLASS 2
class ShoppingCart:
    def __init__(self, owner, item_count = 0):
        self.owner = owner
        self.item_count = item_count

    def add_item(self, quantity):
        self.item_count += quantity

    def remove_item(self, quantity):
        self.item_count -= quantity

    def show_cart(self):
        print(self.owner, "has", self.item_count, "items in their cart")

# TEST
cart = ShoppingCart("Alex")
cart.add_item(9)
cart.remove_item(2)
cart.show_cart()

# CLASS 3
class UserAccount:
    def __init__(self, username, active = False, login_count = 0):
        self.username = username
        self.active = active
        self.login_count = login_count

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False

    def login(self):
        if self.active:
            self.login_count += 1
        else:
            print("Account is not active")

    def show_status(self):
        print(self.username, "- Active:", self.active, "- Logins:", self.login_count)

# TEST
user = UserAccount("abc123")
user.activate()
user.deactivate()
user.login()
user.login()
user.login()
user.login()
user.show_status()

user2 = UserAccount("defg4567")
user2.activate()
user2.deactivate()
user2.activate()
user2.login()
user2.login()
user2.show_status()