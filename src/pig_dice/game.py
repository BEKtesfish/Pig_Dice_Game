# -*- coding: utf-8
"""Game class."""
import random
from computer import Computer
from dice import Dice
from player import Player
from save import Save
from exception import ExitGameException
import os
import time


class Game:
    """Pig Dice Game."""

    """This class represents the Pig Dice game. Players take turns rolling a
    dice and accumulating points until someone reaches or exceeds
    a total score of 100 points.

    Attributes:
    - cheat: A boolean indicating whether cheat mode is enabled (default False)
    - index: An integer representing the index of the current player.
    - current_score: An integer representing the current score of the player's
      turn.
    - player1: An instance of the Player class representing the first player.
    - player2: An instance of the Computer class representing the second
    player.
    - game_played: An integer representing the number of games played.
    - winner: A string representing the name of the winner.
    - player_list: A list containing instances of the Player class.
    """

    def __init__(self, cheat=False):
        """Initialize the Pig Dice Game."""
        self.cheat = cheat
        self.index = 0
        self.current_score = 0
        self.player1 = None
        self.player2 = Computer()
        self.game_played = 0
        self.winner = ''
        self.player_list = []

    def play(self):
        """Start the game and handle player interactions."""
        while True:
            try:
                print(self.display())
                choice = self.take_choice_menu()
                if choice == '1':
                    player1, player2 = self.set_player_multi()
                    self.player1 = player1
                    self.player2 = player2
                    self.player_list = [self.player1, self.player2]
                    while True:
                        try:
                            print(self.display_multiplay())
                            choice2 = self.take_choice_menu()
                            if choice2 == '1':
                                self.multiplay()
                            elif choice2 == '2':
                                self.multiplay_change_name()
                            elif choice2 == '3':
                                if self.game_played != 0:
                                    Save().save(self.player1, self.player2,
                                                self.game_played)
                                    self.game_played = 0
                                break
                            else:
                                raise ValueError(self.invalid_input())
                        except ValueError as e:
                            print(e)

                elif choice == '2':
                    self.player1 = self.set_player_single()
                    self.computer = Computer()
                    self.player_list = [self.player1, self.computer]

                    while True:
                        try:
                            print(self.single_game_menu())
                            choice2 = self.take_choice_menu()
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
                                    Save().save(self.player1, self.computer,
                                                self.game_played)
                                    self.game_played = 0
                                break
                            else:
                                raise ValueError(self.invalid_input())
                        except ValueError as e:
                            print(e)
                elif choice == "3":
                    break
                else:
                    raise ValueError(self.invalid_input())
            except ValueError as e:
                print(e)

    def roll_dice(self):
        """Simulate rolling a six-sided dice."""
        if self.cheat:
            return 6
        else:
            return random.randint(1, 6)

    def single_game(self, mode):
        """Start a single-player game."""
        print("\n------------Game Started-------------")
        self.player1.new_game()
        self.computer.new_game()
        clear_command = 'cls' if os.name == 'nt' else 'clear'
        while True:
            os.system(clear_command)
            try:
                num = self.roll_dice()
                if (self.player1.get_score() <= 100 and
                        self.player2.get_score() <= 100):

                    current_player = self.player_list[self.index]
                    print(self.display_dice_current_player
                          (current_player, num))
                    if num != 1:
                        if isinstance(current_player, Computer):
                            choice = mode(self.current_score)
                            self.computer_game_logic(
                                choice, current_player, num
                                )
                            time.sleep(1.5)

                        else:
                            self.while_num_not_1(current_player, num)
                            time.sleep(1.5)
                    else:
                        self.when_num_is_one(current_player)
                        time.sleep(1.5)
                else:
                    print(self.end_game(self.player1, self.computer))
                    break
            except ExitGameException:
                break

    def computer_game_logic(self, choice, current_player, num):
        """Handle the game logic for the computer player's turn.

        Parameters:
        - choice (str): The computer player's decision to roll ('r') or
            hold ('h').
        - current_player (Player): The current player (either the computer or
            the human player).
        - num (int): The number rolled on the dice.

        Returns:
        None
        """
        if choice == 'r':
            print(self.player_rolled(current_player, num))
        elif choice == 'h':
            print(self.player_hold(current_player, num))
            self.set_current_score_zero()
            # change player index
            self.player_change()

    def invalid_input(self):
        """Return a message for all the invalid options."""
        return "\nInvalid input! Enter a number from the listed options.\n"

    def multiplay(self):
        """Handle computer player's game logic."""
        print("\n------------Game Started-------------")
        self.player1.new_game()
        self.player2.new_game()
        clear_command = 'cls' if os.name == 'nt' else 'clear'
        while True:
            os.system(clear_command)
            try:
                num = self.roll_dice()
                if (self.player1.get_score() <= 100 and
                        self.player2.get_score() <= 100):
                    self.multiplay_game_logic(num)
                    time.sleep(1)
                else:
                    # display the winner
                    print(self.end_game(self.player1, self.player2))
                    break
            except ExitGameException:
                break

    def multiplay_game_logic(self, num):
        """
        Handle the game logic for each turn in a multiplayer game.

        Parameters:
        - num (int): The number rolled on the dice.

        Returns:
        None
        """
        current_player = self.player_list[self.index]
        print(self.display_dice_current_player(current_player, num))
        if num != 1:
            self.while_num_not_1(current_player, num)
        else:
            self.when_num_is_one(current_player)

    def when_num_is_one(self, current_player):
        """
        Handle the situation when a player rolls a one.

        Parameters:
        - current_player (Player): The current player.

        Returns:
        None
        """
        # display rolled one
        print(self.rolled_one(current_player))
        # change player index
        self.player_change()
        # restart to zero the  current score
        self.set_current_score_zero()
        time.sleep(1.5)

    def player_holds(self, current_player, num):
        """
        Handle the situation when a player chooses to hold.

        Parameters:
        - current_player (Player): The current player.
        - num (int): The number rolled on the dice.

        Returns:
        None
        """
        print(self.player_hold(current_player, num))
        # restart to zero the  current score
        self.set_current_score_zero()
        # change player index
        self.player_change()

    def while_num_not_1(self, current_player, num):
        """
        Handle the situation when the rolled number is not one.

        Parameters:
        - current_player (Player): The current player.
        - num (int): The number rolled on the dice.

        Returns:
        None
        """
        while True:
            try:
                # thake choice from the user
                choice = self.take_choice()
                if choice == "exit":
                    raise ExitGameException()
                if choice == 'r':
                    print(self.player_rolled(current_player, num))
                    break
                elif choice == 'h':
                    self.player_holds(current_player, num)
                    break
                else:
                    raise ValueError(self.invalid_input())
            except ValueError as e:
                print(e)

    # display  winner whan the game ends
    def end_game(self, player1, player2):
        """Handle the end of the game and determine the winner.

        Parameters:
        - player1 (Player): The first player.
        - player2 (Player): The second player.

        Returns:
        str: A message indicating the winner and their stats.
        """
        if player1.get_score() > player2.get_score():
            player1.set_game_won()
            self.winner = player1.get_name()
        else:
            player2.set_game_won()
            self.winner = player2.get_name()
        self.game_played += 1
        return f"""Game over, Winner: {self.winner}
{player1.get_name()} Stats: vs  {player2.get_name()} Stats:
-------------------------------
Score: {player1.get_score():<15}Score: {player2.get_score()}
Rolls: {player1.get_num_rolls():<15}Rolls: {player2.get_num_rolls()}
Holds: {player1.get_num_holds():<15}Holds: {player2.get_num_holds()}
"""

    # thigs to do when the player rolls one
    def rolled_one(self, current_player):
        """
        Handle the situation when a player rolls a one.

        Parameters:
        - current_player (Player): The current player.

        Returns:
        str: A message indicating that the player rolled one and their turn is
        skipped.
        """
        return f"\n\n'{current_player.get_name()}' rolled 1, Skipping turn\n\n"

    # change player index
    def player_change(self):
        """Change the index to switch between players."""
        self.index = 1 - self.index

    def set_current_score_zero(self):
        """Reset the current score to zero."""
        self.current_score = 0

    # take the user choice to roll or hold
    def take_choice(self):
        """Take the user's choice to roll or hold."""
        """Returns:
        str: The user's choice."""
        choice = input("Hold or roll ('h', 'r','exit'): ")
        return choice

    def player_hold(self, current_player, num):
        """Handle the player holding the dice.

        Parameters:
        - current_player (Player): The current player.
        - num (int): The number rolled on the dice.

        Returns:
        str: A message indicating that the player holds and their overall
        score.
        """
        current_player.set_num_holds()
        self.current_score += num
        current_player.set_score(self.current_score)
        return f"'{current_player.get_name()}' holds"

    def player_rolled(self, current_player, num):
        """Handle the player rolling the dice."""
        """Parameters:
        - current_player (Player): The current player.
        - num (int): The number rolled on the dice.

        Returns:
        str: A message indicating that the player rolled.
        """
        current_player.set_num_rolls()
        self.current_score += num
        return f"""{current_player.get_name()} rolled\n"""

    def display_dice_current_player(self, current_player, num):
        """Display the current player's turn and dice roll."""
        """Parameters:
        - current_player (Player): The current player.
        - num (int): The number rolled on the dice.

        Returns:
        str: A message displaying the current player's turn and dice roll.
        """
        over_all = "Overall score:"
        roll = "Roll:"
        return (f"Player:'{current_player.get_name():>5}' is playing\n"
                f"{self.player_list[0].get_name()}: "
                f"{over_all:<5} {self.player_list[0].get_score()}\n"
                f"{self.player_list[1].get_name()}: "
                f"{over_all:<5} {self.player_list[1].get_score()}\n"
                f"Current score: {self.current_score}\n"
                f"Dice Roll:\n{Dice().display_dice(num):>5}\n {roll:>18}{num}")

    # no unittest
    def multiplay_change_name(self):
        """Handle changing player names in multiplayer mode."""
        while True:
            try:
                print(self.change_multiplay_name())
                option2 = self.take_choice_menu()
                if option2 == "1":
                    name = self.take_choice_name()
                    self.player1.set_name(name)
                elif option2 == "2":
                    name = self.take_choice_name()
                    self.player2.set_name(name)
                elif option2 == "3":
                    break
                else:
                    raise ValueError("invalid input.")
            except ValueError as e:
                print(f"{e}")

    def display(self):
        """Display the main menu options."""
        """Returns:
        str: The main menu options.
        """
        return """
1.multiplay
2.single play
3.exit
"""

    # no unittest
    def take_choice_menu(self):
        """Take user choice menu."""
        choice = input("Enter option: ")
        return choice

    def display_multiplay(self):
        """Display the multiplayer mode options."""
        """Returns:
        str: The multiplayer mode options.
        """
        return """
\n-------------------------multiplay---------------------------
\n1. start
2. change name
3. go back"""

    def take_choice_name(self):
        """Take the player's name as input."""
        """Returns:
        str: The player's name.
        """
        name = input("Enter name: ")
        return name

    def change_multiplay_name(self):
        """Display for the multiplay change name."""
        return """
\n------ change name--------
1.To change player 1 name.
2.To change player 2 name.
3.Go back\n
"""

    def single_game_menu(self):
        """Display for the single game menu."""
        return """
\n------------------------soloplay----------------------------
\nChoose game mode:
1. Easy mode
2. Medium mode
3. Hard mode
4. Change name
5. go back"""

    def singleplay_change_name(self):
        """Handle changing player names in single player mode."""
        print(self.change_single_name())
        name = self.take_choice_name()
        self.player_list[0].set_name(name)

    def change_single_name(self):
        """Display the menu for changing single player name."""
        """Returns:
        str: The menu for changing single player name.
        """
        return """
\n------ change name--------
Player 1:
"""

    def set_player_multi(self):
        """Set the players for multiplayer mode."""
        """Returns:
        the two players.
        """
        name1 = self.take_choice_name()
        player1 = Player(name1)
        name2 = self.take_choice_name()
        player2 = Player(name2)
        return player1, player2

    def set_player_single(self):
        """Set the player for single player mode."""
        """Returns:
        Player: The single player.
        """
        name1 = self.take_choice_name()
        player1 = Player(name1)
        return player1

    def single_game_intro(self, mode):
        """Introduce the single player game mode."""
        """Parameters:
        - mode (str): The mode of the game.

        Returns:
        str: An introduction to the single player game mode.
        """
        return f"""-----------------{mode} mode-----------------"""
