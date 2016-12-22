#!/usr/bin/env python

import argparse
import json
from travelfoods import City

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key-file', default="keys.json", help="JSON file containing client_id and client_secret. Default: %(default)s")
    parser.add_argument('-c', '--city', required=True, help="City to search for restaurants in.")
    parser.add_argument('-o', '--output-file', help="Output file. If not specified, outputs to console.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-r', '--restaurants', nargs="+", help="List of restaurants to search for.")
    group.add_argument('-f', '--restaurants-file', help="File with list of newline-delimited restaurants.")
    args = parser.parse_args()

    with open(args.key_file, 'r') as json_file:
        keys = json.load(json_file)

    if args.restaurants:
        restaurants_list = args.restaurants
    else:
        content = open(args.restaurants_file, 'r').read()
        restaurants_list = content.strip().split('\n')

    city = City(keys, args.city, restaurants_list)
    result = city.output_restaurants()
    if args.output_file:
        with open(args.output_file, 'w') as output_file:
            output_file.write(result)
    else:
        print result

if __name__ == '__main__':
    main()
