# Listing game and Geo Location API:

- As a user I can Create a game to the listing 
- As a user I can read one game from the listing
- As a user I can read all game from the listing
- As a user I can obtain geolocation for 125 london wall




London wall 125 –> geocoding api -> (lat and log on bd)
Game_advert_listing 

# Description:

This project consists of two different classes, hard coded run file and a user_interface file.

- game_db is a Database class, which is used to connect the pycharm to SQL server.
    - It also consists of methods that can cursor.execute(queries)
- game_class is a Game class. It is used to get the information from users, to insert into the database.
    - This class also has methods that gets information from API via .json() 
- game_run is a file that is hardcoded, to see if the methods from the classes are working or not.
- user_interface file, contains the methods from the classes within the while loops and if statements.