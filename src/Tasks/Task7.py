### Task #7
"""
Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.

Is divisible by 4 -> is divisible by 100 -> is divisible by 400 -> LEAP YEAR

Is divisible by 4 -> LEAP YEAR

"""
Year = int(input(f"Enter any year: "))
print(f"Year is {Year}")
print(type(Year))

if( Year%4 ==0) and ( Year%100 !=0):
    print(f"{Year} is a Leap year ")
elif((Year%4 ==0) and (Year%100 ==0) and (Year%400)==0):
    print(f"{Year} is a Leap year ")
else:
    {
        print(f"{Year} is Not a Leap Year")
    }