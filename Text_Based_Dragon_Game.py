# Text Based Adventure Game
# Designed by Maurice Wesley
# August 13, 2021

# Create dictionary containing rooms with nested dictionary containing key value pairs
room = {
    'Great Hall': {'South': 'Master Bedroom', 'North': 'Dungeon', 'East': 'Kitchen', 'West': 'Library'},
    'Master Bedroom': {'North': 'Great Hall', 'West': 'Man Cave', 'East': 'Wine Room', 'item': 'Gold Armor'},
    'Wine Room': {'West': 'Master Bedroom', 'North': 'Kitchen', 'item': 'Helmet'},
    'Dining Room': {'South': 'Kitchen', 'North': 'Gallery', 'item': 'Mystical Beast'},
    'Kitchen': {'West': 'Great Hall', 'North': 'Dining Room', 'South': 'Wine Room', 'item': 'Protection Spell'},
    'Library': {'North': 'Balcony', 'South': 'Man Cave', 'East': 'Great Hall', 'item': 'Photon Blaster'},
    'Balcony': {'South': 'Library', 'East': 'Dungeon', 'item': 'Wing'},
    'Man Cave': {'North': 'Library', 'East': 'Master Bedroom', 'item': 'Ammo'},
    'Dungeon': {'East': 'Gallery', 'South': 'Great Hall', 'West': 'Balcony', 'item': 'Conjurer'},
    'Gallery': {'West': 'Dungeon', 'North': 'Terrace', 'South': 'Dining Room', 'item': 'Force Field'},
    'Terrace': {'South': 'Gallery', 'item': 'Stamina'},
}


# Create function to show instructions
def show_instructions():
    print("Mystical Beast Adventure Game")  # Output to user
    print("Collect 9 items to win the game, or be eaten by the Beast.")  # Output to user
    print("Move commands: go South, go North, go East, go West")  # Output to user
    print("Add to Inventory: get 'item name'")  # Output to user
    print("Type 'quit' to end the game at any time")  # Output to user
    print("Type 'help' for a hint")  # Output to user
    print("Type 'GPS' for possible directions")  # Output to user


# Create function to show the player's status
def player_status(current_room, inventory, inventory_char):
    print("\nYou are in the", current_room)  # Output to user
    print("Inventory:", inventory)  # Output to user
    print("-" * (15 + len(inventory_char)))  # Dynamic separator


# Create function to display how to get an item
def item_help():
    print('\nInputs are case sensitive')  # Output to user
    print('To grab item')  # Output to user
    print("Type: get 'item name'. Example: get Water")  # Output to user


# Create function to display directions to another room
def gps(current_room):
    room_dict = room[current_room]
    # Loop to iterate over the key value pairs of the current room
    for direction, area in room_dict.items():
        # Check for a specific key in the dictionary
        if direction in ('North', 'South', 'East', 'West'):
            print(f'go {direction} to the {area}')


# Create a function to display comments when player quits
def quit_game():
    print("\nThat's okay Adventurer!")  # Output to user
    print('Try again next time!')  # Output to user
    print('Have a good day!')  # Output to user
    return False


# Create a function to display comments when the player wins
def won_game():
    print('\nYou collected all nine items!')  # Output to user
    print("You defeated the 'Mystical Beast'!")  # Output to user
    print('Great work adventurer!!')  # Output to user
    return False


# Create a function to display comments when the player loses
def lost_game():
    print('\nNom! Nom! Nom! You were destroyed by the Mystical Beast!!')  # Output to user
    print('You must collect all nine items to be victorious.')  # Output to user
    print('Try again next time adventurer!')  # Output to user
    return False


# Create a function to start the game or not
def start():
    # Get user input
    answer = input("Would you like to start your adventure? (Yes or No or Quit)\n")
    # Loop to check for valid user input
    while True:
        # Condition to check user input to start the game
        if answer.lower().strip() == "yes":
            return True  # True to start the game
        # Condition to check user input to end the game
        elif answer.lower().strip() in ('n', "no", 'q', 'quit'):
            # Function call to end the game
            quit_game()
            return False  # False to end the game
        # Condition when user enters an invalid input
        else:
            print("I do not understand.\n")  # Output to user
        # Get user input
        answer = input("Would you like to play? (Yes or No or Quit)\n")


# Create function that contain the game play
def main():
    # Show the instructions to the player
    show_instructions()
    print()
    # Assign variable to the start function value
    play = start()
    # Check value to start the game
    if not play:
        # If value is false then end game
        return

    # Assign variable to a room in the dictionary
    current_room = 'Great Hall'
    # Create list to track items collected
    inventory = []
    # Assign variable to the length of the list
    inventory_char = ' ,  '.join(inventory)
    # Create loop for movement in between rooms
    while True:
        # Show player status function
        player_status(current_room, inventory, inventory_char)
        # Assign variable to key value pair of the room in the room dictionary
        room_dict = room[current_room]
        # Condition to check for 'item' key in variable
        if 'item' in room_dict:
            # Assign variable to the value of the key in current room
            item = room_dict['item']
            # Condition to check if the value is in the inventory
            if item not in inventory:
                print(f'You see {item}!')  # Output to user
                # Condition to check if the current room contains the BOSS
                if current_room == 'Dining Room':
                    # Condition to check the number of items in the inventory
                    if len(inventory) < 9:
                        # Function call when items in inventory less than 9
                        lost_game()
                        break  # End process
                    else:
                        # Function call when items in inventory greater than 9
                        won_game()
                        break  # End process
                # Get user input
                user_input = input('Enter your move:\n')
                # Create list from user input
                user_input_list = user_input.split()
                # Condition to check user input to quit
                if user_input.lower() == 'quit':
                    # Function call when user input is quit
                    quit_game()
                    break  # End process
                # Condition to check user input to get an item
                elif user_input == 'get ' + item:
                    # Add item to inventory
                    inventory.append(item)
                    # Change the length of the dynamic separator
                    inventory_char = ' ,  '.join(inventory)
                    # Output to user
                    print(item, 'collected!')  # Output to user
                    continue
                # Condition to check user input for help
                elif user_input == 'help':
                    # Function call when user asks for help
                    item_help()
                    continue
                # Condition to check user input for directions
                elif user_input.lower().strip() == 'gps':
                    # Function call to give the user directions
                    gps(current_room)
                    continue
                # Condition to check for valid user input to go to another room
                elif user_input_list[0].lower() == 'go' and len(user_input_list) == 2:
                    # Condition to check if element in user input is a valid direction
                    if user_input_list[1] in ('North', 'South', 'East', 'West'):
                        # Assign variable to key value pairs of the current room in the dictionary
                        room_dict = room[current_room]
                        # Condition to check an element in user input is a key in the current room
                        if user_input_list[1] in room_dict:
                            # Reassign current room to the value returned from the element in the list
                            current_room = room_dict[user_input_list[1]]  # get to the next room
                            print('Item not Collected.')  # Output to user
                            continue
                        # Condition if second element is not a valid direction
                        else:
                            print(f"Can't {user_input}")  # Output to user
                            print("Type 'GPS' for possible directions")  # Output to user
                            continue
                    # Condition to check if element is a valid entry
                    else:
                        print(f"Can't {user_input}")  # Output to user
                        continue
                # Condition when user enters an invalid input
                else:
                    print("Invalid move..")  # Output to user
                    continue

        # Assign variable to user input when current room does not have an item
        command = input('Enter your direction:\n')
        # Create list to user input
        command_list = command.split()
        # Condition to check user input
        if command.lower().strip() == 'quit':
            # Function call when user input is quit
            quit_game()
            break  # End process
        # Condition to check user input
        elif command.lower().strip() == 'help':
            print("Type 'GPS' for directions!")  # Output to user
            continue
        # Condition to check to the first element in the list created from user input
        elif command_list[0].lower() == 'go' and len(command_list) == 2:
            # Condition to check the second element in the list created form user input
            if command_list[1] in ('North', 'South', 'East', 'West'):
                # Assign variable to the key value pairs of the current room
                room_dict = room[current_room]
                # Condition to check if the second element of the list is a key in the current room
                if command_list[1] in room_dict:
                    # Assign the current room the value of the key
                    current_room = room_dict[command_list[1]]  # get to the next room
                # Condition to check the second element in the list created from user input
                else:
                    print(f"Can't {command}")  # Output to user
                    print("Type 'GPS' for possible directions")  # Output to user
                    continue
            # Condition to check if the second element of the list is a valid entry
            else:
                print("I don't understand")  # Output to user
                continue
        # Condition to check user input is for directions
        elif command.lower() == 'gps':
            # Function call to display directions to player
            gps(current_room)
            continue
        # Condition when user enters an invalid input
        else:
            print('Invalid Entry')


# Condition to check the location
if __name__ == '__main__':
    # Function call to start the game
    main()


