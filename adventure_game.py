import time
import random

item = ["Dagger"]
devils = ["Pangolin", "Lizard", "Capybara", "Fossa",
          "Sloth", "Pink Fairy Armadillo", "Maned wolf"]
devil_type = []


def enemy(devil_type):
    if len(devil_type) == 0:
        devil_type.append(random.choice(devils))
    return devil_type[0]


def print_pause(text):
    print(text)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, what???")
    return response


def intro():
    print_pause(
        "\n\nYou find yourself standing in an open field, "
        "filled with grass and yellow wildflowers.\n")
    print_pause(
        f"Rumor has it that a {enemy(devil_type)} is somewhere around here, "
        "and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause(
        "In your hand you hold your trusty (but not very effective) dagger.\n")


def field():
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do?\n")
    response = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if "1" in response:
        house()
    if "2" in response:
        cave()


def fight():
    if "Sword" in item:
        print_pause(
            f"As the {enemy(devil_type)} moves to attack,"
            "you unsheath your new sword.\n")
        print_pause(
            "The Sword of Ogoroth shines brightly in your hand "
            "as you brace yourself for the attack.\n")
        print_pause(
            f"You have rid the town of the {enemy(devil_type)}."
            " You are victorious!\n")
        play_again()
    else:
        print_pause("You do your best...\n")
        print_pause(
            (f"but your dagger is no match for the {enemy(devil_type)}.\n"))
        print_pause("You have been defeated!\n")
        play_again()


def house():
    print_pause("You approach the door of the house.\n")
    print_pause(
        f"You are about to knock when the door opens"
        f" and out steps a {enemy(devil_type)}.\n")
    print_pause(f"Eep! This is the {enemy(devil_type)}'s house!\n")
    print_pause(f"The {enemy(devil_type)} attacks you!\n")
    if "Sword" not in item:
        print_pause(
            "You feel a bit under-prepared for this,"
            " what with only having a tiny dagger.\n")
    print_pause("Would you like to (1) fight or (2) run away?\n")
    response = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if "1" in response:
        fight()
    elif "2" in response:
        print_pause(
            "You run back into the field. Luckily,"
            " you don't seem to have been followed.\n")
        field()


def cave():
    print_pause("You peer cautiously into the cave.\n")
    if "Sword" not in item:
        print_pause("It turns out to be only a very small cave.\n")
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found the magical Sword of Ogoroth!\n")
        print_pause(
            "You discard your silly old dagger and take the sword with you.\n")
        item.append("Sword")
    elif "Sword" in item:
        print_pause(
            "You've been here before, and gotten all the good stuff."
            " It's just an empty cave now.\n")
    print_pause("You walk back out to the field.\n")
    field()


def play_again():
    print_pause("Would you like to play again?\n")
    response = valid_input("(y/n)\n", "y", "n")
    if "y" in response:
        print_pause("Excellent! Restarting the game ...\n")
        devil_type.remove(devil_type[0])
        item.remove("Sword")
        item.append("Dagger")
        play_game()
    elif "n" in response:
        print_pause("Thanks for playing! See you next time.\n")


def play_game():
    intro()
    field()


play_game()
