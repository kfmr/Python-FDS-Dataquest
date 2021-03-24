from csv import reader
open_file = open('dq_unisex_names.csv', 'r')
read_file = csv.reader(open_file)
dq_unisex_names_csv = list(read_file)
rows = dq_unisex_names_csv[1:]

#append the lenght of the name to the respective row
for row in rows:
    len_name = len(row[0])
    row.append(len_name)
    
print(rows[:5])