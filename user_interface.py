from game_db import *
from game_class import *
import time
#### connecting to the SQL server###
server = 'localhost,1433'
database = 'Games'
username = 'SA'
password = 'Passw0rd2018'
game_db = listing_server = Game_db(server, database, username, password)

choice = ' '
while choice != 5:
    print('Welcome to Sparta Global game shop')
    time.sleep(1)
    choice = int(input('1 to read all listing, 2 to look for a particular game, 3 to create a game listing and add it to database, 4 to update listings, 5 to exit: '))

    if choice == 1:
        while choice != 2:
            choice = int(input('choose 1 to retrieve all, 2 to go back to the main menu: '))
            if choice == 1:
                game_db.retrieve_all_games()
            elif choice == 2:
                print('Going back to the main menu')
                time.sleep(1)
            else:
                print('choose a valid number')

    elif choice == 2:
        while choice != 2:
            choice = int(input('choose 1 to look for game, 2 to go back to the main menu: '))
            if choice == 1:
                name = input('what is the name of the game? ')
                game_db.retrieve_one_game(name)
            elif choice == 2:
                print('Going back to the main menu')
                time.sleep(1)
            else:
                print('choose a valid number')

    elif choice == 3:
        while choice != 2:
            choice = int(input('choose 1 to insert game, 2 to go back to the main menu: '))
            if choice == 1:
                name = input('GameName: ')
                price = float(input('Price: '))
                game = Game(name, price)
                listing_server.create_gamelist(game.get_name(), game.get_price(), game.longitude_api(), game.latitude_api())
                print('GAME HAS BEEN ADDED')
            elif choice == 2:
                print('Going back to the main menu')
                time.sleep(1)
            else:
                print('choose a valid number')

    elif choice == 4:
        while choice != 2:
            choice = int(input('choose 1 to update game, 2 to go back to the main menu: '))
            if choice == 1:
                ID = int(input('Choose the ID of the game you would like to change: '))
                Name = input('Type the new name of the game: ')
                listing_server.update_gamename(Name, ID)
                print('GAME HAS BEEN UPDATED')
            elif choice == 2:
                print('Going back to the main menu')
                time.sleep(1)
            else:
                print('choose a valid number')


    elif choice == 5:
        print('Exitting')
        time.sleep(1)
        break

    else:
        print('Choose a Valid number')