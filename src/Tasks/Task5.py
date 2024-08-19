#  Create a program that takes two numbers as input and prints
#  whether the first number is greater than, less than, or equal to the second number.

number1 = int(input(f"Enter the number1: "))
number2 = int(input(f"Enter the number2: "))

print(f"number1 is: {number1}")
print(f"number2 is: {number2}")

if number1 > number2:
 print(f"First number {number1} is greater than second number {number2}")

if number1 < number2:
 print(f"First number {number1} is less than Second number {number2}")

else:
 print(f"First number {number1} is equal to second number {number2}")


