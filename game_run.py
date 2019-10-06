from game_db import *
from game_class import *

server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'

list = Game_db(server, database, username, password)

game = Game('GTA', '34.99')
lat = game.latitude_api()
long = game.longitude_api()

list.create_gamelist(game.get_name(), game.get_price(), long, lat)
# game.latitude()