"""Board games."""


class Player:
    """Player class."""

    def __init__(self, name):
        """Initialize player."""
        self.player_name = name
        self.games_played = 0
        self.games_won = 0
        self.played_game_counts = {}


class Game:
    """Game class."""

    def __init__(self, name):
        """Initialize game."""
        self.game_name = name
        self.total_plays = 0
        self.player_counts = {}
        self.wins = {}
        self.losses = {}
        self.player_games = {}
        self.high_score = -1
        self.top_player = ""


class Statistics:
    """Statistics class."""

    def __init__(self, filename):
        """Initialize statistics."""
        self.players = {}
        self.games = {}
        self.total_games = 0
        self.result_type_counts = {
            "points": 0,
            "places": 0,
            "winner": 0
        }
        self.read_file(filename)

    def read_file(self, filename):
        """Read the file line by line."""
        with open(filename, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                # Split line data into variables
                game_name, player_list, result_type, result_data = line.split(";")
                players = player_list.split(",")
                results = result_data.split(",")

                # 1. Set up the game
                current_game = self.setup_game_object(game_name, players)

                # 2. Update players statistics
                self.update_players_data(current_game, game_name, players)

                # 3. Figure out winners and losers, then save scores
                self.handle_match_results(current_game, players, result_type, results)

    def setup_game_object(self, game_name, players):
        """Create or get the game and tracks party sizes."""
        if game_name not in self.games:
            self.games[game_name] = Game(game_name)

        current_game = self.games[game_name]
        current_game.total_plays += 1

        # Track how many players are in the game
        num_players = len(players)
        if num_players not in current_game.player_counts:
            current_game.player_counts[num_players] = 1
        else:
            current_game.player_counts[num_players] += 1

        return current_game

    def update_players_data(self, current_game, game_name, players):
        """Goes through players and updates their match counters."""
        for player_name in players:
            # Create player if they don't exist yet
            if player_name not in self.players:
                self.players[player_name] = Player(player_name)

            # Update total matches for this player
            self.players[player_name].games_played += 1

            # Track how many times this player played this specific game
            player_counters = self.players[player_name].played_game_counts
            if game_name not in player_counters:
                player_counters[game_name] = 1
            else:
                player_counters[game_name] += 1

            # Track player's participation inside the Game object
            if player_name not in current_game.player_games:
                current_game.player_games[player_name] = 1
            else:
                current_game.player_games[player_name] += 1

    def find_winner_and_loser(self, current_game, players, result_type, results):
        """Find who won and lost in the current match."""
        if result_type == "points":
            points_list = [int(x) for x in results]

            max_idx = points_list.index(max(points_list))
            min_idx = points_list.index(min(points_list))

            # Track the high score record
            for i, score in enumerate(points_list):
                if score > current_game.high_score:
                    current_game.high_score = score
                    current_game.top_player = players[i]

            return players[max_idx], players[min_idx]

        if result_type == "places":
            return results[0], results[-1]

        if result_type == "winner":
            return results[0], ""

        return "", ""

    def handle_match_results(self, current_game, players, result_type, results):
        """Save wins, losses and update global counters."""
        # Get names from our helper method
        winner, loser = self.find_winner_and_loser(current_game, players, result_type, results)

        # Save scores (Wins and Losses)
        if winner:
            if winner not in current_game.wins:
                current_game.wins[winner] = 1
            else:
                current_game.wins[winner] += 1
            self.players[winner].games_won += 1

        if loser:
            if loser not in current_game.losses:
                current_game.losses[loser] = 1
            else:
                current_game.losses[loser] += 1

        # Update global stats counters
        self.total_games += 1
        if result_type in self.result_type_counts:
            self.result_type_counts[result_type] += 1

    def get_total(self, parts):
        """Return total statistics."""
        if len(parts) == 1:
            return self.total_games
        return self.result_type_counts.get(parts[1], 0)

    def get_list(self, category):
        """Return names list."""
        if category == "players":
            return list(self.players.keys())
        if category == "games":
            return list(self.games.keys())
        return -1

    def get(self, path: str):
        """Route request path."""
        parts = path.strip("/").split("/")

        if parts[0] == "total":
            return self.get_total(parts)

        if parts[0] in ["players", "games"] and len(parts) == 1:
            return self.get_list(parts[0])

        if len(parts) == 3 and parts[0] == "player":
            return self.get_single_player_stat(parts[1], parts[2])

        if len(parts) == 3 and parts[0] == "game":
            return self.get_single_game_stat(parts[1], parts[2])

        return -1

    def get_single_player_stat(self, name: str, stat_type: str):
        """Look up specific stats for a single player by their name."""
        if name not in self.players:
            return 0 if stat_type != "favourite" else ""

        player = self.players[name]
        if stat_type == "amount":
            return player.games_played
        if stat_type == "won":
            return player.games_won
        if stat_type == "favourite":
            if not player.played_game_counts:
                return ""

            # Find which game they played the most
            max_plays = -1
            fav_game = ""
            for g_name, count in player.played_game_counts.items():
                if count > max_plays:
                    max_plays = count
                    fav_game = g_name
            return fav_game
        return -1

    def get_single_game_stat(self, name: str, stat_type: str):
        """Return statistics for one player."""
        if name not in self.games:
            return 0

        game = self.games[name]

        if stat_type == "amount":
            return game.total_plays

        if stat_type == "player-amount":
            return max(game.player_counts, key=game.player_counts.get)

        if stat_type == "most-wins":
            return max(game.wins, key=game.wins.get)

        if stat_type == "most-frequent-winner":
            return max(game.wins, key=lambda p: game.wins[p] / game.player_games[p])

        if stat_type == "most-losses":
            return max(game.losses, key=game.losses.get)

        if stat_type == "most-frequent-loser":
            return max(game.losses, key=lambda p: game.losses[p] / game.player_games[p])

        if stat_type == "record-holder":
            return game.top_player

        return -1

    def get_global_players_stat(self, stat_type: str):
        """Return global player statistics."""
        if not self.players:
            return -1

        if stat_type == "player-amount":
            return len(self.players)

        if stat_type == "most-wins":
            return max(self.players.values(),
                       key=lambda p: p.games_won).player_name

        if stat_type == "most-frequent-winner":
            return max(
                self.players.values(),
                key=lambda p: p.games_won / p.games_played
            ).player_name

        return -1

    def get_global_games_stat(self, stat_type: str):
        """Calculate global records for games."""
        if not self.games:
            return ""

        if stat_type == "record-holder":
            best_score = -1
            holder = ""
            for game in self.games.values():
                if game.high_score > best_score:
                    best_score = game.high_score
                    holder = game.top_player
            return holder

        return -1