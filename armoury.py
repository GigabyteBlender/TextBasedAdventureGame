import json

# Define a Weapon class with attributes for name, damage, speed, and special ability
from dataclasses import dataclass

@dataclass(frozen=False)
class Weapon:
    def __init__(self, name, damage, speed, special):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.special = special

# Function to load weapons from a JSON file and return a list of Weapon objects
def load_weapons():
    with open('weapons.json', 'r') as f:
        weapon_data = json.load(f)
    return [Weapon(**item) for item in weapon_data]

# Function to display a list of available weapons
def display_weapons(weapon_list):
    print("\nAvailable Weapons:")
    for i, weapon in enumerate(weapon_list, 1):
        print(f"{i}. {weapon.name} - Damage: {weapon.damage}, Speed: {weapon.speed}, Ability: {weapon.special}")

# Function to handle the armoury room logic
def armoury_room(player):
    weapon_list = load_weapons()  # Load the list of weapons
    
    while True:
        print(f"\nYou are in the Armoury. Current Weapon: {player.weapon.name}")
        print("1. View available weapons")
        print("2. Change weapon")
        print("3. Return to start room")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
            # Display the list of available weapons
            display_weapons(weapon_list)
        elif choice == '2':
            # Display the list of available weapons and allow the player to change their weapon
            display_weapons(weapon_list)
            weapon_choice = input("Choose a weapon (number) or 'cancel': ")
            if weapon_choice.lower() == 'cancel':
                continue
            try:
                # Equip the chosen weapon
                new_weapon = weapon_list[int(weapon_choice) - 1]
                player.weapon = new_weapon
                print(f"You have equipped {new_weapon.name}.")
                return "start", player
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
        elif choice == '3':
            # Return to the start room
            return "start", player
        else:
            print("Invalid choice. Please try again.")
