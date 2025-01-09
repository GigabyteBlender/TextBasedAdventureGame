from monster import Monster
from combat import player_combat
from armoury import Weapon
from armour import Armour
import random

def battle_room(floor, player_weapon, player_armor):
    print(f"\nYou enter Floor {floor} of the Battle Rooms.")
    monster = Monster.generate_monster(floor)
    print(f"A {monster.name} appears!")
    
    # Here you would implement battle logic
    defeated = False
    while defeated == False:
        defeated = player_combat(floor, player_weapon, player_armor, monster)
        
    print(f"You defeated the {monster.name}!")
    
    # Weapon drop
    if random.random() < 0.5:  # 50% chance to drop weapon
        print(f"The {monster.name} dropped its {monster.weapon}!")
        choice = input(f"Do you want to replace your {player_weapon.name} with {monster.weapon}? (yes/no): ")
        if choice.lower() == 'yes':
            player_weapon = Weapon(monster.weapon, monster.attack, random.randint(3, 8))
            print(f"You equipped {player_weapon.name}.")
    
    # Armor drop
    if random.random() < 0.5:  # 50% chance to drop armor
        print(f"The {monster.name} dropped its {monster.armor}!")
        choice = input(f"Do you want to replace your {player_armor.name} with {monster.armor}? (yes/no): ")
        if choice.lower() == 'yes':
            player_armor = Armour(monster.armor, monster.attack // 2, random.randint(2, 7))
            print(f"You equipped {player_armor.name}.")
    
    return True, player_weapon, player_armor  # Return True if the player wins the battle, along with updated equipment

def battle_rooms(player_weapon, player_armor):
    current_floor = 1
    max_floors = 10

    while current_floor <= max_floors:
        victory, player_weapon, player_armor = battle_room(current_floor, player_weapon, player_armor)
        
        if victory:
            if current_floor < max_floors:
                choice = input(f"You've completed Floor {current_floor}. Do you want to proceed to the next floor? (yes/no): ")
                if choice.lower() != 'yes':
                    print("Returning to the starting room.")
                    return "start", player_weapon, player_armor
            else:
                print(f"Congratulations! You've completed all {max_floors} floors of the Battle Rooms!")
                return "start", player_weapon, player_armor
            
            current_floor += 1
        else:
            print("You were defeated. Returning to the starting room.")
            return "start", player_weapon, player_armor

    return "start", player_weapon, player_armor
