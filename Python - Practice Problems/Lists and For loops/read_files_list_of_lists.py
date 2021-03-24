from csv import reader
open_file = open('dq_unisex_names.csv', 'r')
read_file = csv.reader(open_file)
dq_unisex_names_csv = list(read_file)

print(dq_unisex_names_csv[:5])
headers = dq_unisex_names_csv[0]
rows = dq_unisex_names_csv[1:]
for row in rows:
    print(row[1])
    #pega todas as linhas que possuem o indice 1