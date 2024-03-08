"""
Dice Class

This class represents a dice in the game. It provides a method to display the visual representation of a dice roll.

Methods:
- display_dice(num): Returns the visual representation of the given dice roll.

"""
class Dice:
    """
    Dice Class

    Represents a dice in the game.
    """

   
    def display_dice(self, num):
        """
        Display Dice Roll.

        Returns the visual representation of the given dice roll.

        Parameters:
        - num (int): The number rolled on the dice.
        """
        if num == 1:
            return """
            ┌─────────┐
            │         │
            │    ●    │
            │         │
            └─────────┘
            """
        elif num == 2:
            return """
            ┌─────────┐
            │ ●       │
            │         │
            │       ● │
            └─────────┘
            """
        elif num == 3:
            return """
            ┌─────────┐
            │ ●       │
            │    ●    │
            │       ● │
            └─────────┘
            """
        elif num == 4:
            return """
            ┌─────────┐
            │ ●     ● │
            │         │
            │ ●     ● │
            └─────────┘
            """
        elif num == 5:
            return """
            ┌─────────┐
            │ ●     ● │
            │    ●    │
            │ ●     ● │
            └─────────┘
            """
        elif num == 6:
            return """
            ┌─────────┐
            │ ●     ● │
            │ ●     ● │
            │ ●     ● │
            └─────────┘
            """