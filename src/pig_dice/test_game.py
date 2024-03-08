"""Unit test."""
import unittest
from game import Game
from player import Player
from dice import Dice
from unittest.mock import patch


class Test_game(unittest.TestCase):
    """Unittest for the game class."""

    def test_instance(self):
        """Test case for verifying the instantiation of the Game class."""
        game = Game()
        game2 = Game(cheat=True)
        self.assertIsInstance(game, Game)
        self.assertIsInstance(game2, Game)

    # roll dice function
    def test_roll_dice(self):
        """Test case for checking the behavior of the roll_dice method."""
        game = Game()
        roll = game.roll_dice()
        exp = 1 <= roll <= 6
        self.assertTrue(exp)
        game2 = Game(cheat=True)
        roll_cheat = game2.roll_dice()
        exp_cheat = 6
        self.assertEqual(exp_cheat, roll_cheat)

    # end game function
    def test_end_game(self):
        """Test case for ensuring the correct determination of."""
        """the game winner and end-game behavior."""
        game = Game()
        game = Game()
        player1 = Player("bereket")
        player2 = Player("abel")
        player1.set_score(60)
        player2.set_score(50)
        end = game.end_game(player1, player2)
        winner = player1.get_name()
        self.assertEqual(game.winner, winner)
        self.assertEqual(player1.game_won, 1)
        self.assertEqual(player2.game_won, 0)
        self.assertEqual(game.game_played, 1)
        text = f"""Game over, Winner: {winner}
{player1.get_name()} Stats: vs  {player2.get_name()} Stats:
-------------------------------
Score: {player1.get_score():<15}Score: {player2.get_score()}
Rolls: {player1.get_num_rolls():<15}Rolls: {player2.get_num_rolls()}
Holds: {player1.get_num_holds():<15}Holds: {player2.get_num_holds()}
"""
        self.assertEqual(end, text)
    # test when player 2 is the winner
        player2.set_score(100)
        end = game.end_game(player1, player2)
        winner = player2.get_name()
        self.assertEqual(game.winner, winner)
        self.assertEqual(player1.game_won, 1)
        self.assertEqual(player2.game_won, 1)
        self.assertEqual(game.game_played, 2)
        text = f"""Game over, Winner: {game.winner}
{player1.get_name()} Stats: vs  {player2.get_name()} Stats:
-------------------------------
Score: {player1.get_score():<15}Score: {player2.get_score()}
Rolls: {player1.get_num_rolls():<15}Rolls: {player2.get_num_rolls()}
Holds: {player1.get_num_holds():<15}Holds: {player2.get_num_holds()}
"""
        self.assertEqual(end, text)

    # the text when a player roll one
    def test_rolled_one(self):
        """Test case for validating the output when a player rolls a one."""
        game = Game()
        player1 = Player("bereket")
        rolled_1_text = game.rolled_one(player1)
        text = f"\n\n'{player1.get_name()}' rolled 1, Skipping turn.\n\n"
        self.assertEqual(rolled_1_text, text)

    # test player chanege
    def test_player_change(self):
        """Test case for verifying the player change functionality."""
        game = Game()
        self.assertEqual(game.index, 0)
        game.player_change()
        self.assertEqual(game.index, 1)

    def test_set_current_score_zero(self):
        """Test case for verifying the player change functionality."""
        game = Game()
        game.current_score = 50
        self.assertEqual(game.current_score, 50)
        game.set_current_score_zero()
        self.assertEqual(game.current_score, 0)

    def test_player_hold(self):
        """Test case for the player hold functionality."""
        game = Game()
        player1 = Player("bereket")
        num = 6
        # check it is zero when it starts
        self.assertEqual(player1.num_holds, 0)
        self.assertEqual(game.current_score, 0)
        self.assertEqual(player1.get_score(), 0)
        return_text = game.player_hold(player1, num)
        self.assertEqual(player1.num_holds, 1)
        self.assertEqual(game.current_score, num)
        self.assertEqual(player1.get_score(), game.current_score)
        text = (f"'{player1.get_name()}' holds, "
                f"Overall score: {player1.get_score()}\n")
        self.assertEqual(return_text, text)

    def test_player_rolled(self):
        """Test case for the player hold functionality."""
        game = Game()
        player1 = Player("bereket")
        num = 6

        # check it is zero when it starts
        self.assertEqual(player1.num_holds, 0)
        self.assertEqual(game.current_score, 0)
        self.assertEqual(player1.get_num_rolls(), 0)
        game.current_score = num
        self.assertEqual(game.current_score, num)

    def test_display_dice_current_player(self):
        """Unittest for displaying the current player's dice roll and score."""
        game = Game()
        player1 = Player("bereket")
        num = 6
        return_text = game.display_dice_current_player(player1, num)

        text = (f"Player: '{player1.get_name()}' is playing\n"
                f"Current score: {game.current_score}\n"
                f"Dice Roll:\n{Dice().display_dice(num)}  roll: {num}")
        self.assertEqual(return_text, text)

    def test_display(self):
        """Test case for the display method."""
        game = Game()
        return_text = game.display()
        text = """
\n
1.multiplay
2.single play
3.exit
"""
        self.assertEqual(return_text, text)

    def test_display_multiplay(self):
        """Test case for displaying multiplay options."""
        game = Game()
        return_text = game.display_multiplay()
        text = """
\n-------------------------multiplay---------------------------
\n1. start
2. change name
3. go back"""
        self.assertEqual(return_text, text)

    def test_change_multiplay_name(self):
        """Test case display for changing player names  in multiplay mode."""
        game = Game()
        return_text = game.change_multiplay_name()
        text = """
\n------ change name--------
1.To change player 1 name.
2.To change player 2 name.
3.Go back\n
"""
        self.assertEqual(return_text, text)

    def test_single_game_menu(self):
        """Test case for the single game menu display."""
        game = Game()
        return_text = game.single_game_menu()
        text = """
\n------------------------soloplay----------------------------
\nChoose game mode:
1. Easy mode
2. Medium mode
3. Hard mode
4. Change name
5. go back"""
        self.assertEqual(return_text, text)

    def test_single_game_intro(self):
        """Test case for the introduction to single game mode."""
        game = Game()
        mode = "easy"
        return_text = game.single_game_intro(mode)
        text = f"""
-----------------{mode} mode-----------------
"""
        self.assertEqual(return_text, text)

    def test_set_player_single(self):
        """Test case for setting a single player."""
        game = Game()
        name = "bereket"
        player = Player(name)
        game.take_choice_name = lambda: (name)
        name = game.set_player_single()
        self.assertEqual(name.get_name(), player.get_name())

    def test_set_multiplayer(self):
        """Test case for setting up multiplayer players."""
        game = Game()
        player1_name = "sham"
        player2_name = "chamto"
        player1 = Player(player1_name)
        player2 = Player(player2_name)
        game.take_choice_name = lambda: (player1, player2)
        return_player1, return_player2 = game.set_player_multi()
        self.assertIsInstance(return_player1, Player)
        self.assertIsInstance(return_player2, Player)

    def test_change_single_name(self):
        """Test case for changing the name in single player mode."""
        text = """
\n------ change name--------
Player 1:
"""
        game = Game()
        return_text = game.change_single_name()
        self.assertEqual(text, return_text)

    def test_take_choice_name(self):
        """Test case for taking player name input."""
        game = Game()
        name = "bereket"
        game.take_choice_name = lambda: (name)
        self.assertEqual(game.take_choice_name(), name)

    def test_take_choice(self):
        """Test case for taking user choice input."""
        game = Game()
        choice = "exit"
        game.take_choice = lambda: (choice)
        self.assertEqual(choice, game.take_choice())

    def test_take_choice_menu_valid_input(self):
        """Test case for valid input in the menu."""
        game = Game()
        with patch('builtins.input', side_effect=['1']):
            choice = game.take_choice_menu()
        self.assertEqual(choice, '1')
