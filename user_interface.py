from game_db import *
from game_class import *
#### connecting to the SQL server###
server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'
game_db = listing_server = Game_db(server, database, username, password)

choice = ' '
while choice != 4:
    choice = int(input('1 to read all listing, 2 to look for a particular game, 3 to create a game listing and add it to database, 4 to exit: '))
    if choice == 1:
        game_db.retrieve_all_games()
    elif choice == 2:
        name = input('what is the name of the game? ')
        game_db.retrieve_one_game(name)
    elif choice == 3:
        name = input('GameName: ')
        price = float(input('Price: '))
        game = Game(name, price)
        listing_server.create_gamelist(game.get_name(), game.get_price(), game.longitude_api(), game.latitude_api())
        print('GAME HAS BEEN ADDED')
    else:
        break
