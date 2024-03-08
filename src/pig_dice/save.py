"""Save Class."""
import json


class Save:
    """Class responsible for saving and loading game history data."""

    game_history = []

    def save(self, player1, player2, played_game, filname="game_history.json"):
        """
        Save game history data to a JSON file.

        Parameters:
        - player1 (Player): The first player object.
        - player2 (Player): The second player object.
        - played_game (str): how many games played.
        - filename (str): The filename to save the data to.

        Default is "game_history.json". """
        game = {
            "game": {
                "player 1": {
                    "name":   player1.get_name(),
                    "won":    player1.get_game_won()
                },
                "player 2": {
                    "name":   player2.get_name(),
                    "won":    player2.get_game_won()
                }, "played game":  played_game

            }
        }
        self.load(filname)
        Save().game_history.append(game)
        with open(filname, 'w') as file:
            json.dump(Save().game_history, file, indent=4)

    def load(self, filname="game_history.json"):
        """Load game history data from a JSON file.

        - filename (str): The filename to load the data from.
        Default is "game_history.json"."""
        try:
            with open(filname, "r") as file:
                try:
                    Save().game_history = json.load(file)
                except json.decoder.JSONDecodeError:
                    # Handle the case where the file is empty
                    print("The JSON file is empty or has invalid JSON data.")
        except FileNotFoundError:
            # Handle the case where the file does not exist
            print("The JSON file does not exist.")
        except IOError:
            # Handle other I/O errors
            print("An error occurred while reading the JSON file.")
