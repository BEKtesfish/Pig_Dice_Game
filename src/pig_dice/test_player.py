"""Unittest for player."""
import unittest
from player import Player


class Test_player(unittest.TestCase):
    """Test class for player."""

    def test_instance(self):
        """Test case for creating an instance of Player."""
        player1 = Player("sham")
        player1 = Player("sham")
        self.assertIsInstance(player1, Player)

    def test_get_name(self):
        """Test case for getting the player's name."""
        player1 = Player("sham")
        player_name = player1.get_name()
        name = "sham"
        self.assertEqual(player_name, name)

    def test_set_name(self):
        """Test case for setting the player's name."""
        player1 = Player("sham")
        name = "bereket"
        player1.set_name(name)
        player_name = player1.get_name()
        self.assertEqual(name, player_name)

    def test_beginning_score_zero(self):
        """Test case for verifying that the player's score is zero at the beginning."""
        player1 = Player("sham")
        starting_score = 0
        player_starting_score = player1.get_score()
        self.assertEqual(starting_score, player_starting_score)

    def test_set_score(self):
        """Test case for setting the player's score."""
        player1 = Player("sham")
        set_score = 50
        player1.set_score(set_score)
        seted_score = player1.get_score()
        self.assertEqual(set_score, seted_score)

    def test_new_game(self):
        """Test case for resetting the player's stats for a new game."""
        player1 = Player("sham")
        score = 50
        player1.set_num_holds()
        player1.set_num_rolls()
        player1.set_score(score)
        self.assertEqual(player1.get_score(), score)
        self.assertEqual(player1.get_num_holds(), 1)
        self.assertEqual(player1.get_num_rolls(), 1)
        player1.new_game()
        self.assertEqual(player1.get_score(), 0)
        self.assertEqual(player1.get_num_holds(), 0)
        self.assertEqual(player1.get_num_rolls(), 0)

    def test_game_won(self):
        """Test case for getting the number of games won by the player."""
        player1 = Player("sham")
        player1.game_won = 1
        self.assertEqual(player1.get_game_won(), 1)


        
    
    


