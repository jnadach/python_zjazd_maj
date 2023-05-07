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

class Ingredient:

    def __init__(self, name, calories, protein, fat, carbs, fiber, ingredient_type):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.ingredient_type = ingredient_type

    def __str__(self):
        return str(self.__dict__)
        # return "----------------------------\n" \
        #        + f"Name: {self.name}\n" \
        #        + f"Calories: {self.calories}\n" \
        #        + f"Protein: {self.protein}\n" \
        #        + f"Fat: {self.fat}\n" \
        #        + f"Carbs: {self.carbs}\n" \
        #        + f"Fiber: {self.fiber}\n" \
        #        + f"Type: {self.ingredient_type}\n" \
        #        + "----------------------------"


# example = Ingredient("Bagietki francuskie",283,8.70,1.70,59.2,2,"BREAD")
# print(example)




