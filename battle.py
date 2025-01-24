from monster import Monster
from combat import player_combat
from armoury import load_weapons
from armour import load_armour
import random
from persistance import GamePersistence

def battle_room(floor, player):
        
    print(f"\nYou enter Floor {floor} of the Battle Rooms.")
    monster = Monster.generate_monster(floor)

    persistance = GamePersistence()
    try:
        text = persistance.loadData('text_data', 'text_saves')
    except Exception as e:
        print(f"error loading text files: {e}")

    name = monster.name.lower()
    print(text.get(name))

    print(f"A {monster.name} appears!")
    
    #battle logic
    monster_defeated = False
    while monster_defeated == False:
        monster_defeated, player_defeated, player_dead = player_combat(floor, player, monster)
        if player_defeated:
            break
        
    if monster_defeated:
        print(f"You defeated the {monster.name}!")
    if player_defeated:
        print(f"You were defeated by {monster.name}!")
        return False, player, player_dead
    if player_dead:
        return False, player, player_dead
    
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
            if a.name == monster.armor:
                armour = a

        choice = input(f"Do you want to replace your {player.armour.name} with {armour.name}? (yes/no): ")
        if choice.lower() == 'yes':
            player.armour = armour
            print(f"You equipped {player.armour.name}.")
    
    return True, player, player_dead  # Return True if the player wins the battle, along with updated equipment

def battle_rooms(player, floor):

    max_floors = 10

    while floor <= max_floors:
        victory, player, player_dead = battle_room(floor, player)
        
        if victory:
            player.cleared_floors += 1
            if floor < max_floors:
                choice = input(f"You've completed Floor {floor}. Do you want to proceed to the next floor? (yes/no): ")
                if choice.lower() != 'yes':
                    print("Returning to the starting room.")
                    floor += 1
                    return "start", player, floor
            else:
                print(f"Congratulations! You've completed all {max_floors} floors of the Battle Rooms!")
                floor = 1
                return "start", player, floor
        else:
            if player_dead:
                print('You have died, sending you back to start room')
            else:
                print("You were defeated. Returning to the starting room.")
            return "start", player, floor

    return "start", player, floor