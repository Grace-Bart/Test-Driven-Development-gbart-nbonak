import unittest
from RestaurantsInArea import RestaurantsInArea
from Reservation import Reservation
from Customer import Customer
from Restaurant import Restaurant

class RestaurantTest(unittest.TestCase):
    def set_up(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        self.Restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        res1 = Reservation(customer, 12, 2)
        res2 = Reservation(customer, 12, 12)

    def tear_down(self):
        pass

    def test_seat_reservation_A(self):
        self.Restaurant.seat_reservation(res1)
        self.assertEqual(self.Restaurant.seats_available, 3)

    def test_seat_reservation_B(self):
        self.Restaurant.seat_reservation(res2)
        self.assertEqual(self.Restaurant.seats_available, 0)

    def test_reset(self):
        self.Restaurant.reset()
        self.assertEqual(self.Restaurant.seats_available, self.Restaurant.MAX_SEATS)

class CustomerTest(unittest.TestCase):
    def set_up(self):
        name = "Brian"
        phone_number = "(802)555-1234"

        self.Customer = Customer(name, phone_number)

        restaurant = Restaurant("Tapas", "mexican", 7, 11, 17)

    def tear_down(self):
        pass
    
    def test_make_reservation(self):
        res = self.Customer.make_reservation(restaurant, 15, 7)
        self.assertEqual(res.customer, "Brian")
        self.assertEqual(res.time, 15)
        self.assertEqual(res.party_size, 7)

class RestaurantsInAreaTest(unittest.TestCase):
    def set_up(self):
        self.RestaurantsInArea = RestaurantsInArea()
        #self.RestaurantsInArea.add_restaurant()

    def tear_down(self):

    def test_(self):
        assert RestaurantsInArea.
class ReservationTest(unittest.TestCase):
    def set_up(self):

    def tear_down(self):


