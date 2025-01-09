import random

def player_combat(floor, player_weapon, player_armor, monster):
    #array to store the damage of each move
    moves = {"slash": 2+player_weapon.damage, "stab": player_weapon.damage}
    
    #displays moves
    x = 0
    for move in moves:
        x += 1
        print(f'{x}.{move}')
    
    #entering move choic and calculating damage of move
    try:
        choice = str(input('Enter which attack you want to use (enter name): '))
    except:
        print('Invalid input')
        
    damage = moves.get(choice)
    
    print(f'you dealt {damage} to the monster')
    monster.health -= damage
    if monster.health <= 0:
        return True
    else:
        return False
    
    
    
    