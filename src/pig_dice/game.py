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
        
    def play(self):
        """Start the game and handle player interactions."""
        while True:
            try:
                print(self.display())
                choice=self.take_choice_menu()
                if choice == '1':
                    player1,player2=self.set_player_multi()
                    self.player1=player1
                    self.player2=player2
                    self.player_list=[self.player1,self.player2]
                    while True:
                        try:
                            print(self.display_multiplay())
                            choice2=self.take_choice_menu()
                            if choice2== '1':
                                self.multiplay()
                            elif choice2 == '2':
                                self.multiplay_change_name()
                            elif choice2 == '3':
                                if self.game_played != 0:
                                    Save().save(self.player1,self.player2,self.game_played)
                                    self.game_played=0
                                    
                                break
                            else:
                                raise ValueError("\nInvalid input! Enter a number from the listed options.\n ")
                        except ValueError as e:
                            print(e)

                elif choice == '2':
                
                    self.player1=self.set_player_single()
                    self.computer=Computer()
                    self.player_list=[self.player1,self.computer]

                    while True:
                        try:
                            print(self.single_game_menu())
                            choice2=self.take_choice_menu()
                            if choice2 == '1':
                                self.single_game_intro("Easy")
                                self.single_game(Computer().easy_mode)
                            elif choice2 == '2':
                                self.single_game_intro("Medium")
                                self.single_game(Computer().medium_mode)
                            elif choice2 == '3':
                                self.single_game_intro("Hard")
                                self.single_game(Computer().hard_mode)
                            elif choice2 == '4':
                                self.singleplay_change_name()
                            elif choice2 == '5':
                                if self.game_played != 0:
                                    Save().save(self.player1,self.computer,self.game_played)
                                    self.game_played=0
                                break
                            else:
                                raise ValueError("\nInvalid input! Enter a number from the listed options.\n ")
                        except ValueError as e:
                            print(e)    
                elif choice == "3":
                    break
                else:
                    raise ValueError("\nInvalid input! Enter a number from the listed options.\n")
            except ValueError as e:
                            print(e)
    