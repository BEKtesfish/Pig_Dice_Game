"""Computer Player Class."""
from player import Player
import time
"""This class represents a computer player in the game. It provides different
    playing modes such as easy, medium, and hard.

Attributes:
- name: The name of the computer player.

Methods:
- easy_mode(current_score): Returns 'h' if current score is greater than 20,
    else 'r'.
- medium_mode(current_score): Returns 'h' if current score is greater than or
    equal to 25 when score is 0,
  else 'h' if current score is greater than or equal to 18, else 'r'.
- hard_mode(current_score): Returns 'h' if current score is less than 71 and
    roll score is greater than or equal to 21,
  or if current score is greater than or equal to 71 and roll score is greater
  than or equal to 18, else 'r'.
- sleep(): Introduces a delay of 1.5 seconds to simulate the computer's
 decision-making process.
"""


class Computer(Player):
    """Computer Player Class Represents."""

    """"a computer player in the game."""

    def __init__(self):
        """
        Initialize the Computer Player.

        Sets the name of the computer player to 'computer'.
        """
        super().__init__("computer")

    # easy mode
    def easy_mode(self, current_score):
        """
        Easy Playing Mode.

        Returns 'h' if current score is greater than 20, else 'r'.

        Parameters:
        - current_score (int): The current score of the player.
        """
        self.sleep()
        if current_score > 20:
            return 'h'
        else:
            return 'r'

    # meduim mode
    def medium_mode(self, current_score):
        """
        Medium Playing Mode.

        Returns 'h' if current score is greater than or equal to 25 when score
        is 0, else 'h'
        if current score is greater than or equal to 18, else 'r'.

        Parameters:
        - current_score (int): The current score of the player.
        """
        self.sleep()
        if self.get_score() == 0:
            return 'h' if current_score >= 25 else 'r'
        else:
            return 'h' if current_score >= 18 else 'r'

    # hard mode
    def hard_mode(self, current_score):
        """Hard Playing Mode."""
        """-Returns 'h' if computers overall score is < 71 and current score
            is >= 21 or else if computer overall score >=71 and current score
            is >= 18
        -Returns 'r' if computer overall score  is  < 71 nad current score is
        <21 or else if computer score is >= 71 and
         current score is < 18 s
        Parameters:
        - current_score (int): The current score of the player."""

        self.sleep()
        if self.get_score() < 71:
            return 'h' if current_score >= 21 else 'r'
        elif self.get_score() >= 71:
            return 'h' if current_score >= 18 else 'r'

    def sleep(self):
        """
        Introduces a Delay.

        Introduces a delay of 1.5 seconds to simulate the computer's
        decision-making process.
        """
        time.sleep(1.5)
