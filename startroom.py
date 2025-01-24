def start_room():
    # Display the starting room options to the player
    print("\nYou are in the starting room.")
    print("1. Enter the Armoury")
    print("2. Enter the Armour Room")
    print("3. Enter the Battle Rooms")
    print("4. Exit the game")
    print("5. Save or Load game")
    
    while True:
        # Prompt the player to choose an option
        choice = input("Where would you like to go? ")
        
        # Return the corresponding room or action based on the player's choice
        if choice == "1":
            return "armoury"
        elif choice == "2":
            return "armour"
        elif choice == "3":
            return "battle"
        elif choice == "4":
            return "exit"
        elif choice == "5":
            return "save/load"
        else:
            # Inform the player of an invalid choice and prompt again
            print("Invalid choice. Please try again.")
