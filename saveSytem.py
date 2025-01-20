from persistance import GamePersistence

persistance = GamePersistence()


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
    except:
        print('error saving')
    print('saved data')


def load_player_data(save_name):
    """Loads the player's data from Object Storage."""
    try:
        player_data = persistance.loadGame(save_name)
        print('loaded data succesfully')
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
            player = load_player_data(player.name)
    except:
        print('error with parsing data')
        pass
        
    return 'start', player
