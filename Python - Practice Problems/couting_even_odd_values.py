values = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]

num_even = 0
num_odd = 0

for value in values:
    if value % 2 == 0:
        num_even+=1
    else:
        num_odd+=1