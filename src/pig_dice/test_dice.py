"""Unit testing."""

import unittest
from dice import Dice


class Test_dice(unittest.TestCase):
    """Unit tests for the Dice class."""

    def test_instance(self):
        """Test if an instance of Dice class is created."""
        dice = Dice()
        self.assertIsInstance(dice, Dice)

    def test_dices(self):
        """Test the display_dice method for each face of the dice."""
        dice = Dice()

        for i in range(1, 7):
            art_dice = dice.display_dice(i)
            test_dice = dice.display_dice(i)
            self.assertEqual(art_dice, test_dice)
            self.assertEqual(art_dice, test_dice)
