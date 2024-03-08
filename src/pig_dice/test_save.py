"""Unitt test for save class."""

import unittest
import json
from save import Save
from player import Player
import os


class TestSave(unittest.TestCase):
    """Test cases for the Save class."""

    def setUp(self):
        """Set up test environment."""
        self.test_filename = "test_game_history.json"

    def tearDown(self):
        """Tear down test environment.""" 
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save(self):
        """Test case for saving game data."""  
        player1 = Player("Player 1")
        player1.set_game_won()
        player2 = Player("Player 2")
        played_game = 1

        # Instantiate Save class
        saver = Save()

        # Call save method
        saver.save(player1, player2, played_game, self.test_filename)
        
        # Assert that the file is created and contains the correct data
        self.assertTrue(os.path.exists(self.test_filename))

        with open(self.test_filename, "r") as file:
            saved_data = json.load(file)
            expected_data = [{
                "game": {
                    "player 1": {
                        "name": player1.get_name(),
                        "won": player1.get_game_won()
                    },
                    "player 2": {
                        "name": player2.get_name(),
                        "won": player2.get_game_won()
                    },
                    "played game": played_game
                }
            }]
            self.assertEqual(expected_data, saved_data)
        
        with self.assertRaises(IOError):
            saver.save(player1, player2, played_game, "/invalid/path/invalid_filename.json")


    
    

        


