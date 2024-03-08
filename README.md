Welcome to the Pig Dice game!

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

        5. Cheat Mode:
        - Optionally, players can enable cheat mode where the dice always roll a six. This can be used for testing or
            fun purposes but should be disabled during regular gameplay.
        - Note: Type 'cheat' and press Enter to activate cheat mode and start the game.

        6. High Score:
        - Players have the option to see the high score.
        - Note: Type 'high_score' or 'score'.

        7. Difficulty Levels:
        - Players can choose from different difficulty levels when playing against the computer, such as Easy, Medium, 
        or Hard. Each difficulty level may alter the computer's strategy or behavior.

        8. Exit:
        - While playing, type 'exit' to terminate and restart the game.

        These are the basic rules of the Pig Dice game. Enjoy playing!


License:

This project is licensed under the MIT License. See the LICENSE file for more information.


✍️ Authors
 -Sham
 -Ghazal
 -Bereket
