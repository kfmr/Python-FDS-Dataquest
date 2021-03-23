"""Read the data from dq_unisex_names.csv.
Create a list rare_names and add to it all names whose estimated number is at most 1,000.
Optional steps to test your answer:

Print the first five names in rare_names."""

from csv import reader
dq_unisex_names_csv = open('dq_unisex_names.csv')
read_file = reader(dq_unisex_names_csv)
unisex_names_csv_data = list(read_file)

rare_names = []
for row in unisex_names_csv_data[1:]:
    name = row[0]
    estimated_number = float(row[1])
    if estimated_number <=1000:
        rare_names.append(name)
        
print(rare_names[:5])