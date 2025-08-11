# To finish this project, you have to know what lists do and how they behave
# You also need to know about the split() function and how it works.
# test_numbers = [25, 10, 23]
# result = addition(test_numbers)
# print(result)

"""
Calculator Version 2:
This calculator is an imnprovement on the previous one, This one takes more
than one argument. The downside is that it can perform only one operation at a time.
In version 3, I am gonna make one that can perform with multiple operation and also more than 2
arguments. It would also follow the order of operation.
"""

# Here are the functions

def division(numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total /= num
    return(total)

def subtraction(numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total -= num
    return (total)

def addition(numbers):
    total = 0
    for num in numbers:
        total += num
    return (total)

def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return (total)

# Take the choice operator of the user
choice = int(input("Choose Operator:\n1. Addition \n2. Subtraction\n3. Multiplication\n4. Division\n"))
# Take the numbers they want to operate on, separated by a space
raw_numbers = input("Input numbers to calculate (separate them with a space): ")
# Split numbers by space, convert to float and store in a list
numbers = [float(num) for num in raw_numbers.split()]

if choice == 1:
    result = addition(numbers)
    print(result)
if choice == 2:
    result = subtraction(numbers)
    print(result)
if choice == 3:
    result = multiply(numbers)
    print(result)
if choice == 4:
    result = division(numbers)
    print(result)