from monster import Monster
from combat import player_combat
from armoury import Weapon, load_weapons
from armour import Armour, load_armour
import random

def battle_room(floor, player):
        
    print(f"\nYou enter Floor {floor} of the Battle Rooms.")
    monster = Monster.generate_monster(floor)
    print(f"A {monster.name} appears!")
    
    #battle logic
    monster_defeated = False
    while monster_defeated == False:
        monster_defeated, player_defeated = player_combat(floor, player, monster)
        if player_defeated:
            break
        
    if monster_defeated:
        print(f"You defeated the {monster.name}!")
    if player_defeated:
        print(f"You were defeated by {monster.name}!")
    
    # Weapon drop
    if random.random() < 0.5:  # 50% chance to drop weapon
        print(f"The {monster.name} dropped its {monster.weapon}!")
        weapon_list = load_weapons()
        for w in weapon_list:
            if w.name == monster.weapon:
                weapon = w
        
        choice = input(f"Do you want to replace your {player.weapon.name} with {weapon.name}? (yes/no): ")
        if choice.lower() == 'yes':
            player.weapon = weapon
            print(f"You equipped {player.weapon.name}.")
    
    # Armor drop
    if random.random() < 0.5:  # 50% chance to drop armor
        print(f"The {monster.name} dropped its {monster.armor}!")
        armour_list = load_armour()
        for a in armour_list:
            if a.name == monster.armour:
                armour = a

        choice = input(f"Do you want to replace your {player.armour.name} with {armour.name}? (yes/no): ")
        if choice.lower() == 'yes':
            player.armour = armour
            print(f"You equipped {player.armour.name}.")
    
    return True, player  # Return True if the player wins the battle, along with updated equipment

def battle_rooms(player):
    current_floor = 1
    max_floors = 10

    while current_floor <= max_floors:
        victory, player = battle_room(current_floor, player)
        
        if victory:
            player.cleared_floors += 1
            if current_floor < max_floors:
                choice = input(f"You've completed Floor {current_floor}. Do you want to proceed to the next floor? (yes/no): ")
                if choice.lower() != 'yes':
                    print("Returning to the starting room.")
                    return "start", player
            else:
                print(f"Congratulations! You've completed all {max_floors} floors of the Battle Rooms!")
                return "start", player
            
            current_floor += 1
        else:
            print("You were defeated. Returning to the starting room.")
            return "start", player

    return "start", player