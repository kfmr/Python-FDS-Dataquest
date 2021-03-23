"""Write a program that calculates the maximum of the values list without using a built-in function. Assign the maximum value to a variable named maximum.
"""

values = [72, 48, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15]

maximum = 0
for value in values:
    if value > maximum:
        maximum = value