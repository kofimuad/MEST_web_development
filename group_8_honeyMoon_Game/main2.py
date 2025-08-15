def get_name():
    """Gets the couple's surname to start the game."""
    print("***************************************")
    print("HONEYMOON (ACCRA OR KUMASI) BUDGET GAME")
    print("***************************************\n")
    name = input("What is your name as a couple? (Hint: Your surname)\n")
    print("*****************************************************************")
    print(f"Hello Mr. & Mrs. {name}, Welcome to the honeymoon budget game!❤️")
    print("*****************************************************************")
    print()
    return name

def get_destination():
    """Prompts the user for a valid destination."""
    while True:
        destination = input("Where would you like to go for your honeymoon? (Accra / Kumasi)\n").upper()
        if destination in ["ACCRA", "KUMASI"]:
            return destination
        else:
            print("Invalid destination! We only budget for Accra or Kumasi. Please try again.")

def get_budget(destination):
    """Prompts the user for a valid starting budget."""
    while True:
        try:
            starting_budget = float(input(f"What is your budget for the honeymoon? (GHS{'10,000 or more for Accra' if destination == 'ACCRA' else '5,000 or more for Kumasi'})\nGHS"))
            if (destination == "ACCRA" and starting_budget >= 10000) or (destination == "KUMASI" and starting_budget >= 5000):
                return starting_budget
            else:
                print("Your budget is too low for this destination. Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def accra(starting_budget):
    """Handles the accommodation budget for Accra."""
    while True:
        accomodation = input("Will you stay at a Luxury Hotel or a Guesthouse?\nOptions:\nL for Luxury Hotel \nG for Guesthouse\n").upper()
        if accomodation == "L":
            starting_budget -= 5000
            break
        elif accomodation == "G":
            starting_budget -= 3000
            break
        else:
            print("Invalid Response. Please enter 'L' or 'G'.")
    return starting_budget

def kumasi(starting_budget):
    """Handles the accommodation budget for Kumasi."""
    while True:
        accomodation = input("Will you stay at a Luxury Hotel or a Guesthouse?\nOptions:\nL for Luxury Hotel \nG for Guesthouse\n").upper()
        if accomodation == "L":
            starting_budget -= 3000
            break
        elif accomodation == "G":
            starting_budget -= 1000
            break
        else:
            print("Invalid Response. Please enter 'L' or 'G'.")
    return starting_budget

def sight_seeing(starting_budget, destination):
    """Handles the sightseeing budget based on the destination."""
    if destination == "KUMASI":
        while True:
            sight_saw = input("Select where you want to go (Choose 1 - 3):\n1. Visit Kumasi Zoo (GHS300)\n2. Manhyia Palace Museum (GHS800)\n3. Visit Rattray Park (GHS1000)\n")
            if sight_saw == "1":
                return starting_budget - 300
            elif sight_saw == "2":
                return starting_budget - 800
            elif sight_saw == "3":
                return starting_budget - 1000
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    elif destination == "ACCRA":
        while True:
            sight_saw = input("Select where you want to go (Choose 1 - 3):\n1. Jetski at Labadi (GHS1000)\n2. Accra Art Galleries (GHS500)\n3. Go to Despite's Auto Museum (GHS1500)\n")
            if sight_saw == "1":
                return starting_budget - 1000
            elif sight_saw == "2":
                return starting_budget - 500
            elif sight_saw == "3":
                return starting_budget - 1500
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    return starting_budget

def main():
    """The main function to run the honeymoon budget game."""
    get_name()
    
    while True:
        destination = get_destination()
        starting_budget = get_budget(destination)
        
        # Determine accommodation and update budget
        if destination == "ACCRA":
            starting_budget = accra(starting_budget)
        elif destination == "KUMASI":
            starting_budget = kumasi(starting_budget)
            
        print(f"Remaining budget: GHS{starting_budget}")

        # Determine activities and update budget
        while True:
            activities = input("Select Activities(Choose 1 or 2):\n1. Stay In\n2. Sight Seeing\n")
            if activities == "1":
                print(f"You have GHS {starting_budget} remaining. Enjoy your stay!")
                break
            elif activities == "2":
                starting_budget = sight_seeing(starting_budget, destination)
                print(f"Your have GHS{starting_budget} remaining.")
                break
            else:
                print("You can enter just 1 or 2. Please try again.")

        play_again = input("Would you like to budget for another honeymoon? (yes/no)\n").lower()
        if play_again != "yes":
            print("Thanks for playing! Have a wonderful honeymoon! ❤️")
            break

if __name__ == "__main__":
    main()