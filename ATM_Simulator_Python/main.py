user_pin = 4521
def authenticate():
    while True:
        try:
            pin = int(input("Enter your fucking pin here: "))
            if user_pin == pin:
                print("Yeah right nigga, it's you..")
                break
            else:
                print("fuck off!!! --> Input your pin again")
        except ValueError:
            print("Print only numbers, dumbass")

    return (f"Welcome Mr. Hydra, you are authenticated")


def choices():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")
    
    options = int(input("Choose an option:\n"))
    return (options)



welcome  = authenticate()
print(welcome)


def main():
    pass