#check if a triangle is equilateral, isosceles, or scalene based on its side lengths using if-else.
# Input side lengths
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if side1 == side2 and side2 == side3:
    print("It's an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("It's an isosceles triangle.")
else:
    print("It's a scalene triangle.")
