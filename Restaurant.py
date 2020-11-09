class Restaurant:
    def __init__(self, name, genre, max_seats, open_t, close_t):
        self.name = name
        self.genre = genre
        self.seats_available = max_seats
        self.MAX_SEATS = max_seats
        self.open_t = open_t
        self.close_t = close_t


    def take_reservation(self, reservation):
        if self.seats_available - reservation.party_size >= 0:
            self.seats_available -= reservation.party_size
            return True
        else:
            return False


    def has_seats(self, num_seats):
        if self.seats_available - num_seats >= 0:
            return True
        else:
            return False

    def reset(self):
        self.seats_available = self.MAX_SEATS

    def has_seats_bad(self, num_seats):
        if self.seats_available - num_seats > 0:
            return True
        else:
            return False