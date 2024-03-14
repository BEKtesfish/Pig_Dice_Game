🎲Pig Dice Game🎲
Welcome to the Pig Dice game!

> [!NOTE]  for Windows Users:

If you encounter the error "'charmap' codec can't encode characters in position 72-82: character maps to <undefined>" while playing the game in the terminal, we recommend trying to play it in VS Code. We've extensively tested the game on various Windows computers, and only one computer faced this problem. However, there's a small chance you could encounter a similar issue. Playing the game in VS Code should resolve any encoding-related issues you may encounter.

## Introduction

Pig Dice is a simple dice game where players compete to be the first to reach a target score. Players take turns rolling a six-sided die, accumulating points with each roll. However, if a player rolls a 1, they lose all points accumulated in that turn, and it becomes the next player's turn. The first player to reach the target score wins the game.


💡 Motivation

Playing games is not only about having fun but also about boosting our mood and improving our mental health. In this version of the Pig Dice Game, we've added a feature to provide inspiring quotes to keep you motivated and uplifted throughout the game.




# Installation

Follow these steps to set up and play the game:

- **Clone the Repository:**  
  Clone this repository to your local machine using the following command:


  (HTTPS) git clone https://github.com/BEKtesfish/Pig_Dice_Game.git
  (ssh)   git clone https://github.com/BEKtesfish/Pig_Dice_Game.git


- **Navigate to the Game Directory:**  
  Navigate to the directory of the cloned repository using the `cd` command:

    cd ./pig-dice-game


- **Set Up Virtual Environment (Optional but Recommended):**  
    -Create a virtual environment for the game to isolate its dependencies. You can use `venv`, `virtualenv`, or any other virtual environment tool you prefer.

    ```bash
    make venv

    -activate your venv

-install Dependencies:
   Install the required dependencies for the game using the provided requirements.txt file.

   - write 'make install' and all will be installed


-Check if Packages are Installed:
    Verify that the required packages are installed correctly by running the following command:
    
    - write 'make installed' and every thing installed will be listed


-Navigate to Source File:
    Navigate to the src directory of the game where the game file is located.
    
    type 'cd src'

--Navigate to game files:
    Navigate to the 'pig_dice' directory of the game where you can run the game file is located.


    # Additional Development Tools
        The project includes a Makefile that provides several targets for managing the development and testing process. Here's a breakdown of each target:

        -version: Displays the Python version being used. ('make version')
        -venv: Sets up a virtual environment and provides activation instructions. ('make venv')
        -install: Installs dependencies listed in requirements.txt. ('make install')
        -installed: Lists all installed Python packages. ('make installed')
        -clean: Removes generated and installed files. ('make clean')
        -clean-doc: Removes documentation files. ('make clean-doc')
        -clean-all: Removes the virtual environment and all generated files. ('make clean-all')
        -pylint: Checks for Python code errors and conventions. ('make pylint')
        -flake8: Enforces Python code style. ('make flake8')
        -lint: Combines linting using flake8 and pylint. ('make lint')
        -black: Formats Python code according to the black code style. ('make balck')
        -codestyle: Formats Python code using black. ('make codestyle')
        -unittest: Runs unit tests using unittest. ('make unittest')
        -coverage: Measures code coverage and generates reports. ('make coverage')
        -test: Combines linting, unit testing, and coverage measurement. ('make test')
        -pydoc: Generates Python documentation using pydoc. ('make pydoc')
        -pdoc: Generates HTML documentation using pdoc. ('make pdoc')
        -pyreverse: Generates class and package diagrams using pyreverse. ('make pyreverse')
        -doc: Generates project documentation using pdoc and pyreverse. ('make doc')
        -metrics: Calculates various software metrics. ('make metrics')
        -bandit: Checks for security issues using bandit. ('make brandit')
        
        # You can run these targets by invoking make followed by the target name in your terminal. For example, to install dependencies, you would run make install.


-Start the Game:
    Run the shell.py file to start the Pig Dice Game.

    bash
    Copy code
    python shell.py





## Features

- Single-player mode against AI opponents
- Multiplayer mode to challenge friends
- Adjustable difficulty levels
- Cheat mode for added fun
- High score tracking




# Rules of the agme.

        Pig Dice Game Rules:

        Objective:
        The objective of Pig Dice is to be the first player to reach or exceed a total score of 100 points.

        Equipment:
        - One six-sided dice
        - A scorecard or a way to keep track of points

        Gameplay:
        1. Starting the Game:
        - The game begins with two players, taking turns to roll the dice.
        - Players can choose to play in single-player mode against the computer or in multiplayer mode against another
            player.
        - Note: Type 'start' and follow the instruction.

        2. Taking Turns:
        - On a player's turn, they roll the dice.
        - If the player rolls:
            - roll 1: They lose all points accumulated during that turn, and it becomes the next player's turn.
            - Any other number: The number rolled is added to the player's turn total, and they can choose to hold or 
            roll again.

        3. Holding:
        - If a player chooses to hold, the turn total is added to their overall score, and it becomes the next player's
            turn.
        - Holding allows the player to secure their points for that turn and add them to their total score.

        4. Winning the Game:
        - The game continues until one player reaches or exceeds a total score of 100 points.
        - Once a player reaches the winning score, they are declared the winner, and the game ends.

        5.Cheat Mode

            In the Pig Dice game, there is a cheat mode available for those who want to have a bit more fun or test their luck! To activate cheat mode:

            1. When starting the game, instead of typing `start`, type `cheat` and press Enter.
            2. You will see a message confirming that cheat mode has been activated.
            3. Enjoy the game with the dice always on your side!

            **Example:**
                Welcome to the Pig Dice game! Type help or ? to list commands.
                (Pig Dice) cheat
                ---Welcome to Pig Dice Cheat Mode, where the dice are always on your side!---
                
            NOTE: Remember, cheat mode is just for fun and testing purposes. Have a blast!




        6. High Score:
        - Players have the option to see the high score.
        - Note: Type 'high_score' or 'score'.

        7. Difficulty Levels:
        - Players can choose from different difficulty levels when playing against the computer, such as Easy, Medium, 
        or Hard. Each difficulty level may alter the computer's strategy or behavior.

        8. computer intelligence.
            -  we came up to the computer player game stratagy from Wikipedia optimal play stratagy
            
            easy mode:
                    - the computer holds when its current score reachs 20. This strategy has an 8% disadvantage against optimal play.

            medium mode:
                    - the computer  holds  if current score reaches 25 and the overall score is 0 and 
                       if the overall score is not 0 it holds when the current score reaches 18
                    - the computer rolls if current score did not reach 25 and the over all score is 0 and 
                       if the over all score is not 0 it will roll until the current score reaches 18.
                    -This has a 3.3% disadvantage against optimal play.
                    

                    -
            hard mode:
                    - the computer holds the  computers overall score is < 71 and current score
                      is >= 21 or else if computer overall score >=71 and current score
                      is >= 18.
                    - the computer rolls if the computer overall score  is  < 71 and current score is <21 
                      or else if computer score is >= 71 and  current score is < 18.
                    - this stratagy is that when the computer overall score is lower to take a risk and roll 
                      until the current score reaches 21 and when the overall score is higher to lower the risk and hold when current score reaches 18

        8. Exit:
        - While playing, type 'exit' to terminate and restart the game.

        These are the basic rules of the Pig Dice game. Enjoy playing!


License:

This project is licensed under the MIT License. See the LICENSE file for more information.


✍️ Authors
 -Sham
 -Ghazal
 -Bereket
