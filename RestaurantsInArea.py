class RestaurantsInArea:
    def __init__(self, restaurants):
        self.restaurants = restaurants

    def get_restaurants(self):
        return self.restaurants

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def remove_restaurant(self, restaurant):
        self.restaurants.remove(restaurant)

    def find_restaurant_name(self, name):
        for i in range(len(self.restaurants)):
            if self.restaurants[i].name == name:
                return self.restaurants[i]
        return False


    def find_restaurant_genre(self, genre):
        genre_list = []
        for i in range(len(self.restaurants)):
            if self.restaurants[i].genre == genre:
                genre_list.append(self.restaurants[i])
        return genre_list