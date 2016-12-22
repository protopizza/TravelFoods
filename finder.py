import json
from travelfoods import City
from travelfoods import Restaurant

KEYS_FILE = 'keys.json'

with open(KEYS_FILE, 'r') as json_file:
    keys = json.load(json_file)

city = City("vancouver", keys)
restaurants = []
restaurants.append(city.find("maumi"))
restaurants.append(city.find("kirin"))
restaurants.append(city.find("miku"))

print Restaurant.getCsvHeader()
for r in restaurants:
    print r.toCsvLine()
