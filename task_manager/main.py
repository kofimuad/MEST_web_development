# This program welcomes a user that creates a new account.
# It prompts the user for their name and when they input their name,
# it prints a welcome message. Saying; welcome "user's name".

# Request the user's name
# name = input("What is your name?\n")
# # Print the welcome message with the user's name
# print(f"Welcome, {name}!")


# age = 77 # this is a int data type
# first_name = "Nana"
# last_name = "Akufo-Addo" # this is a string data type
# is_president = False # this is a boolean data type
# years_as_president = 8.5 # this is a float data type
# email = "showbezzy@ghana.gov"



# your_name = input("what is your name? ")
# your_age = input("what is your age? ")
# converted_age = int(your_age)  # Convert the input to an integer
# calc_age = converted_age + 20
# print(f"Hello {your_name}, you will be {calc_age} in 20 years.")


# #Calculator Program

# # Ask user to enter the first number
# first_num = input("Enter number: \n")
# # Ask user to enter the second number
# second_num = input("Enter another number: \n")

# print("Now we wait...")

# # Here we convert the numbers into intergers
# first_num = int(first_num)
# second_num = int(second_num)

# # Add the 2 numbers
# result = first_num + second_num

# print(f"This is the result: {result}\nSimple addition you can't do. Tswww")


# first_name = input("What is your first name? ").upper()

# last_name = input("What is your last name? ").upper()

# print(f"Your fullname in upper case is {first_name} {last_name}")

# print("Your name is " + first_name + " " + last_name)


# # Python full name to UPPERCASE program 

# # Ask user to enter their first name
# first_name = input("What is your first name? ")

# # Ask user to enter their last name 
# last_name = input("What is your last name? ")

# # Print user's fullname in UPPERCASE
# print(f"Your first name in upper case is {first_name.upper()} {last_name.upper()}")

# age = int(input("How old are you? "))
# if age >= 18 and age <= 50:
#     print("You have access")
# else:
#     print("Fuck off!")

# age = int(input("How old are you? "))
# if 18 <= age <= 50:
#     print("You have access")
# else:
#     print("Fuck off!")


# Look up logical operators.

# num = int(input("Input number to check:\n"))

# if num % 2 == 0 :
#     print("The number is even")
# else:
#     print("The number is odd")

# # Ask user to input an integer
# num = int(input("Input number to check: "))
# # Find the interger modulo 2
# mod_ans = (num % 2)

# if mod_ans == 0:
#     print("This is an even number") # If remainder equal zero print even
# else:
#     print("This is an odd number") # Else print odd

# score = float(input("Enter your score: "))

# if score >= 90 and score <= 100:
#     print("grade A")
# elif score >= 80 and score <= 89:
#     print("grade B")
# elif score >= 70 and score <= 79:
#     print("grade C")
# elif score >= 60 and score <= 69:
#     print("grade D")
# else:
#     print("wabon too much ---  grade F")


# score = int(input("Enter your score: "))

# if score >= 90 and score <= 100:
#     print("grade A")
# if score >= 80 and score <= 89:
#     print("grade B")
# if score >= 70 and score <= 79:
#     print("grade C")
# if score >= 60 and score <= 69:
#     print("grade D")
# if score >= 0 and score <= 59:
#     print("grade F")


# Discount calculator

# purchase_amt = float(input("Input your purchase amount here: GHS "))

# if purchase_amt >= 100:
#     dis_amt = purchase_amt - (purchase_amt * 0.2)
#     print(f"This is the price you have to pay GHS {dis_amt}")
# elif purchase_amt >= 50:
#     dis_amt = purchase_amt - (purchase_amt * 0.1)
#     print(f"This is the price you have to pay GHS {dis_amt}")
# else:
#     print(f"No discount allowed for GHS {purchase_amt}")

# We are going to learn about Loops now.

# std1 = "Alex"
# std2 = "Afia"
# std3 = "Hydra"

# students = ["Alex", "Afia", "Hydra"]
# names = []
# for student in students:
#     names.append(student)

# print(names)

# file = open("tasks.txt", "r")
# tasks = file.read().split("\n")
# for task in tasks:
#     print(task)
# for i, task in enumerate(tasks):
#     print(f"{i} {task}")
# for task in tasks:
#     print(f"{tasks.index(task)}. {task}")
# for task in tasks:
#     print(f"{tasks.index(task) + 1}. {task}")

# Use loop to calculate the sum of teh numbers below
# numbers = [10, 5, 20, 8, 15]
# total = 0
# for num in numbers:
#     total += num
# print(total)

# emails = open("emails.txt", "r")
# email_list = emails.read().split("\n") 
# # print(email_list)

# user_name = ""
# for email in email_list:
#     user_name = email.split('@')[0]
#     print(user_name)

# user_names = []
# for email in email_list:
#     user_name = email.split('@')[0]
#     user_names.append(user_name)
# print(user_names)



#  DEMONSTRATE COMPOUNDING INTEREST

# Have the user enter their investment amount and expected interest

# invest_amt = int(input("What amount are you investing? \n"))
# interest = float(input("What's your expected interest? \n"))

# # Each year their investment will increase by (their investment + their investment * interest)
# for i in range(10):
#     invest_amt = invest_amt + (invest_amt * interest)

# # Print out the earnings after 10 years.
# print("{:.2f}".format(invest_amt))

# Ask for money invested + the interest rate

# Convert the value to a float

# Convert value to a float and round the percent


# def register_user(user, email, password):
#     # Check if the user does not already have an account
#     # hash your password
#     # Validate inputs
#     # Check if user is not a robot
#     # Returns response
#     return "User registered successfully"

# register_user("Bismark", "iambismark38@gmail.com", "theeend")


# def my_idi(fname):
#     print(fname + " Lord Finess")

# my_idi("Hydra")

import add
import delete
import show
import update
# Check the files, you will see the code in those files.

add_task_response = add.add_task("sleep")
print(add_task_response)

show_task_response = show.add_task()
print(show_task_response)

update_task_response = add.add_task("sleep", "wake up")
print(update_task_response)

delete_task_response = add.add_task("sleep")
print(delete_task_response)

def add(x, y, z):
    result = x + y + z
    return result
add(5,4,8)