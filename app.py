#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

#Game rules:

#Rock beats scissors (breaking it).
#Scissors beat paper (cutting it).
#Paper beat rock (wrapping it).
#The minigame is multiplayer and the computer plays the role of your opponent and chooses a random element from the list of elements
#Interaction with the player:

#The console is used to interact with the player.
#The player can choose one of the three options: rock, paper, or scissors.
#The player can choose whether to play again.
#The player should be warned if they enter an invalid option.
#The player is shown their score at the end of the game.

#Validation of user input:
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
#By the end of each round, the player must answer whether they want to play again or not.

import random
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return app.send_static_file("index.html")
#   return "Hello World!"
print("Hello World!")

# create a list of play options
t = ["Rock", "Paper", "Scissors"]
# define a function that randomly returns one of the 3 options
random.choice(t)


# assign a random play to the computer
computer = "Rock"  #t[randint(0,2)]

# set player to False
player = False

while player == False:
# set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    # player was set to True, but we want it to be False so the loop continues
    player = False
    # make computer a random choice again
    computer = random.choice(t)

    







