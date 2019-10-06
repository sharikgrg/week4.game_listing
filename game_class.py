import requests
import json
class Game:
    def __init__(self, name, price, location = '125 London Wall'):
        self.name = name
        self.price = price
        self.location = location

    def get_name(self):
        return str(self.name)

    def get_price(self):
        return float(self.price)

    def latitude_api(self):
        request_postcode = requests.get('http://api.postcodes.io/postcodes/EC2Y5AS')
        latitude = request_postcode.json()
        return float(latitude['result']['latitude'])

    def longitude_api(self):
        request_postcode = requests.get('http://api.postcodes.io/postcodes/EC2Y5AS')
        longitude = request_postcode.json()
        return float(longitude['result']['longitude'])
