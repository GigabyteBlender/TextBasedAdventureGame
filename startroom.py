def start_room():
    print("\nYou are in the starting room.")
    print("1. Enter the Armoury")
    print("2. Enter the Armour Room")
    print("3. Enter the Battle Rooms")
    print("4. Exit the game")
    
    while True:
        choice = input("Where would you like to go? ")
        
        if choice == "1":
            return "armoury"
        elif choice == "2":
            return "armour"
        elif choice == "3":
            return "battle"
        elif choice == "4":
            return "exit"
        else:
            print("Invalid choice. Please try again.")
