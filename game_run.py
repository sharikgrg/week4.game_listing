from game_db import *
from game_class import *

server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'

list = Game_db(server, database, username, password)

game = Game('GTA', '34.99')
game1 = Game('Tomb Raider', '34.99')
game2 = Game('FIFA 18', '43.99')
lat = game.latitude_api()
long = game.longitude_api()

# list.create_gamelist(game.get_name(), game.get_price(), long, lat)
# list.create_gamelist(game1.get_name(), game1.get_price(), long, lat)
# list.create_gamelist(game2.get_name(), game2.get_price(), long, lat)
# game.latitude()

list.retrieve_all_games()

list.retrieve_one_game('Tomb Raider')