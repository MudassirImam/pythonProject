# Home Can you create a Program I will give you number(userinput and print table)
"""
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10
"""
table = input("Enter the number for which Multiple table you want to see")
print(type(table))
num_str = table
num_int = int(num_str)
print(type(num_int))
print(f"{num_int}*1={num_int}")
print(f"{num_int}*2={num_int*2}")
print(f"{num_int}*3={num_int*3}")
print(f"{num_int}*4={num_int*4}")
print(f"{num_int}*5={num_int*5}")
print(f"{num_int}*6={num_int*6}")
print(f"{num_int}*7={num_int*7}")
print(f"{num_int}*8={num_int*8}")
print(f"{num_int}*9={num_int*9}")
print(f"{num_int}*10={num_int*10}")
