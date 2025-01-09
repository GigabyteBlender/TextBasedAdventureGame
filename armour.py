import json

class Armour:
    def __init__(self, name, defense, weight):
        self.name = name
        self.defense = defense
        self.weight = weight

def load_armour():
    with open('armour.json', 'r') as f:
        armour_data = json.load(f)
    return [Armour(**item) for item in armour_data]

def display_armour(armour_list):
    print("\nAvailable Armour:")
    for i, armour in enumerate(armour_list, 1):
        print(f"{i}. {armour.name} - Defense: {armour.defense}, Weight: {armour.weight}")

def armour_room(current_armour):
    armour_list = load_armour()
    
    while True:
        print(f"\nYou are in the Armour Room. Current Armour: {current_armour.name}")
        print("1. View available armour")
        print("2. Change armour")
        print("3. Return to start room")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
            display_armour(armour_list)
        elif choice == '2':
            display_armour(armour_list)
            armour_choice = input("Choose an armour piece (number) or 'cancel': ")
            if armour_choice.lower() == 'cancel':
                continue
            try:
                new_armour = armour_list[int(armour_choice) - 1]
                print(f"You have equipped {new_armour.name}.")
                return "start", new_armour
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
        elif choice == '3':
            return "start", current_armour
        else:
            print("Invalid choice. Please try again.")

            print("Invalid choice. Please try again.")

