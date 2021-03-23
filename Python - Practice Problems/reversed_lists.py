"""
Write a program to check whether values1 is the reverse of values2. Assign the answer to a boolean variable named is_reversed. Both lists have the same length.
"""

values1 = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 101, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]
values2 = [97, 119, 113, 92, 108, 120, 107, 81, 102, 114, 110, 111, 81, 107, 108, 93, 94, 109, 111, 109, 80]

is_reversed = True
for value in values1:
    if value != values2[-1:]:
        is_reversed = False
    
    
is_reversed = True
for i in range(len(values1)):
    if values1[i] != values2[-i - 1]:
        is_reversed = False