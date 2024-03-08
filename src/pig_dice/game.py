import random
from computer import Computer
from dice import Dice
from player import Player
from save import Save
from exception import ExitGameException
class Game:
    """
    Pig Dice Game:

    This class represents the Pig Dice game. Players take turns rolling a dice
    and accumulating points until someone reaches or exceeds a total score of
    100 points.

    Attributes:
    - cheat: A boolean indicating whether cheat mode is enabled (default False).
    - index: An integer representing the index of the current player.
    - current_score: An integer representing the current score of the player's turn.
    - player1: An instance of the Player class representing the first player.
    - player2: An instance of the Computer class representing the second player.
    - game_played: An integer representing the number of games played.
    - winner: A string representing the name of the winner.
    - player_list: A list containing instances of the Player class.
    """

    def __init__(self,cheat=False):
        """Initialize the Pig Dice Game."""
        self.cheat=cheat
        self.index=0
        self.current_score=0
        self.player1=None
        self.player2=Computer()
        self.game_played=0
        self.winner=''
        self.player_list=[]
    