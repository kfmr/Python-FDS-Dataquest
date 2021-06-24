## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
#loop nas linhas do dataset
for row in moma:
    # atribuir a linha 3 a variavel birthdate
    birth_date = row[3]
    #se não for vazio, transformar a string em int
    if birth_date != "":
        birth_date = int(birth_date)
    # atribuir o valor de birthdate inteiros a linha 3 do dataset
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##

# Create an empty list, ages, to store the artist age data.
ages = []
#Create an empty list final_ages, to store the final age data.
final_ages = []
#Use a loop to iterate over the rows in moma.
for row in moma:
    #assign the artwork year (at index 6) to date
    date = row[6]
    #assign the artist birtyear index 3
    birth = row[3] 
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)
            

for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
    
print(final_ages)

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen
# declarar uma lista vazia
decades = []
# iterar sob todos os valores da lista final_ages
for age in final_ages:
    # se o valor for unknown, a decada recebe o age
    if age == "Unknown":
        decade = age
    else:
        # transformar o numero em string
        decade = str(age)
        # retirar o ultimo digito com slice da string com [:-1]
        decade = decade[:-1] + "0s"
    # a cada iteração adiciona o valor da variavel decades de acordo com as validações do if-else
    decades.append(decade)
    
print(decades)
        

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for decade in decades:
    if decade in decade_frequency:
        decade_frequency[decade]+=1
    else:
        decade_frequency[decade] = 1
        
print(decade_frequency)

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
print(f"{artist}'s birth year is {birth_year}")

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
# iterar sob o dataset listas de listas
for row in moma:
    artist = row[1]
    if artist in artist_freq:
        artist_freq[artist]+=1
    else:
        artist_freq[artist] = 1
        
        
print(artist_freq)

## 7. Creating an Artist Summary Function ##

def artist_sumary(artist_name):
    # localiza o valor pelo nome do artista na chave:valor do dicionário
    num_artwork = artist_freq[artist_name]
    return f"There are {num_artwork} artworks by {artist_name} in the data set"



print(artist_sumary("Henri Matisse"))


## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
# template = "The population of {} is {:,.2f} million"
for row in pop_millions:
    country = row[0]
    pop_num = row[1]
    print(f"The population of {country} is {pop_num:,.2f} million")

## 9. Challenge: Summarizing Artwork Gender Data ##

#Create a frequency table for the values in the Gender (row index 5) column.
#Loop over each key-value pair in the dictionary. Display a line of output in #the format shown above summarizing each pair.

#criar dicionário vazio
gender_freq = {}

# iterar sob o dataset(lista de listas)
for row in moma:
    gender = row[5]
    if gender in gender_freq:
        gender_freq[gender] +=1
    else:
        gender_freq[gender] = 1
        
        
print(gender_freq)
#loop sob a chave(gender) e valor(number)
for gender, number in gender_freq.items():
    # number:,colocar a virgula
    template = f"There are {number:,} artworks by {gender} artists"
    print(template)