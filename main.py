from startroom import start_room
from armoury import armoury_room, Weapon
from armour import armour_room, Armour
from battle import battle_rooms

def main():
    print("Welcome to the Tower of Trials!")
    current_room = "start"
    player_weapon = Weapon("Basic Sword", 4, 5)
    player_armor = Armour("Cloth Armor", 2, 1)
    
    while True:
        if current_room == "start":
            current_room = start_room()
        elif current_room == "armoury":
            current_room, player_weapon = armoury_room(player_weapon)
        elif current_room == "armour":
            current_room, player_armor = armour_room(player_armor)
        elif current_room == "battle":
            current_room, player_weapon, player_armor = battle_rooms(player_weapon, player_armor)
        elif current_room == "exit":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
