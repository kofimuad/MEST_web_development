# HONEY MOON GAME

# import sys
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


while is_playing:
    destination = input("Where would you like to go for your honeymoon ---> Accra / Kumasi\n").upper()

    if destination not in ["ACCRA", "KUMASI"]:
        print("Invalid location. Please choose only Accra or Kumasi.")
        continue  # Go back to the start of the loop

    starting_budget = float(input("What is your budget for the honeymoon? (GHS10,000 or more for Accra and GHS5000 or more for Kumasi)\nGHS"))

    if destination == "ACCRA" and starting_budget < 10000:
        print("You can't come to Accra. STAY HOME!!")
        print("Run program again with better budget")
    elif destination == "KUMASI" and starting_budget < 5000:
        print("You're poor")
    elif destination not in ["ACCRA", "KUMASI"]:
        print("Invalid response. Try again.")


accomodation = input("Will you stay at a Luxury Hotel or a Guesthouse?\nOption 1. L for Luxury Hotel\nOption 2. G for Guesthouse\n").upper()

if accomodation == "L":
    starting_budget -= 5000
elif accomodation == "G":
    print("You should budget GHS 5000 for a month")
    starting_budget -= 3000
else:
    print("Invalid Response")

if destination == "ACCRA":
    activities = input("Select Activities(Choose 1 or 2):\n1. Stay In\n2. Sight Seeing\n")
    if activities == "1":
        print("No money reduction --> Enjoy your solitude together")
    elif activities == "2":
        sight_saw =  input("Select where you want to go (Choose 1 - 3):\n1. Jetski at Labadi (GHS1000)\n2. Accra Art Galleries (GHS 500)\n3. Go to Despite's Auto Museum (GHS 1500)\n")
        if sight_saw == "1":
            starting_budget -= 1000
        elif sight_saw == "2":
            starting_budget -= 500
        elif sight_saw == "3":
            starting_budget -= 1500
        else:
            print("Invalid response")
    else:
        print("Invalid response")
elif destination == "KUMASI":
    activities = input("Select Activities(Choose 1 or 2):\n1. Stay In\n2. Sight Seeing\n")
    if activities == "1":
        print("No money deducted --> Enjoy your solitude together")
    elif activities == "2":
        sight_saw =  input("Select where you want to go (Choose 1 - 3):\n1. Visit Kumasi Zoo (GHS300)\n2. Manhyia Palace Museum (GHS 800)\n3. Visit Rattray Park (GHS 1000)\n")
        if sight_saw == "1":
            starting_budget -= 300
        elif sight_saw == "2":
            starting_budget -= 800
        elif sight_saw == "3":
            starting_budget -= 1000
    else:
        print("Invalid response")
else:
    print("You can choose only Accra or Kumasi")

dinner = input("Where do you want to have dinner? (Choose 1 or 2)\n1. 5 Star Restaurant(GHS 2000)\n2. Chop Bar (GHS 500)\n")
if dinner == "1":
    starting_budget -= 2000
elif dinner == "2":
    starting_budget -= 500
else:
    print("Invalid Input")

print(f"You have GHS{starting_budget} left")

# if starting_budget >

print("***********************")
print("HAVE A NICE HONEYMOON!!\nENJOY YOURSELVES!😌")
print("***********************")

