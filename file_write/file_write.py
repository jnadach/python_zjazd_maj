animals_array = [
    "Kot - Ssak",
    "Pies - Ssak",
    "Wąż - Gad",
    "Dziobak - Ssak",
    "Sowa - Ptak",
    "Komodo - Gad",
    "Szerszeń - Owad",
    "Tarantula - Gad",
    "Żaba - Płaz",
    "Miś - Ssak",
    "Koń - Ssak",
    "Pszczoła - Owad" 
    "Kukułka - Ptak",
    "Mucha - Owad",
]

animals_file_name = 'animals.txt'

with open(animals_file_name, 'w', encoding='utf-8') as animals:
    for animal in animals_array:
        animals.write(animal)


