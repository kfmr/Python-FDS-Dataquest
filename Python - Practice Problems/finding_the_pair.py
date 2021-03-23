"""
Find two distinct numbers in values whose sum is equal to 100.
Assign one of them to value1 and the other one to value2.
If there are several solutions, any one will be marked as correct.

Optional step to check your answer:

Print the value of value1 and value2.
"""


values = [72, 50, 48, 50, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15, 50, 50]

value1 = None
value2 = None
for x in values:
    for y in values:
        if x + y == 100 and x != y:
            value1 = x
            value2 = y
        
print(value1)
print(value2)