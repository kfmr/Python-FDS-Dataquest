#Convert string to float in a list

from csv import reader
open_file = open('dq_unisex_names.csv', 'r')
read_file = csv.reader(open_file)
dq_unisex_names_csv = list(read_file)
rows = dq_unisex_names_csv[1:]

for row in rows:
    row[1] = float(row[1])
    
print(rows[:5])
print(type(row[1]))
print(rows[1])