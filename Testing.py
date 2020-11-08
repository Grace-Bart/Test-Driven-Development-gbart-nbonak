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

        self.res1 = Reservation(customer, 12, 2)
        self.res2 = Reservation(customer, 12, 12)
        self.res3 = Reservation(customer, 12, 3)

    def tear_down(self):
        pass

    def test_take_reservation_A(self):
        self.Restaurant.take_reservation(self.res1)
        self.assertEqual(self.Restaurant.seats_available, 3)

    def test_take_reservation_B(self):
        self.Restaurant.take_reservation(self.res2)
        self.assertEqual(self.Restaurant.seats_available, 3)

    def test_take_reservationC(self):
        self.Restaurant.take_reservation(self.res3)
        self.assertEqual(self.Restaurant.seats_available, 0)

    def test_has_seatsA(self):
        self.Restaurant.reset()
        self.assertEqual(self.Restaurant.has_seats(self, 3), True)

    def test_has_seatsB(self):
        self.Restaurant.reset()
        self.assertEqual(self.Restaurant.has_seats(self, 50), False)

    def test_has_seatsC(self):
        self.Restaurant.reset()
        self.assertEqual(self.Restaurant.has_seats(self, 5), True)

    def test_reset(self):
        self.Restaurant.reset()
        self.assertEqual(self.Restaurant.seats_available, self.Restaurant.MAX_SEATS)


class CustomerTest(unittest.TestCase):
    def set_up(self):
        name = "Brian"
        phone_number = "(802)555-1234"

        self.customer = Customer(name, phone_number)

        self.restaurant = Restaurant("Tapas", "mexican", 7, 11, 17)

    def tear_down(self):
        pass

    def test_make_reservation(self):
        self.res = self.customer.make_reservation(self.restaurant, 15, 7)
        self.assertEqual(self.res.customer, "Brian")
        self.assertEqual(self.res.time, 15)
        self.assertEqual(self.res.party_size, 7)


class RestaurantsInAreaTest(unittest.TestCase):
    def set_up(self):
        self.restaurant1 = Restaurant("Friendly's", "American", 20, 10, 20)
        self.restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        self.restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        self.RestaurantsInArea = RestaurantsInArea([self.restaurant1, self.restaurant2])

    def tear_down(self):
        pass

    def test_get_restaurants(self):
        assert self.RestaurantsInArea.get_restaurants() == [self.restaurant1, self.restaurant2], "get_restaurants test failed"

    def test_add_restaurantA(self):
        self.RestaurantsInArea.add_restaurant(self.restaurant3)
        assert RestaurantsInArea.get_restaurants()[2] == self.restaurant3, "add_restaurant test failed"

    def test_add_restaurantB(self):
        assert self.RestaurantsInArea.get_restaurants() == [self.restaurant1,
                                                            self.restaurant2, self.restaurant3], "get_restaurants test failed"

    def test_find_restaurant_name(self):
        pass

    def test_find_restaurant_genre(self):
        pass


