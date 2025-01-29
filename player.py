class Player:
    # Player class to store player information
    def __init__(self, player_name, player_weapon, player_armour, player_age, player_hp, inventory, cleared_floors, current_room):
        self.name = player_name
        self.weapon = player_weapon
        self.armour = player_armour
        self.age = player_age
        self.hp = player_hp
        self.inventory = inventory
        self.current_location = current_room
        self.cleared_floors = cleared_floors
    