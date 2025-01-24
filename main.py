from startroom import start_room
from armoury import armoury_room, Weapon
from armour import armour_room, Armour
from battle import battle_rooms
from saveSytem import choose_option, save_text_data
from player import Player

def main():
    '''Main function to run the game'''

    # Uncomment the line below to save the text data to the database
    # save_text_data()
    
    print("Welcome to the Tower of Trials!")
    
    # Get player name and age with input validation
    while True:
        try:
            player_name = input('Enter your player name: ')
            player_age = int(input('Enter your player age: '))
            break
        except:
            print('cannot use that input')
    
    # Initialize game variables
    current_room = "start"
    player_weapon = Weapon("Basic Sword", 4, 5, 'None')
    player_armour = Armour("Cloth Armor", 2, 1, 12, 'None')
    cleared_floors = 0

    # Create player object
    player = Player(player_name, player_age, player_armour, player_weapon, cleared_floors, current_room)
    floor = 1
    
    # Main game loop
    while True:
        match current_room:
            case "start":
                current_room = start_room()
            case "armoury":
                current_room, player = armoury_room(player)
            case "armour":
                current_room, player = armour_room(player)
            case "battle":
                # Check if player's armour is broken before entering battle
                if player_armour.durability <= 0:
                    print("you cannot enter the room with broken armour")
                    current_room = "start"
                else:
                    current_room, player, floor = battle_rooms(player, floor)
            case "save/load":
                current_room, player = choose_option(player)
            case "exit":
                print("Thank you for playing!")
                break
            
            case _:
                print("Invalid room. Returning to start.")
                current_room = "start"

if __name__ == "__main__":
    main()
