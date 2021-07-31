import time
import random

# Global Variables
item = ["dagger"]
revisitedField = False


def display(txt):
    print(txt)
    time.sleep(2)


def house():
    monsters = ['pirate', 'dragon']
    chosenMonster = random.choice(monsters)
    display("You approach the door of the house.")
    display(
        "You are about to knock when the door opens and out steps a "
        + chosenMonster + "."
    )
    display("Eep! This is the pirate's house!")
    display("The pirate attacks you!")
    if 'dagger' in item:
        # print this line if the player has a dagger only.
        display(
            "You feel a bit under-prepared for this,"
            "what with only having a tiny dagger."
        )
    # check if the user input is valid
    while True:
        responseFightOrRun = input(
            "Would you like to (1) fight or (2) run away?"
        )
        if responseFightOrRun == '1' or responseFightOrRun == '2':
            return responseFightOrRun


def cave(item):
    display("You peer cautiously into the cave.")
    if 'dagger' in item:
        display("It turns out to be only a very small cave.")
        display("Your eye catches a glint of metal behind a rock.")
        display("You have found the magical Sword of Ogoroth!")
        display(
            "You discard your silly old dagger and take the sword with you."
        )
        # player acquires a sword
        item[0] = 'sword'
    elif 'sword' in item:
        display("You've been here before, and gotten all the good stuff.")
        display("It's just an empty cave now.")
    display("You walk back out to the field.")


def field():
    display("Enter 1 to knock on the door of the house.")
    display("Enter 2 to peer into the cave.")
    display("What would you like to do?")
    # check if the user input is valid
    while True:
        userChoice = input("(Please enter 1 or 2).")
        if userChoice == '1' or userChoice == '2':
            return userChoice


def intro():
    display(
        "You find yourself standing in an open field,"
        " filled with grass and yellow wildflowers."
        )
    display(
        "Rumor has it that something wicked is somewhere around here,"
        " and has been terrifying the nearby village."
        )
    display("In front of you is a house.")
    display("To your right is a dark cave.")
    display(
        "In your hand you hold your trusty"
        " (but not very effective) dagger.\n"
    )


def fight(item):
    if "dagger" in item:
        # player will be defeated
        display("You do your best...")
        display("but your dagger is no match for the pirate.")
        display("You have been defeated!")
        display("GAME OVER\n")

    elif "sword" in item:
        # player will win
        display("As the pirate moves to attack, you unsheath your new sword.")
        display(
            "The Sword of Ogoroth shines brightly in "
            "your hand as you brace yourself for the attack."
        )
        display(
            "But the pirate takes one look at your shiny new toy"
            " and runs away!"
        )
        display("You have rid the town of the pirate. You are victorious!")
        display("GAME OVER\n")


def running():
    display(
        "You run back into the field. Luckily,"
        " you don't seem to have been followed."
    )


def playAgain():
    # check if the user input is valid
    while True:
        responsePlayAgain = input("Would you like to play again? (y/n)")
        if responsePlayAgain == 'y' or responsePlayAgain == 'n':
            return responsePlayAgain


def resetVariables(item):
    # global item
    item[0] = "dagger"


def play_game(item, revisitedField):
    while True:
        # Intro is run only if user never been to field before
        if revisitedField is False:
            intro()

        userChoice = field()

        if userChoice == '1':
            responseFightOrRun = house()
            if responseFightOrRun == '1':
                fight(item)
                responsePlayAgain = playAgain()
                # check if the input is valid
                if responsePlayAgain == 'y':
                    # restar the game
                    display('Exellent!')
                    # reset item that user has at the beginning
                    resetVariables(item)
                    revisitedField = False
                elif responsePlayAgain == 'n':
                    display('Thanks for playing! See you next time.')
                    break
            elif responseFightOrRun == '2':
                running()
                # This is to decide if we have been to field before
                revisitedField = True
        elif userChoice == '2':
            cave(item)
            # This is to decide if we have been to field before
            revisitedField = True


if __name__ == "__main__":
    play_game(item, revisitedField)
