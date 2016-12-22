import json
import requests

API_HOST = 'https://api.yelp.com'
TOKEN_PATH = '/oauth2/token'
SEARCH_PATH = '/v3/businesses/search'

GRANT_TYPE = 'client_credentials'

class Yelp(object):

    def __init__(self, client_id, client_secret):
        self.access_token = self.get_access_token(client_id, client_secret)

    def get_access_token(self, client_id, client_secret):
        url = '{}{}'.format(API_HOST, TOKEN_PATH)
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': GRANT_TYPE
        }
        resp = requests.post(url, data=data)
        return resp.json()['access_token']

    def get_request(self, url, params=None, headers=None):
        if headers is None:
            headers = {}
        headers['Authorization'] = 'Bearer {}'.format(self.access_token)
        resp = requests.get(url, params=params, headers=headers)
        return resp.json()

    def search(self, name, location=None):
        url = '{}{}'.format(API_HOST, SEARCH_PATH)
        params = {
            'term': name
        }

        if location is not None:
            params['location'] = location
        return self.get_request(url, params=params)
