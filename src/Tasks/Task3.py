"""
Explain the difference between the = operator and the == operator in Python.

What does the ** operator do in Python, and how is it used?

What does the ^ operator do in Python, and in what context is it commonly used?

 """

"""
1. Explain the difference between the = operator and the == operator in Python.

= Operator (Assignment Operator)
Purpose: Used to assign a value to a variable.

Usage: This operator sets the value of a variable.

x = 10

== Operator (Equality Operator)
Purpose: Used to compare two values to check if they are equal.

Usage: This operator returns True if the values on both sides are equal and False otherwise.

x = 10
y = 20
result = (x==y)
print(result) # This will print false
"""
#------------------------------------------------------
""" 2. What does the ** operator do in Python, and how is it used?

1. Exponentiation
When used between two numbers, ** performs exponentiation. It raises the number on the left (the base) to
the power of the number on the right (the exponent).

result = 2**3 # 2 raise to the power of 3
print(result) # output: 8

2. Unpacking Keyword Arguments
In function calls, ** is used to unpack a dictionary into keyword arguments

def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

# dictionary with arguments
args =  {"name": "Mudassir", "age": 30}

# unpack dictionary into keyword arguments
greet(**args)

"""

"""
3. What does the ^ operator do in Python, and in what context is it commonly used?

#In Python, the ^ operator is used for bitwise XOR (exclusive OR) operations.
#It operates on the binary representations of integers.

Bitwise XOR Operation
The bitwise XOR operator compares each bit of two integers. For each bit, it returns 1
if the bits are different and 0 if they are the same.
"""


a = 12 # binary: 1100
b = 10 # binary: 1010

result = a^b  # binary:  0110 (Decimal: 6)
print(result)

"""
Context of Use
1. Bitwise Manipulation:

The ^ operator is commonly used in low-level programming or when working directly with bits, 
such as in cryptographic algorithms, network protocols, or certain optimizations.
"""

"""
2. Swapping Variables:
It can be used to swap two variables without using a temporary variable:
"""
a = 10 # binary: 1010
b = 8  # binary: 1000

a = a^b # 0010
b = a^b # 1010
a = a^b # 1000

print(a) # output: 8
print(b) # output: 10

"""
3. Finding the Single Different Element:

It is also useful in problems where you need to find a single unique element in an array where every other
 element appears twice. XOR-ing all elements together will cancel out the pairs, leaving only the unique 
 element:
"""
nums = [1, 2, 3, 2, 1]
unique = 0

for num in nums:

 unique = unique^num
 print(f"Unique number in an array is: {unique}")


