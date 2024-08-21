"""
Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.

"""

Length = int(input("Enter the length of triangle: "))
Breadth = int(input("Enter the breadth of triangle: "))
Height = int(input("Enter the Height of triangle: "))

print(Length)
print(Breadth)
print(Height)


if(Length==Breadth==Height):
    print("This is an Equilateral Triangle with all sides equal ")

elif(Length==Breadth or Length==Height or Breadth==Height):
    print("This is an isosceles Triangle with two sides equal ")

else:
    print("This is an Scalene Triangle with No sides equal ")