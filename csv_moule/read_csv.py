import csv

filename = 'username.csv'

with open(filename, encoding='utf-8', newline='') as csv_file:
    # Sniffer
    #read() -calosc jako string, read_line() - jedna linia, read_lines() - calosc jako lista
    sample = csv_file.read()
    file_dialect = csv.Sniffer().sniff(sample)
    #Wracamy na poczatek pliku
    csv_file.seek(0)
    csv_file.readline().strip('\n').split(file_dialect.delimiter)
    #Reader jest juz na lini drugiej
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC, dialect=file_dialect)
    for row in reader:
        print(row)

print(file_dialect.delimiter)
print(file_dialect.escapechar)
print(repr(file_dialect.lineterminator))
