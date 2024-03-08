"""Represents a player in the game."""


class Player:
    """Attributes."""

    """- name (str): The name of the player.
    - score (int): The current score of the player.
    - num_rolls (int): The number of times the player has rolled the dice.
    - num_holds (int): The number of times the player has held their turn.
    - game_won (int): The number of games won by the player.
    """

    def __init__(self, name):
        """
        Initialize a player with a given name.

        Parameters:
        - name (str): The name of the player.

        Returns:
        None
        """
        self.name = name
        self.score = 0
        self.num_rolls = 0
        self.num_holds = 0
        self.game_won = 0

    def set_name(self, name):
        """
        Set the name of the player.

        Parameters:
        - name (str): The name to set.

        Returns:
        None
        """
        self.name = name

    def get_name(self):
        """
        Get the name of the player.

        Returns:
        str: The name of the player.
        """
        return self.name

    def get_score(self):
        """
        Get the  score of the player.

        Returns:
        int: The score of the player.
        """
        return self.score

    def set_score(self, num):
        """
        Set the score of the player.

        Parameters:
        - num (int): The score to set.

        Returns:
        None
        """
        self.score += num

    def new_game(self):
        """Reset."""
        """the player's score, number of rolls, and number of holds for
        a new game.

        Returns:
        None
        """
        self.score = 0
        self.num_rolls = 0
        self.num_holds = 0

    def get_num_rolls(self):
        """
        Get the number of rolls made by the player.

        Returns:
        int: The number of rolls made by the player.
        """
        return self.num_rolls

    def set_num_rolls(self):
        """
        Increment the number of rolls made by the player.

        Returns:
        None
        """
        self.num_rolls += 1

    def get_game_won(self):
        """
        Get the number of games won by the player.

        Returns:
        int: The number of games won by the player.
        """
        return self.game_won

    def set_game_won(self):
        """
        Increment the number of games won by the player.

        Returns:
        None
        """
        self.game_won += 1

    def get_num_holds(self):
        """
        Get the number of holds made by the player.

        Returns:
        int: The number of holds made by the player.
        """
        return self.num_holds

    def set_num_holds(self):
        """
        Increment the number of holds made by the player.

        Returns:
        None
        """
        self.num_holds += 1
