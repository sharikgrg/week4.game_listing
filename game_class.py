import requests
## This class is used for API to give geolocation and also to give in game details
class Game:
    def __init__(self, name, price, postcode, location = '125 London Wall'):
        self.name = name
        self.price = price
        self.location = location
        self.postcode = postcode

    def get_name(self):
        return str(self.name)

    def get_price(self):
        return float(self.price)

    def latitude_api(self):
        request_postcode = requests.get(f'http://api.postcodes.io/postcodes/{self.postcode}')
        latitude = request_postcode.json()
        return float(latitude['result']['latitude'])

    def longitude_api(self):
        request_postcode = requests.get(f'http://api.postcodes.io/postcodes/{self.postcode}')
        longitude = request_postcode.json()
        return float(longitude['result']['longitude'])
