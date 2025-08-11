x = float(input("What is the first side: "))
y = float(input("What is the second side: "))
z = float(input("What is the third side: "))

if x == y and y == z:
    print("This is an equilatarel triangle")
elif x == y or x == z or y == z:
    print("This is an isosceles triangle")
else:
    print("it is a scalene triangle")