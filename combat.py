import json
import random
from weaponMoves import Moves

def load_moves():
    # Load moves from a JSON file and return a list of Moves objects
    with open('moves.json', 'r') as f:
        moves_data = json.load(f)
    return [Moves(**item) for item in moves_data]

def display_moves(moves_list):
    # Display the available moves to the player
    print("\nAvailable moves:\n")
    for i, move in enumerate(moves_list, 1):
        print(f"{i}. {move.name} - Damage: {move.damage}, Speed: {move.speed}")

def player_combat(floor, player, monster):
    # Adjust monster's health based on the current floor level
    monster.health *= floor

    while True:
        # Display moves
        moves_list = load_moves()
        display_moves(moves_list)
        
        # Player's turn
        try:
            # Get player's move choice
            choice = input('\nEnter which attack you want to use (enter number): ')
            move = moves_list[int(choice) - 1]
            damage = move.damage

            if damage is None:
                raise ValueError
            print(f'You dealt {damage} damage to the monster')
            monster.health -= damage
            
            # Check if the monster is defeated
            if monster.health <= 0:
                return True, False, False
        except ValueError:
            print('Invalid input. Try again.')
            continue
        
        # Monster's turn
        monster_damage = random.randint(1, monster.attack)
        player_damage_taken = max(0, monster_damage)
        print(f'The monster attacks you for {player_damage_taken} damage')
        player.armour.durability -= player_damage_taken
        
        # Check if player's armour is broken
        if player.armour.durability <= 0:
            player.hp -= abs(player.armour.durability)
            player.armour.durability = 0
            print("Your armor has been destroyed!")
            # Check if the player is defeated
            if player.hp <= 0:
                return False, True, True
            else:
                return False, True, False
        
        # Display current health and armour status
        print(f'Monster health: {monster.health}')
        print(f'Your armor durability: {player.armour.durability}, Your current health: {player.hp}')
        print("----------------------------------")