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
            return starting_budget, "Luxury Hotel (GHS5000)"
        elif accomodation == "G":
            starting_budget -= 3000
            return starting_budget, "Guesthouse (GHS3000)"
        else:
            print("Invalid Response. Please enter 'L' or 'G'.")

def kumasi(starting_budget):
    """Handles the accommodation budget for Kumasi."""
    while True:
        accomodation = input("Will you stay at a Luxury Hotel or a Guesthouse?\nOptions:\nL for Luxury Hotel \nG for Guesthouse\n").upper()
        if accomodation == "L":
            starting_budget -= 3000
            return starting_budget, "Luxury Hotel (GHS3000)"
        elif accomodation == "G":
            starting_budget -= 1000
            return starting_budget, "Guesthouse (GHS1000)"
        else:
            print("Invalid Response. Please enter 'L' or 'G'.")
    return starting_budget

def sight_seeing(starting_budget, destination):
    """Handles the sightseeing budget based on the destination."""
    if destination == "KUMASI":
        while True:
            sight_saw = input("Select where you want to go (Choose 1 - 3):\n1. Visit Kumasi Zoo (GHS300)\n2. Manhyia Palace Museum (GHS800)\n3. Visit Rattray Park (GHS1000)\n")
            if sight_saw == "1":
                return starting_budget - 300, "Kumasi Zoo (GHS300)"
            elif sight_saw == "2":
                return starting_budget - 800, "Manhyia Palace Museum (GHS800)"
            elif sight_saw == "3":
                return starting_budget - 1000, "Rattray Park (GHS1000)"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    elif destination == "ACCRA":
        while True:
            sight_saw = input("Select where you want to go (Choose 1 - 3):\n1. Jetski at Labadi (GHS1000)\n2. Accra Art Galleries (GHS500)\n3. Go to Despite's Auto Museum (GHS1500)\n")
            if sight_saw == "1":
                return starting_budget - 1000, "Jetski at Labadi (GHS1000)"
            elif sight_saw == "2":
                return starting_budget - 500, "Accra Art Galleries (GHS500)"
            elif sight_saw == "3":
                return starting_budget - 1500, "Despite's Auto Museum (GHS1500)"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    return starting_budget, "No sightseeing"

def dinner_date(starting_budget, destination):
    """Handles the dinner date budget based on the destination."""
    if destination == "ACCRA":
        while True:
            date_night = input("Select where you want to go for dinner (Choose 1 or 2):\n1. Luxury Restaurant (GHS1500)\n2. Casual Restaurant (GHS800)\n")
            if date_night == "1":
                return starting_budget - 1500, "Luxury Restaurant (GHS1500)"
            elif date_night == "2":
                return starting_budget - 800, "Casual Restaurant (GHS800)"
            else:
                print("Invalid choice. Please enter 1 or 2.")
    elif destination == "KUMASI":
        while True:
            date_night = input("Select where you want to go for dinner (Choose 1 or 2):\n1. Luxury Restaurant (GHS1000)\n2. Casual Restaurant (GHS500)\n")
            if date_night == "1":
                return starting_budget - 1000, "Luxury Restaurant (GHS1000)"
            elif date_night == "2":
                return starting_budget - 500, "Casual Restaurant (GHS500)"
            else:
                print("Invalid choice. Please enter 1 or 2.")
    return starting_budget, "No dinner date"

def main():
    """The main function to run the honeymoon budget game."""
    get_name()
    
    while True:
        # Initialize the list for the current game
        honeymoon_choices = []
        
        destination = get_destination()
        honeymoon_choices.append(f"Destination: {destination}")
        
        starting_budget = get_budget(destination)
        
        # Determine accommodation and update budget
        if destination == "ACCRA":
            print("Tip: If you want a luxury hotel, you would have to budget GHS5,000 on accomodation.\nHowever, if you want a guest house, you would have to budget GHS3,000 on accomodation.")
            starting_budget, choice_str = accra(starting_budget)
            honeymoon_choices.append(f"Accommodation: {choice_str}")
        elif destination == "KUMASI":
            print("Tip: If you want a luxury hotel, you would have to budget GHS3,000 on accomodation.\nHowever, if you want a guest house, you would have to budget GHS1,000 on accomodation.")
            starting_budget, choice_str = kumasi(starting_budget)
            honeymoon_choices.append(f"Accommodation: {choice_str}")
            
        print(f"Remaining budget after accommodation: GHS{starting_budget}")

        # Determine activities and update budget
        while True:
            activities = input("Select Activities(Choose 1 or 2):\n1. Stay In\n2. Sight Seeing\n")
            if activities == "1":
                honeymoon_choices.append("Activities: Stay In")
                print(f"You have GHS {starting_budget} remaining. Enjoy your stay!")
                break
            elif activities == "2":
                starting_budget, choice_str = sight_seeing(starting_budget, destination)
                honeymoon_choices.append(f"Activities: {choice_str}")
                print(f"Your have GHS{starting_budget} remaining after sightseeing.")
                break
            else:
                print("You can enter just 1 or 2. Please try again.")

        # Determine dinner date and update budget
        while True:
            dinner_choice = input("Would you like to go on a dinner date? (yes/no)\n").lower()
            if dinner_choice == "yes":
                starting_budget, choice_str = dinner_date(starting_budget, destination)
                honeymoon_choices.append(f"Dinner Date: {choice_str}")
                print(f"Your have GHS{starting_budget} remaining after your dinner date.")
                break
            elif dinner_choice == "no":
                honeymoon_choices.append("Dinner Date: No dinner date")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        
        print(f"\nFinal budget remaining: GHS{starting_budget}")

        ## Display the list of choices
        print("\n***********************************")
        print("YOUR HONEYMOON CHOICES SUMMARY")
        print("***********************************")
        for choice in honeymoon_choices:
            print(f"- {choice}")
        print("\n")

        play_again = input("Would you like to budget for another honeymoon? (yes/no)\n").lower()
        if play_again != "yes":
            print("Thanks for playing! Have a wonderful honeymoon! ❤️")
            break

if __name__ == "__main__":
    main()