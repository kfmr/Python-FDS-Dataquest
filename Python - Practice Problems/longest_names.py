"""
Read the data from dq_unisex_names.csv.
Create a list named longest_names containing all names with length greater than ten.
Optional steps to test your answer:

Print the first five names in longest_names.
"""



from csv import reader
dq_unisex_names_csv = open('dq_unisex_names.csv')
read_file = reader(dq_unisex_names_csv)
unisex_names_csv_data = list(read_file)

longest_names = []
for row in unisex_names_csv_data[1:]:
    name = row[0]
    if len(name) > 10:
        longest_names.append(name)
        
print(longest_names[:5])