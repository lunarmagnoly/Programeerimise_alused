

class Statistics:
    """
    Statistics class.
    Main class that stores statistics about board games.
    """
    def __init__(self, filename):
        self.players = {}
        self.games = {}
        self.total_games = 0
        self.result_type_counts = {
            "points": 0,
            "places": 0,
            "winner": 0
        }
        self.read_file(filename)
    def get(self, path:str):
        parts = path.strip("/").split("/")

        if parts[0] == "players":
            return list(self.players.keys())
        if parts[0] == "games":
            return list(self.games.keys())
        if parts[0] == "total":
            if len(parts) == 1:
                return self.total_games
            else:
                result_type = parts[1]
                return self.result_type_counts[result_type]

    def read_file(self, filename):
        """
        Reads data from file.
        """
        with open (filename, encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                game_name, player_names, result_type, result = line.split(";")
                players = player_names.split(",")
                results = result.split(",")
                if game_name not in self.games:
                    self.games[game_name] = Game(game_name)
                for player_name in players:
                    if player_name not in self.players:
                        self.players[player_name] = Player(player_name)
                    self.players[player_name].amount += 1
                self.games[game_name].amount += 1
                self.total_games += 1
                self.result_type_counts[result_type] += 1



class Player:
    """
    Player class.
    Stores information about the player.
    """
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.wins = 0
        self.games = {}


class Game:
    """
    Game class.
    Stores information about the game.
    """
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.player_amounts = {}
        self.wins = {}
        self.losses = {}