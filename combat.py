import random
import json

class Moves:
    def __init__(self, name, damage, speed):
        self.name = name
        self.damage = damage
        self.speed = speed

def load_moves():
    with open('moves.json', 'r') as f:
        moves_data = json.load(f)
    return [Moves(**item) for item in moves_data]

def display_moves(moves_list):
    print("\nAvailable Armour:")
    for i, move in enumerate(moves_list, 1):
        print(f"{i}. {move.name} - Damage: {move.damage}, Speed: {move.speed}")

def player_combat(floor, player, monster):
    
    while True:
        # Display moves
        moves_list = load_moves()
        display_moves(moves_list)
        
        # Player's turn
        try:
            choice = input('Enter which attack you want to use (enter number): ')
            move = moves_list[int(choice) - 1]
            damage = move.damage

            if damage is None:
                raise ValueError
            print(f'You dealt {damage} damage to the monster')
            monster.health -= damage
            
            if monster.health <= 0:
                return True, False
        except ValueError:
            print('Invalid input. Try again.')
            continue
        
        # Monster's turn
        monster_damage = random.randint(1, monster.attack)
        player_damage_taken = max(0, monster_damage)
        print(f'The monster attacks you for {player_damage_taken} damage')
        player.armour.durability -= player_damage_taken
        
        if player.armour.durability <= 0:
            print("Your armor has been destroyed!")
            return False, True
        
        print(f'Monster health: {monster.health}')
        print(f'Your armor durability: {player.armour.durability}')
        print("--------------------")
