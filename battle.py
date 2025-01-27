from monster import Monster
from combat import player_combat
from armoury import load_weapons
from armour import load_armour
import random
from persistance import GamePersistence

def battle_room(floor, player):
    # Print the current floor the player is on
    print(f"\nYou enter Floor {floor} of the Battle Rooms.")
    
    # Generate a monster based on the current floor
    monster = Monster.generate_monster(floor)

    # Load text data for the game
    persistance = GamePersistence()
    try:
        text_data = persistance.loadData('text_data', 'text_saves')
    except Exception as e:
        print(f"Error loading text files: {e}")
        text_data = {}

    # Print the description of the monster
    monster_name = monster.name.lower()
    if monster_name in text_data:
        print(text_data[monster_name])
    else:
        print(f"No description available for {monster.name}.")

    print(f"A {monster.name} appears!")
    
    # Battle logic
    monster_defeated = False
    while not monster_defeated:
        # Engage in combat with the monster
        monster_defeated, player_defeated, player_dead = player_combat(floor, player, monster)
        if player_defeated:
            break
        
    # Check the outcome of the battle
    if monster_defeated:
        print(f"You defeated the {monster.name}!")
    if player_defeated:
        return False, player, player_dead

    
    # Weapon drop logic
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
    
    # Armor drop logic
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
    
    # Return True if the player wins the battle, along with updated equipment
    return True, player, player_dead

def battle_rooms(player, floor):
    # Define the maximum number of floors
    max_floors = 10

    # Loop through each floor until the maximum is reached
    while floor <= max_floors:
        # Engage in a battle room
        victory, player, player_dead = battle_room(floor, player)
        
        if victory:
            # Increment the number of cleared floors if the player wins
            player.cleared_floors += 1
            if floor < max_floors:
                # Ask the player if they want to proceed to the next floor
                floor += 1
                choice = input(f"You've completed Floor {floor}. Do you want to proceed to the next floor? (yes/no): ")
                if choice.lower() != 'yes':
                    print("Returning to the starting room.")
                    return "start", player, floor
            else:
                # Congratulate the player for completing all floors
                print(f"Congratulations! You've completed all {max_floors} floors of the Battle Rooms!")
                floor = 1
                return "start", player, floor
        else:
            # Handle the case where the player is defeated
            if player_dead:
                print('You have died, sending you back to start room')
            else:
                print("You were defeated. Returning to the starting room.")
            return "start", player, floor

    # Return to the starting room if the loop ends
    return "start", player, floor