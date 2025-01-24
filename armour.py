import json

class Armour:
    def __init__(self, name, defense, weight, durability, special):
        self.name = name
        self.defense = defense
        self.weight = weight
        self.durability = durability
        self.special = special

# Function to load armour data from a JSON file and create Armour objects
def load_armour():
    with open('armour.json', 'r') as f:
        armour_data = json.load(f)
    return [Armour(**item) for item in armour_data]

# Function to display a list of available armour
def display_armour(armour_list):
    print("\nAvailable Armour:")
    for i, armour in enumerate(armour_list, 1):
        print(f"{i}. {armour.name} - Defense: {armour.defense}, Weight: {armour.weight}, Durability: {armour.durability}, Skill: {armour.special}")

# Function to handle the armour room logic
def armour_room(player):
    armour_list = load_armour()  # Load the list of armour

    while True:
        print(f"\nYou are in the Armour Room. Current Armour: {player.armour.name}")
        print("1. View available armour")
        print("2. Change armour")
        print("3. Return to start room")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
            # Display the list of available armour
            display_armour(armour_list)
        elif choice == '2':
            # Display the list of available armour and allow the player to change their armour
            display_armour(armour_list)
            armour_choice = input("Choose an armour piece (number) or 'cancel': ")
            if armour_choice.lower() == 'cancel':
                continue
            try:
                # Equip the chosen armour
                new_armour = armour_list[int(armour_choice) - 1]
                player.armour = new_armour
                print(f"You have equipped {new_armour.name}.")
                return "start", player
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
        elif choice == '3':
            # Return to the start room
            return "start", player
        else:
            print("Invalid choice. Please try again.")