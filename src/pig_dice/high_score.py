"""This modulo has methood for displaying highscore."""
import json


def load_json_data(filename):
    """
    Load JSON data from a file.

    Parameters:
    - filename (str): The name of the JSON file to load.

    Returns:
    - dict: The loaded JSON data.

    Raises:
    - FileNotFoundError: If the JSON file does not exist.
    - ValueError: If the JSON file is empty or has invalid JSON data.
    - IOError: If an error occurs while reading the JSON file.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("The JSON file does not exist.")
    except json.decoder.JSONDecodeError:
        raise ValueError("The JSON file is empty or has invalid JSON data.")
    except IOError:
        raise IOError("An error occurred while reading the JSON file.")


def calculate_high_scores(json_data):
    """
    Calculate high scores based on the number of wins for each player.

    Parameters:
    - json_data (dict): The loaded JSON data.

    Returns:
    - list: A sorted list of tuples containing player names and their
    corresponding win counts, sorted in descending order of wins.
    """
    player_wins = {}
    if json_data:
        for game_record in json_data:
            game = game_record.get('game', {})
            for player_key in game:
                player = game[player_key]
                if isinstance(player, dict):
                    player_name = player.get('name')
                    won = player.get('won', 0)
                    player_wins[player_name] = (
                        player_wins.get(player_name, 0) + won)
    return sorted(player_wins.items(), key=lambda x: x[1], reverse=True)


def generate_high_score_list(sorted_players):
    """
    Generate and display the high score list.

    Parameters:
    - sorted_players (list): A sorted list of tuples containing player names
    and their corresponding win counts.

    Returns:
    None
    """
    if sorted_players:
        print(display())
        for rank, (player, wins) in enumerate(sorted_players, start=1):
            print(display_high_score(rank, player, wins))
    else:
        print("High Score List:\nEmpty")


def load(filename="game_history.json"):
    """
    Load game history, calculate high scores, and display the high score list.

    Parameters:
    - filename (str): The name of the JSON file tos
    load (default: "game_history.json")

    Returns:
    None
    """
    try:
        json_data = load_json_data(filename)
        sorted_players = calculate_high_scores(json_data)
        generate_high_score_list(sorted_players)
    except (FileNotFoundError, ValueError, IOError) as e:
        print(str(e))


def display_high_score(rank, player, wins):
    """
    Format a single high score entry.

    Parameters:
    - rank (int): The rank of the player.
    - player (str): The name of the player.
    - wins (int): The number of wins for the player.

    Returns:
    - str: The formatted high score entry.
    """
    return f"""    {rank}. {player:<12}: {wins} wins"""


def display():
    """
    Generate the header of the high score list.

    Returns:
    - str: The header of the high score list.
    """
    return """
       HIGH SCORE LIST
*------------------------------*"""
