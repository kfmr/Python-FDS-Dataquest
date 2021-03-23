"""
Read the data from dq_unisex_names.csv.
Count how many names have an estimated number greater than or equal to 100,000. Assign the result to a variable named count.
"""

from csv import reader
dq_unisex_names_csv = open('dq_unisex_names.csv')
read_file = reader(dq_unisex_names_csv)
unisex_names_csv_data = list(read_file)

count = 0
for row in unisex_names_csv_data[1:]:
    estimated_number = float(row[1])
    if estimated_number >=100000:
        count+=1