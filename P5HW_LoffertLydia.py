# Lydia Loffert
# 11/18/2024
# P5HW
# Use functions to create a game with characters

'''
https://www.makeuseof.com/python-text-adventure-game-create/

ideas for what the game should be about?
closed room (3 rooms?) inventory puzzle

can there be limited graphics? without turtle?
if not, how can i use text to show the rooms?

how can the characters be used in this setting?

character doesnt have to be made by player they can choose between two (AS LONG AS THEY ARE DICTIONARIES)
maybe game doenst change much depending on charcater you choose but its starts differnt and you encounter the other character if you
dont choose them. they solve the same puzzles but maybe you have to get the other player's item off of them
'''
# helplab 9am to 1pm FRI
'''
USE COMMENTS

can there be a text parser? can i make a dictionary of usable vocab words
or should the possible actions be displayed to the user

look to other infocom text games for construction ideas

maybe no direct enemies but theres traps or a wall that tries to close in on you and will kill you if you take the right prompt/have the item ?

Player character doesn't have many stats, but their dictionary tells you they start off with one or two items

can i have room/character dialogue change after events happen?

Gives you the room name in brackets at the top of the screen at the start of every room scene

Maybe have dialogue branch options to talk to the other NPC

settings:?
    * empty swimming pool
    * other character's room that you can talk to/get something from
    * long hallway with an elevator at the end, the hallway seems almost to rotate as it stretches on, at the very end is an elevator.
    [go down hallway] You walk down the hallway, you don't feel like you're turning, but when you look back the door you came from has moved to the wall.
    * "You feel someone watching you" (never explained
    *

    NOT GOING TO WORK WRAP IT UP

    small bathroom
    what actions should happen:
    enemy encounter
    get item
    use item

maybe instead of an "attack" you "attack" the elevator with the crowbar until it opens
    
'''

# Import libraries
import random

def create_character():
    """
    Create a game character by collecting user input.
    
    Returns:
    dict: A dictionary representing the game character with user-provided attributes.
    """
    
    name = input("Enter character name: ").strip()
    health = int(input(f"Enter {name}'s health: "))
    atk_damage = int(input(f"Enter {name}'s attack damage: "))
    
    character = {
        "name": name,
        "health": health,
        "damage": atk_damage
    }
    
    return character


def display_character(character):
    print("---------")
    for key, value in character.items():
        print(f"{key}: {value}")
    print()


def battle(attacker, defender):
    """
    Simulate a battle where the attacker deals damage to the victim.
    
    Args:
        attacker (dict): Dictionary representing the attacking character
        defender (dict): Dictionary representing the defending character
    
    Returns:
        dict: Updated defender dictionary with reduced health
    """
    print(f"{attacker['name']} is attacking {defender['name']}!!!!")
    print(f"")
    defender['health'] -= attacker['damage']
    
    return defender

def crowbar():
    


def bathroom():

    room = {
        "item": crowbar,
        "elevator": elevator
    }

def get_item():

    

    



# Define the main
def main():
    print("Game is starting....")
    print("\n\n\n")
    
    # Create two characters
    print("Create first character: ")
    char1 = create_character()
    print("\nCreate second character: ")
    char2 = create_character()
    print()

    # Display the created characters
    display_character(char1)
    display_character(char2)

    # Simulate a battle
    char2 = battle(char1, char2)

    display_character(char2)


# Call the main
if __name__ == "__main__":
    main()



