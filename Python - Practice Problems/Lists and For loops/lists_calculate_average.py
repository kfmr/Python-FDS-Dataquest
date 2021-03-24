values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]


#pythonic way
average = sum(values) / len(values)
print(average)

#another code with for loop
sum_values = 0
len_values = 0
for value in values:
    sum_values+=value
    len_values+=1
    
average_of_values = sum_values / len_values

print(average_of_values)
    