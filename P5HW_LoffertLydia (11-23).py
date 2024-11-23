# Lydia Loffert
# 11/18/2024
# P5HW
# Use functions to create a game


# Import time library
import time


# Create empty character list to hold attributes
character = {}

# Create empty emergency exit list to hold attributes
exit_door = {}


def main_menu():
    # Allow player to boot up game
    boot_inp = input("Start the game? (Yes/No)\n")
    if boot_inp.lower().strip() == "yes":
        pass
    else:
        print("Thanks for playing!")
        exit()

def create_character():
    """
    Create game character by collecting user input.
    
    Returns:
    dict: A dictionary representing the game character with user-provided attributes.
    """
    name = input("What is your name? \n")
    # Make global change to list (everywhere I looked said this isn't reccommended but
    #I've hit a dead end trying to make this work and I don't really understand the perimeters/arguments at alllll 😟)
    global character
    character = {
        "name": name,
        "strength": 20,
        "status": "headache"
    }
    
    return character

# Create exit door containing it's values
def make_emerg_exit():

    name = "panel",
    resistance = 40
    global exit_door # Sorry....
    exit_door = {
        "name": name,
        "resistance": resistance,
    }
    
    return exit_door

def display_character(character):
    print("------------")
    print()
    for key, value in character.items():
        # Show inventory to player
        if key == "name":
            print(f"Name: {value}")
        elif key == "status":
            print(f"You have:\n\
Nothing but a {value}\n")
    time.sleep(1)
    return character


def bed(): # Player investigates bed

    # If player has already investigated
    if "item1" in character: 
        print("You don't find anything else under the bed, and it hasn't gotten\n\
more comfortable since you last saw it.\n")
        
    else:
        print("You decide to check out the uncomfortable bed. You sit on it and it\n\
feels like it looks. Looking underneath it however, reveals a small key.\n\n\
You tuck it away into your pocket.\n")
        # Key is added to inventory
        character["item1"] = "key"
    #return to decision branch
    decision()
    

def elevator():
    
    print("You approach the elevator, it's rather ornate, and stands out oddly\n\
in the dingy room. Pressing the button does nothing, but there's a small \n\
keyhole below it.\n")

    # If player has key from bed
    if "item1" in character:
        time.sleep(2)
        print("That key you found under the bed seems like it might fit, you \n\
try it in the lock and hear a click.\n\n\
The elevator is now open.\n")
        # Trigger elevator door open (I can't make it work so it's just added as an inventory item...
        character["el_flag"] = "ON"
    
    #return to decision branch
    decision()
        

def cupboard():
    
    # If player has already investigated cupboard
    if "item2" in character:
        print("There's not much else to see in the cupboard now, unless you're\n\
really into cobwebs.\n")
        
    else:
        print("You try the cupboard. It's contents are mostly bare except for a lone crowbar\n\
wedged into a shelf too small for it. But it comes out rather easily when you pull on it.\n")
        time.sleep(1.5)
        print("You tuck the crowbar into your pocket (somehow)\n")
    
    # Crowbar is added to inventory
        character["item2"] = "crowbar"
        
    #return to decision branch
    decision()

def in_elevator():
    
    print("Inside the elevator is a panel with only two buttons: Up and Down, above them is\n\
a headshot of former North Carolina Commissioner of Labor Cherie Berry.\n")
    
    button_press = input("Well, wanna go up or down?\n")

    # Player goes up
    time.sleep(.5)
    if button_press.lower() == "up":
        print("\n---------\n")
        print("The doors close and the chamber hums as you feel yourself being lifted up\n\
along with it. It eventually rumbles un-gently to a stop.\n\
But the doors don't open.\n")
        time.sleep(1)
        
        print("Though only now when you look around do you notice the emergency exit above you.\n\
It looks a little loose, there's light filtering through it.\n")
        # If player has crowbar
        if "item2" in character:
            escape()
        else:
            time.sleep(1)
            print("Unsure of what to do, you head back down.\n")
            #return to decision branch
            decision()
            
    # Player goes down
    time.sleep(1)
    if button_press.lower() == "down":
        print("\nNothing happens, You suppose you must be on the ground floor.\n")
        in_elevator()
    else:
        print("I don't think you can go that way...")
        in_elevator()
   
# Player decides what to do
def decision():
    time.sleep(1)
    choice = input("What would you like to investigate? (Elevator/Cupboard/Bed)\n")
    time.sleep(.5)

    if choice.lower() == "elevator":
        print("\n---------\n")
        # If elevator is unlocked player goes directly in it instead
        if "el_flag" in character:
            in_elevator()
        else:
            elevator()
        
    if choice.lower() == "cupboard":
        print("\n---------\n")
        cupboard()
        
    if choice.lower() == "bed":
        print("\n---------\n")
        bed()
     
    else:
        print("That's not in this room\n")
        decision()

def escape():
    time.sleep(2)
    use_bar = input("Use the crowbar?\n") # Have player initiate opening the hatch
    while True:
        if use_bar.lower() == "yes":
            break
        else:
            print("You don't want to escape?!\n") # Keep asking player until they do it
            use_bar = input("Use the crowbar?\n")
        
        
        
    time.sleep(1)
    print("\nYou pull out the crowbar you found in the cupboard and wedge it between the opening.\n")
    # Emergency exit resistance amount is weakened by protag's strength amount
    time.sleep(1)
    
    exit_door['resistance'] -= character['strength']
    print("The panel pulls farther from it's opening, you just need to give it one more go.\n\n")
    time.sleep(1)
    
    pull_answer = input("Pull again?\n")
    while True:
        if pull_answer.lower() == "yes":
            break
        else:
            print("You don't want to escape?!\n") # Keep asking player until they pull again
            pull_answer = input("Pull again?\n")
        
        
    print("\n---------\n")    
    # Emergency exit resistance amount is depleted by protag's strength amount
    exit_door['resistance'] -= character['strength']
    if exit_door['resistance'] == 0:

        time.sleep(3)
        print("The panel breaks loose and sunlight drops in behind it and fills the shaft. You poke your\n\
head out from the opening and see that you're looking head on into a thankfully not-too-busy street.\n")
        time.sleep(1)
        print("Pulling yourself out from what you now see is a sewer grate, you bewilderingly make your\n\
way back home, wherever that is from here.\n\n\n")
        time.sleep(2)
        print(f"Congratulations! {character['name']} has escaped!\n\n\n")
        time.sleep(1)

    print("Thanks for playing!")
    time.sleep(3)
    exit()



# Define the main
def main():

    main_menu()
    print("\n")
    print("Game is starting....")
    
    time.sleep(1)
    
    print("\n\n")

    # Name the player character
    protag = create_character()

    #Create emergency exit dictionary
    make_emerg_exit()
    
    # Game opening
    print(f"\n{protag['name']} wakes up on the floor of a cramped and dirty room. They don't\n\
remember how they got there or anything from the last few hours.\n")

    time.sleep(1)

    # Display the created characters
    display_character(protag)

    print(f"Taking in their surroundings {protag['name']} can see that the room resembles a cell,\n\
but with no exits except for a large elevator door on the north wall.\n\n")
    time.sleep(1)   
    print("To the left is a cupboard, and to the right an uncomfortable-looking bed.\n")

    # Take action
    decision()



# Call the main
if __name__ == "__main__":
    main()



