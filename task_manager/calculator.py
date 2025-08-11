# Create the functions for calculating stuff

# This is the addition function
def addition(n1, n2): 
    return (n1 + n2)

# This is the multiplication function
def multiply(n1, n2):
    return (n1 * n2)

# This is the subtraction function
def subtraction(n1, n2):
    return (n1 - n2)

# This is the division function
def division(n1, n2):
    return (n1 / n2)

# This is the modular function
def modular(n1, n2):
    return (n1 % n2)

# print(multiply(5, 2))
# print(addition(5, 2))
# print(subtraction(5, 2))
# print(division(5, 2))
# print(modular(5, 2))

# Ask the user to choose the kind for calculation they want to do

print("1. Addition\n2. Multiplication\n3. Division\n4. Subtraction\n5. Modular")
sel = int(input("Choose 1 - 5 for the operation: "))

# Ask the user to enter two numbers

num1 = int(input("What is your first number: "))
num2 = int(input("What is your second number: "))

# Use a conditional statement to choose the calculation to be done.

if sel == 1:
    result = addition(num1, num2)
    print(result)
elif sel == 2:
    result = multiply(num1, num2)
    print(result)
elif sel == 3:
    result = division(num1, num2)
    print(result)
elif sel == 4:
    result = subtraction(num1, num2)
    print(result)
elif sel == 5:
    result = modular(num1, num2)
    print(result)
else:
    print("You did not enter a valid number")