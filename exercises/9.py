#  Find a function that helps you generate random numbers
import random

rand_x = random.randrange(1, 10)

# Take the user's guess
usr_num = int(input("Guess a number between 1 - 10: "))

# Hint.. The program compares the value to the value generated if it's greater, say too high and it's less. say too low
# Also use the and to find if it is specifically too high or low..

if usr_num == rand_x:
    print("Bingo!")

while usr_num != rand_x:
    print("Wrong Answer")
    if usr_num > rand_x:
        print("Too High!")
        
    else:
        print("Too Low!")
    
    usr_num = int(input("Try Again: "))


print("Bingo!")