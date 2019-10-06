import pyodbc
# this class is used to connect to any SQL databases and servers, and execute queries
class Game_db:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connect_gamedb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connect_gamedb.cursor()

    def cursor_execute(self, query):
        return self.cursor.execute(query)

    def create_gamelist(self, name = '', price = ' ', longitude = ' ', latitude = ' ', location = '125 London Wall'):
        self.cursor_execute(f"INSERT INTO listing(GameName, Price, Location, Longitude, Latitude) VALUES('{name}', {price}, '{location}', {longitude}, {latitude})")
        self.connect_gamedb.commit()

    def retrieve_all_games(self):
        query = self.cursor_execute("SELECT * FROM listing").fetchall()
        for game in query:
            print(game)

    def retrieve_one_game(self,name):
        query = self.cursor_execute(f"SELECT * FROM listing WHERE GameName like '%{name}%'").fetchone()
        print(query)



