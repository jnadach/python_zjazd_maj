import csv
filename = 'country_info.txt'

our_dialect = csv.excel
our_dialect.delimiter = '|'


countries = {}
with open(filename, encoding='utf-8', newline='') as user_file:
    reader = csv.DictReader(user_file, dialect=our_dialect)

    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

while True:
    selected_country = input("Podaj kraj lub kod: ")

    if selected_country == '0':
        break

    result = countries.get(selected_country.casefold())
    if result:
        print(f"Stolica: {result['Capital']}", f"Strefa czasowa: {result['TimeZone']}",
              f"Kod kierunkowy: {result['IAC']}", f"Waluta: {result['Currency']}", sep='\n\t')
    else:
        print(f"Nie ma takiego klucza jak {selected_country}")

