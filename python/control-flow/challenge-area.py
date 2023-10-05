# Write a Python program to calculate and display the surface area of a user-chosen geometric shape. The 3 possible choices are a square, a circle and a triangle.

import math

shape = input("pick a shape: square (s), circle (c), triangle (t)? ")

match shape:
    case "s":
        side = int(input("what is the lenght of the side? "))
        print(f"Your're square has an area of {side * side}")
    case "c":
        rad = int(input("what is the radius of your circle? "))
        print(f"Your circle has an area of {math.pi * rad ** 2}")
    case "t":
        base = int(input("what is the base of your triangle? "))
        height = int(input("what is the height of your triangle?")) 
        print(f"Your triangle is {base * height / 2}")
    case _:
        print("pick t, c or s!")