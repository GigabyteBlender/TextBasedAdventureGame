from persistance import GamePersistence
import os

persistance = GamePersistence()

def save_text_data():
    #saving the text files into the database
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
                save_data[filename] = content

    try:
        persistance.saveData(save_name, save_data, 'text_saves')
    except Exception as e:
        print(f"error saving text files: {e}")

def save_player_data(player):
    """Saves the player's data to Object Storage."""
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
        persistance.saveGame(player.name, player_data)
    except Exception as e:
        print(f'error saving: {e}')
    print('saved data')

def load_player_data(save_name):
    """Loads the player's data from Object Storage."""
    try:
        player_data = persistance.loadGame(save_name)
        print('loaded data succesfully')
        print(player_data)
        return player_data

    except Exception as e:
        print(f"Error loading save file {save_name}: {e}")
        return None


def save_game(player):
    print("Saving the game...")
    save_player_data(player)

def continue_game():
    print("Continuing the game...")
    
def choose_option(player):
    choice = input('Enter what you want to do: ')
    
    try:
        if choice == 'save':
            save_player_data(player)
            
        elif choice == 'load':
            save_name = input('enter save name: ')
            player = load_player_data(save_name)
    except:
        print('error with parsing data')
        pass
        
    return 'start', player
