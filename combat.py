import random

def player_combat(floor, player, monster):
    # Array to store the damage of each move
    moves = {"slash": 2 + player.weapon.damage, "stab": player.weapon.damage}
    
    while True:
        # Display moves
        print("Your moves:")
        for i, move in enumerate(moves, 1):
            print(f'{i}. {move}')
        
        # Player's turn
        try:
            choice = input('Enter which attack you want to use (enter name): ')
            damage = moves.get(choice.lower())
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
        print(f'Your armor durability: {player_armor.durability}')
        print("--------------------")
