import unittest
from RestaurantsInArea import RestaurantsInArea
from Reservation import Reservation
from Customer import Customer
from Restaurant import Restaurant


class RestaurantTest(unittest.TestCase):
    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_take_reservation_A(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        res1 = Reservation(customer, 12, 2)

        restaurant.take_reservation(res1)
        self.assertEqual(restaurant.seats_available, 3)

    def test_take_reservation_B(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        res1 = Reservation(customer, 12, 12)

        restaurant.take_reservation(res1)
        self.assertEqual(restaurant.seats_available, 5)

    def test_take_reservationC(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        res1 = Reservation(customer, 12, 2)
        res2 = Reservation(customer, 12, 3)

        restaurant.take_reservation(res1)
        restaurant.take_reservation(res2)
        self.assertEqual(restaurant.seats_available, 0)

    def test_has_seatsA(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        res1 = Reservation(customer, 12, 2)

        restaurant.take_reservation(res1)
        self.assertEqual(restaurant.has_seats(3), True)

    def test_has_seatsB(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        self.assertEqual(restaurant.has_seats(50), False)

    def test_has_seatsC(self):

        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        self.assertEqual(restaurant.has_seats(5), True)

    def test_has_seats_bad(self):

        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        self.assertEqual(restaurant.has_seats_bad(5), True)


    def test_reset(self):
        name = "Carla's"
        genre = "Diner"
        max_seats = 5
        open_t = 6
        close_t = 15

        restaurant = Restaurant(name, genre, max_seats, open_t, close_t)

        customer = Customer("George", "(802)555-5555")

        res1 = Reservation(customer, 12, 2)
        res2 = Reservation(customer, 12, 3)

        restaurant.take_reservation(res1)
        restaurant.take_reservation(res2)
        restaurant.reset()
        self.assertEqual(restaurant.seats_available, restaurant.MAX_SEATS)


class CustomerTest(unittest.TestCase):
    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_make_reservation(self):
        name = "Brian"
        phone_number = "(802)555-1234"

        customer = Customer(name, phone_number)

        restaurant = Restaurant("Tapas", "mexican", 7, 11, 17)

        res = customer.make_reservation(restaurant, 15, 7)
        self.assertEqual(res.customer.name, "Brian")
        self.assertEqual(res.time, 15)
        self.assertEqual(res.party_size, 7)


class RestaurantsInAreaTest(unittest.TestCase):
    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_get_restaurantsA(self):
        restaurant1 = Restaurant("Friendly's", "American", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2])

        assert restaurantsInArea.get_restaurants() == [restaurant1, restaurant2], "get_restaurants test failed"

    def test_get_restaurantB(self):
        restaurant1 = Restaurant("Friendly's", "American", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2])

        restaurantsInArea.add_restaurant(restaurant3)
        assert restaurantsInArea.get_restaurants() == [restaurant1,
                                                        restaurant2, restaurant3], "get_restaurants test failed"

    def test_add_restaurantA(self):
        restaurant1 = Restaurant("Friendly's", "American", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2])

        restaurantsInArea.add_restaurant(restaurant3)
        assert restaurantsInArea.get_restaurants()[2] == restaurant3, "add_restaurant test failed"


    def test_find_restaurant_nameA(self):
        restaurant1 = Restaurant("Friendly's", "Diner", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2, restaurant3])

        assert restaurantsInArea.find_restaurant_name("Denny's") == restaurant2, "find_restaurant_name test failed"

    def test_find_restaurant_nameB(self):
        restaurant1 = Restaurant("Friendly's", "American", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2, restaurant3])

        assert restaurantsInArea.find_restaurant_name("Smorgasbord") == False, "find_restaurant_name test failed"

    def test_find_restaurant_genreA(self):
        restaurant1 = Restaurant("Friendly's", "Diner", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2, restaurant3])

        assert restaurantsInArea.find_restaurant_genre("Diner") == [restaurant1, restaurant2] , "find_restaurant_genre test failed"

    def test_find_restaurant_genreB(self):
        restaurant1 = Restaurant("Friendly's", "Diner", 20, 10, 20)
        restaurant2 = Restaurant("Denny's", "Diner", 15, 7, 1)
        restaurant3 = Restaurant("Sabai Sabai", "Thai", 203, 11, 22)

        restaurantsInArea = RestaurantsInArea([restaurant1, restaurant2, restaurant3])

        assert restaurantsInArea.find_restaurant_genre("Mexican") == [] , "find_restaurant_genre test failed"


