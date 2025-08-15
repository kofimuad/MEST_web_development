# 1. Ask for player's name
print("***************************************")
print("HONEYMOON (ACCRA OR KUMASI) BUDGET GAME")
print("***************************************\n")
name = input("What is your name as a couple? (Hint: Your surname)\n") # First data collected
is_playing = True

print("*****************************************************************")
print(f"Hello Mr. & Mrs. {name}, Welcome to the honeymoon budget game!❤️")
print("*****************************************************************")
print()



def accra(destination, starting_budget):
    if destination == "ACCRA":
        print("Your budget should be GHS10,000 or more.")

        if starting_budget >= 10000:
            print("Tip: If you want a luxury hotel, you would have to budget GHS5,000 on accomodation.\nHowever, if you want a guest house, you would have to budget GHS3,000 on accomodation.")
            accomodation = input("Will you stay at a Luxury Hotel or a Guesthouse?\nOptions:\n L for Luxury Hotel \nG for Guesthouse\n").upper()
            if accomodation == "L":
                starting_budget -= 5000
                print(f"Remaining budget: GHS{starting_budget}")
            elif accomodation == "G":
                starting_budget -= 3000
                print(f"Remaining budget: GHS{starting_budget}")
            else:
                print("Invalid Response")
        else:
            print("Invalid Response")
    else:
        print("Invalid Response")

def kumasi(destination, starting_budget):
    if destination == "KUMASI":
        print("Your budget should be GHS5,000 or more.")

        if starting_budget >= 5000:
            print("Tip: If you want a luxury hotel, you would have to budget GHS3,000 on accomodation.\nHowever, if you want a guest house, you would have to budget GHS1,000 on accomodation.")
            accomodation = input("Will you stay at a Luxury Hotel or a Guesthouse?\nOptions:\nL for Luxury Hotel \nG for Guesthouse\n").upper()
            if accomodation == "L":
                starting_budget -= 3000
                print(f"Remaining budget: GHS{starting_budget}")
            elif accomodation == "G":
                starting_budget -= 1000
                print(f"Remaining budget: GHS{starting_budget}")
            else:
                print("Invalid Response")
    else:
        print("Invalid Response")


def sight_seeing(starting_budget, destination):
    if destination == "KUMASI":
        sight_saw =  input("Select where you want to go (Choose 1 - 3):\n1. Visit Kumasi Zoo (GHS300)\n2. Manhyia Palace Museum (GHS 800)\n3. Visit Rattray Park (GHS 1000)\n")
        if sight_saw == "1":
            starting_budget -= 300
        elif sight_saw == "2":
            starting_budget -= 800
        elif sight_saw == "3":
            starting_budget -= 1000
        else:
            print("Enter 1 - 3")
        print(f"Your have GHS {starting_budget} remaining")

    elif destination == "ACCRA":
        sight_saw =  input("Select where you want to go (Choose 1 - 3):\n1. Jetski at Labadi (GHS1000)\n2. Accra Art Galleries (GHS 500)\n3. Go to Despite's Auto Museum (GHS 1500)\n")
        if sight_saw == "1":
            starting_budget -= 1000
        elif sight_saw == "2":
            starting_budget -= 500
        elif sight_saw == "3":
            starting_budget -= 1500
        else:
            print("Enter 1 - 3")
        print(f"Your have GHS {starting_budget} remaining")
    else:
        print("You can choose only Accra or Kumasi")

def main():
    is_playing = True

    while is_playing:
        destination = input("Where would you like to go for your honeymoon? (Accra / Kumasi)\n").upper()

        starting_budget = float(input("What is your budget for the honeymoon? (GHS10,000 or more for Accra and GHS5000 or more for Kumasi)\nGHS"))

        if destination == "ACCRA":
            accra(destination, starting_budget)
            activities = input("Select Activities(Choose 1 or 2):\n1. Stay In\n2. Sight Seeing\n")
            if activities == "2":
                sight_seeing(starting_budget, destination)
            elif activities == "1":
                print("You have {starting_budget} remaining")
            else:
                print("You can enter just 1 or 2")
        elif destination == "KUMASI":
            kumasi(destination, starting_budget)
            activities = input("Select Activities(Choose 1 or 2):\n1. Stay In\n2. Sight Seeing\n")
            sight_seeing(starting_budget, destination)
            if activities == "2":
                sight_seeing(starting_budget, destination)
            elif activities == "1":
                print("You have {starting_budget} remaining")
            else:
                print("You can enter just 1 or 2")
        else:
            is_playing = False
            print("Invalid destination!\nWe only budget for Accra or Kumasi.")



if __name__ == "__main__":
    main()