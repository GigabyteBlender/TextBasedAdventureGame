class Player:
    # Player class to store player information
    def __init__(self, player_name, player_age, player_armour, player_weapon, cleared_floors, current_room):
        self.name = player_name
        self.weapon = player_weapon
        self.armour = player_armour
        self.age = player_age
        self.hp = 100
        self.inventory = {'1': None, '2': None, '3': None, '4': None, '5': None}
        self.current_location = current_room
        self.cleared_floors = cleared_floors
    