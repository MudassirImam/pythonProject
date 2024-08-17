"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""
# Take 2 inputs from the user num1, num2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# max of two numbers below
int_max = max(num1, num2)
print(f"maximum number is: {int_max}")

# pow num1 to num2
int_pow = pow(num1, num2)
print(f"POW of 2 number is: {int_pow}")

# sub, mul, sum, div.
int_sub = num1-num2
print(f"Num1 - Num2 is: {int_sub}")

int_mul = num1*num2
print(f"Num1 * Num2 is: {int_mul}")

int_sum = num1+num2
print(f"Num1 + Num2 is: {int_sum}")

int_div = num1/num2
print(f"Num1 / Num2 is: {int_div}")

