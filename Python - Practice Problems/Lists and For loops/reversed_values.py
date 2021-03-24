#reverse the numbers of the values list

values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]

reversed_values = []
for value in range(len(values)):
    reversed_values.append(values[-value-1])
    
print(reversed_values)
    