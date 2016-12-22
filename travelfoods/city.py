import restaurant
from yelp import Yelp

class City(object):

    def __init__(self, city_name, keys):
        self.city_name = city_name
        self.yelp = Yelp(keys['client_id'], keys['client_secret'])

    def find(self, restaurant_name):
        search_results = self.yelp.search(restaurant_name, self.city_name)['businesses']

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

        return restaurant.Restaurant(params)
