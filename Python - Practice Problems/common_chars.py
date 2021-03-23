"""
Write a program that creates a list named common that contains the characters that are common to both s1 and s2. The list of common characters should not contain duplicates, but it can have any order.
"""

s1 = 'I have been busier these days due to having a lot on my plate.'
s2 = 'You have been very supportive towards my recent endeavors.'

common = []

for letter in s1:
    if letter in s2 and letter not in common:
        common.append(letter)