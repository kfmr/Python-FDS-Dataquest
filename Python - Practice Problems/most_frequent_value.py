#Find the most frequent values in values and print it.


values = [72, 50, 48, 50, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 32, 10, 62, 48, 32, 96, 75, 15]

most_frequent = values[0]
for value in values:
    if values.count(value) > values.count(most_frequent):
        most_frequent = value
    

print(most_frequent)