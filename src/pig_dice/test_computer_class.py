"""Unit testing."""
from computer import Computer
from game import Game
from player import Player
import unittest
class Test_computer_player_medium(unittest.TestCase):
    """Unit tests for the Computer class in medium difficulty mode."""
    def test_instance(self):
        """Test if an instance of Computer class is created."""
        computer=Computer()
        self.assertIsInstance(computer,Computer)

    def test_function_return(self):
        """Test the return values of easy, medium, and hard mode functions."""
        computer_player=Computer()
        easy_return=computer_player.easy_mode(10)
        medium_return=computer_player.medium_mode(30)
        hard_return=computer_player.hard_mode(40)
        option=['r', 'h']
        exp1=easy_return  in option
        exp2=medium_return  in option
        exp3=hard_return  in option
        self.assertTrue(exp1)
        self.assertTrue(exp2)
        self.assertTrue(exp3)
    def test_easy(self):
        """Test the behavior of easy mode."""
        computer_player=Computer()
        computer_player_return=computer_player.easy_mode(10)
        exp="r"
        evaluate=computer_player_return is exp
        self.assertTrue(evaluate)
        computer_player2=Computer()
        computer_player_return_2=computer_player2.easy_mode(22)
        exp1="h"
        evaluate=computer_player_return_2 is exp1
        self.assertTrue(evaluate)
    def test_medium_mode(self): 
        """Test the behavior of medium mode."""
        computer_player=Computer()
        computer_player_return=computer_player.medium_mode(26)
        exp="h"
        evaluate=computer_player_return is exp
        self.assertTrue(evaluate)
        computer_player_return_2=computer_player.medium_mode(10)
        exp="r"
        evaluate=computer_player_return_2 is exp
        self.assertTrue(evaluate)

        #test logice when computer score is  >0
        computer_player2=Computer()
        computer_player2.set_score(20)
        computer_player_return_3=computer_player2.medium_mode(10)
        exp="r"
        evaluate=computer_player_return_3 is exp
        self.assertTrue(evaluate)

        computer_player_return_4=computer_player2.medium_mode(19)
        exp="h"
        evaluate=computer_player_return_4 is exp
        self.assertTrue(evaluate)

    def test_hard_mode(self):
        """Test the behavior of hard mode."""
        computer_player=Computer()
        computer_player_return=computer_player.hard_mode(10)
        exp="r"
        evaluate=computer_player_return is exp
        self.assertTrue(evaluate)
        computer_player_return_2=computer_player.hard_mode(25)
        exp="h"
        evaluate=computer_player_return_2 is exp
        self.assertTrue(evaluate)

        #test logic when computer score is greater than 71
        computer_player2=Computer()
        computer_player2.set_score(80)
        computer_player_return_3=computer_player2.hard_mode(10)
        exp="r"
        evaluate=computer_player_return_3 is exp
        self.assertTrue(evaluate)

        computer_player_return_4=computer_player2.hard_mode(19)
        exp="h"
        evaluate=computer_player_return_4 is exp
        self.assertTrue(evaluate)

        
       



        




