from startroom import start_room
from armoury import armoury_room, Weapon
from armour import armour_room, Armour
from battle import battle_rooms
from saveSytem import choose_option, save_text_data
from player import Player


def main():

    save_text_data()
    
    print("Welcome to the Tower of Trials!")
    while True:
        try:
            player_name = input('Enter your player name: ')
            player_age = int(input('Enter your player age: '))
            break
        except:
            print('cannot use that input')
            
    current_room = "start"
    player_weapon = Weapon("Basic Sword", 4, 5, 'None')
    player_armour = Armour("Cloth Armor", 2, 1, 12, 'None')
    cleared_floors = 0

    player = Player(player_name, player_age, player_armour, player_weapon, cleared_floors, current_room)
    floor = 1
    
    while True:
        if current_room == "start":
            current_room = start_room()
        elif current_room == "armoury":
            current_room, player = armoury_room(player)
        elif current_room == "armour":
            current_room, player = armour_room(player)
        elif current_room == "battle":
            if player_armour.durability <= 0:
                print("you cannot enter the room with broken armour")
                current_room = "start"
            else:
                current_room, player, floor = battle_rooms(player, floor)
        elif current_room == "save/load":
            current_room, player = choose_option(player)
        elif current_room == "exit":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
