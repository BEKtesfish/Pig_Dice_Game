"""Unittest."""
import unittest
import high_score


class Test_high_score(unittest.TestCase):
    """Unittest for high score class."""
    def test_load_file(self):
        """Test case for loading a non-existing file."""
        with self.assertRaises(FileNotFoundError):
            high_score.load_json_data("non_exsisting_fil.json")

    def test_calculate_high_score(self):
        """Test case for calculating high scores."""
        data = [{
        "game": {
            "player 1": {
                "name": "bereekt",
                "won": 1
            },
            "player 2": {
                "name": "computer",
                "won": 7
            },
            "played game": 1
                }
            }]
        # we expect from the calculate_high_score function a list with tuble of player name and there win number 
        data_sorted = [('computer', 7), ('bereekt', 1)]
        high_score_sort = high_score.calculate_high_scores(data)
        self.assertEqual(data_sorted, high_score_sort)

    def test_display(self):
        """Test case for displaying the high score to display"""
        text = """
       HIGH SCORE LIST
*------------------------------*"""
        return_text = high_score.display()
        self.assertEqual(text, return_text)
     
    def test_display_high_score(self):
        """Test case for displaying individual high scores."""
        rank = 1
        player = "bereket"
        wins = 2
        text = f"""    {rank}. {player:<12}: {wins} wins"""
        return_text = high_score.display_high_score(rank, player, wins)
        self.assertEqual(text, return_text)