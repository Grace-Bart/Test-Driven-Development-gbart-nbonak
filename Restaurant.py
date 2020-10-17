class Restaurant:
    def __init__(self, name, genre, seats_available, max_seats, open_t, close_t, reservations):
        self.name = name
        self.genre = genre
        self.seats_available = seats_available
        self.MAX_SEATS = max_seats
        self.open_t = open_t
        self.close_t = close_t
        self.reservations = reservations

    def seat_reservation(self):
        pass

    def reset(self):
        pass