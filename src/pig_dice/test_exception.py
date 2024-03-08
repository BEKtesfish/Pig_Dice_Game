

import unittest
from exception import ExitGameException

class Test_exception(unittest.TestCase):
    """Unit tests for the ExitGameException class."""
    def test_instaance(self):
        """Test if an instance of ExitGameException can be created."""
        exception=Exception()
        self.assertIsInstance(exception,Exception)
    def test_exit_game_exception(self):
        """Test if ExitGameException raises the correct message."""
        try:
            
            raise ExitGameException("Exit game")
        except ExitGameException as e:
            
            self.assertEqual(str(e), "Exit game")

