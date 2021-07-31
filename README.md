# Advanture Project
This project is to implement a simple version of an old-fashioned text-based adventure game with Python.


## Installation
Code editor to work with Python. 
I have been using Visual Studio Code for this project. 

## Directory structure
Game.py
README.md

## How to check out the Python program(i.e. Game.py)
Please keep the structure of the directories and 
open a terminal and type
"python Game.py" in the directory where the Game.py is located. 

## Details on variables and functions
# Global Variables
item : To keep track of item(s) a user has.
revisitedField : To determine if a user has visited the field before.

#functions
display(txt): To display text message in terminal with delay

house(): To proceed senario in case a user chooses to come into the house

cave(item): To proceed senario in case a user chooses to peer into the cave

field(): To proceed senario in case a user chooses to head to the field

intro(): To display intro of this game

fight(item): To proceed senario in case a user decide to fight with the enemy

def running(): To proceed senario in case a user chooses to run away from the enemy

def playAgain(): To determine if a user wants to play the game again

def resetVariables(item): To proceed senario in case a user choose to play game again then it resets a global value, item. 

def play_game(item, revisitedField): To proceed senario in case a user chooses to play the game. 

## Future work
-Add more randomness into game so that user can experience various senarios.

## Licence
Udacity