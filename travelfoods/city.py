import restaurant
from yelp import Yelp

class City(object):

    def __init__(self, keys, city_name, restaurants_to_find=None):
        self.restaurant_list = []
        self.yelp = Yelp(keys['client_id'], keys['client_secret'])
        self.city_name = city_name

        for restaurant in restaurants_to_find:
            self.add_restaurant(restaurant)

    def add_restaurant(self, restaurant_name):
        search_results = self.yelp.search(restaurant_name, self.city_name)['businesses']

        if len(search_results) == 0:
            return None

        # maybe dumb
        business = search_results[0]
        params = {
            restaurant.RESTAURANT_NAME: business['name'],
            restaurant.RESTAURANT_RATING: business['rating'],
            restaurant.RESTAURANT_REVIEW_COUNT: business['review_count'],
            restaurant.RESTAURANT_CUISINE: business['categories'][0]['alias'],
            restaurant.RESTAURANT_LINK: business['url'].split('?')[0],
            restaurant.RESTAURANT_LOCATION: business['location']['city'],
            restaurant.RESTAURANT_PRICE: business['price']
        }
        self.restaurant_list.append(restaurant.Restaurant(params))

    def output_restaurants(self):
        result = ""
        result += restaurant.Restaurant.getCsvHeader()
        for r in self.restaurant_list:
            result += r.toCsvLine()
        return result
