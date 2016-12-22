RESTAURANT_NAME = 'name'
RESTAURANT_RATING = 'rating'
RESTAURANT_REVIEW_COUNT = 'review_count'
RESTAURANT_CUISINE = 'cuisine'
RESTAURANT_LINK = 'link'
RESTAURANT_LOCATION = 'location'
RESTAURANT_PRICE = 'price'

COLUMNS_ORDER = [
    RESTAURANT_NAME,
    RESTAURANT_RATING,
    RESTAURANT_REVIEW_COUNT,
    RESTAURANT_CUISINE,
    RESTAURANT_LINK,
    RESTAURANT_LOCATION,
    RESTAURANT_PRICE
]

class Restaurant(object):
    def __init__(self, fields):
        self.fields = fields

    @staticmethod
    def getCsvHeader():
        return ",".join(COLUMNS_ORDER)

    def toCsvLine(self):
        ordered_fields = []
        for column in COLUMNS_ORDER:
            ordered_fields.append(str(self.fields[column]))
        return ",".join(ordered_fields)
