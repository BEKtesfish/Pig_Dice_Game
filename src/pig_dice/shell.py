#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
from game import *
import high_score
import display

class PigDiceCLI(cmd.Cmd):
    intro = "Welcome to the Pig Dice game! Type help or ? to list commands.\n"
    prompt = "(Pig Dice) "

    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.game = None

    def do_start(self, _):
        """Start"""
        game=Game()
        game.play()

    def do_rules(self, _):
        """Display the game rules."""
        print(display.rules())
    def do_exit(self, _):
        """Exit the game."""
        print("Exiting Pig Dice. Goodbye!")
        return True
    def do_high_score(self, _):
        """Display the high score list."""
        high_score.load()
    def do_score(self, _):
        """Alias for 'high_score' command."""
        return self.do_high_score(_)
    def do_quit(self, _):
        """Exit the game."""
        return self.do_exit(_)
    
    def do_cheat(self, _):
        """welcome cheater, Sometimes, a little bit of mischief adds spice to life.
        Welcome to the world of Pig Dice Cheat Mode, 
        where the dice are always on your side!"""
        game=Game(cheat=True)
        game.play()
    def do_q(self, _):
        """Alias for 'exit' command."""
        return self.do_exit(_)

 

    # Implement other command methods as needed

if __name__ == "__main__":
    cli = PigDiceCLI()
    cli.cmdloop()
