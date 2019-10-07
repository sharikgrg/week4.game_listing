from game_db import *
from game_class import *
#### connecting to the SQL server###
server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'
listing_server = Game_db(server, database, username, password)

### Entering data into Game class)
game = Game('GTA', '34.99')
game1 = Game('Tomb Raider', '34.99')
game2 = Game('FIFA 18', '43.99')

### obtaining latitude and longitude by methods in Game class
lat = game.latitude_api()
long = game.longitude_api()

### As a User I can create and add a game to the database###
# listing_server.create_gamelist(game.get_name(), game.get_price(), long, lat)
# listing_server.create_gamelist(game1.get_name(), game1.get_price(), long, lat)
# listing_server.create_gamelist(game2.get_name(), game2.get_price(), long, lat)
# game.latitude()

## As a user i can read all games list
listing_server.retrieve_all_games()


## AS a user I can read one game
listing_server.retrieve_one_game('Tomb Raider')

## Updating Game name using ID
listing_server.update_gamename('GTA V', 1)