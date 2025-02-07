from persistance import GamePersistence
import os
from player import Player
from armoury import Weapon
from armour import Armour


# Initialize the GamePersistence object
persistance = GamePersistence()

def save_text_data():
    # Save the text files into the database
    save_name = 'text_data'
    # Define the folder path
    folder_path = 'text'

    # Initialize the save_data dictionary
    save_data = {}

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                save_data[filename[:-4]] = content  # Remove the '.txt' extension

    try:
        # Save the text data to the database
        persistance.saveData(save_name, save_data, 'text_saves')
    except Exception as e:
        print(f"error saving text files: {e}")

def save_player_data(player):
    """Saves the player's data to Object Storage."""
    # Create a dictionary with the player's data
    player_data = {
        "name": player.name,
        "weapon": player.weapon,
        "armour": player.armour,
        "age": player.age,
        "hp": player.hp,
        "inventory": player.inventory,
        "current_location": player.current_location,
        "cleared_floors": player.cleared_floors
    }
    # Assuming the save file name is based on player's name
    print('saving data')
    try:
        # Save the player's data to the database
        persistance.saveGame(player.name, player_data)
    except Exception as e:
        print(f'error saving: {e}')
    print('saved data')

def load_player_data(save_name):
    """Loads the player's data from Object Storage."""
    try:
        # Load the player's data from the database
        player_data = persistance.loadGame(save_name)
        
        player_name = player_data.get("name")
        
        weapon_data = player_data.get("weapon")
        player_weapon = Weapon(**weapon_data)
        
        armour_data = player_data.get("armour")
        player_armour = Armour(**armour_data)
        
        player_age = player_data.get("age")
        player_hp = player_data.get("hp")
        inventory = player_data.get("inventory")
        cleared_floors = player_data.get("cleared_floors")
        current_room = player_data.get("current_location")
        
        player = Player(player_name, player_weapon, player_armour, player_age, player_hp, inventory, cleared_floors, current_room)
        
        print(f'loaded data from -{player_name}- successfully')
        return player
    except Exception as e:
        print(f"Error loading save file {save_name}: {e}")
        return None

def save_game(player):
    # Save the game by saving the player's data
    print("Saving the game...")
    save_player_data(player)

def continue_game():
    # Placeholder function for continuing the game
    print("Continuing the game...")

def choose_option(player):
    # Prompt the user to choose an option
    choice = input('Enter what you want to do: ')
    
    try:
        if choice == 'save':
            # Save the player's data
            save_player_data(player)
        elif choice == 'load':
            # Load the player's data
            save_name = input('enter save name: ')
            player = load_player_data(save_name)
    except:
        print('error with parsing data')
        pass
        
    return 'start', player
