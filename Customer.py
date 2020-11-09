from Reservation import Reservation
from Restaurant import Restaurant

class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def make_reservation(self, restaurant, time, party_size):
        res = Reservation(self, time, party_size)
        restaurant.take_reservation(res)
        return res
