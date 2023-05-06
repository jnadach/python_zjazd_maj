# Napisz program konsolowy który:
#
# Podczas uruchomienia wczyta dane z pliku ingredients.csv i zachowa je w wybranej przez siebie strukturze danych
#
# Po uruchomieniu w konsoli wyświetli menu z 4 możliwościami
#
# 1 – Dodanie nowego składnika
#
# 2 – Wyświetlenie wszystkich składników
#
# 3 – Wyświetlenie składnika po nazwie (like)
#
# 0 – Zakończenie programu

import csv

class Ingredients:

    def __init__(self, name, calories, protein, fat, carbs, fiber, ingredient_type):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.ingredient_type = ingredient_type

    def __str__(self):
        return "----------------------------\n" \
               + f"Name: {self.name}\n" \
               + f"Calories: {self.calories}\n" \
               + f"Protein: {self.protein}\n" \
               + f"Fat: {self.fat}\n" \
               + f"Carbs: {self.carbs}\n" \
               + f"Fiber: {self.fiber}\n" \
               + f"Type: {self.ingredient_type}\n" \
               + "----------------------------"

filename = "ingredients.csv"
ingredients_instances_dict = {}


with open(filename, encoding='utf-8', newline='') as ingredients:
    reader = csv.DictReader(ingredients, delimiter=';')
    for row in reader:
        ingredients_instance = Ingredients(row['NAME'],
                                           row['CALORIES'],
                                           row['PROTEIN'],
                                           row['FAT'],
                                           row['CARBS'],
                                           row['FIBER'],
                                           row['TYPE'])
        ingredients_instances_dict[row['NAME']] = ingredients_instance


def add_ingredients(name, calories, protein, fat, carbs, fiber, ingredient_type):
    pass

def find_all():
    return ingredients.copy()

def find_by_name_like(name: str):
    copy = find_all()
    return (lambda ingridient: name.casefold() in ingredients.name.casefold(), copy)

input("Witamy w programie Ingridients. Dostępne opcje:",
        "1 – Dodanie nowego składnika",
        "2 – Wyświetlenie wszystkich składników")
#
# 2 – Wyświetlenie wszystkich składników
#
# 3 – Wyświetlenie składnika po nazwie (like)
#
# 0 – Zakończenie programu")


