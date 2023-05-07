import loader
from program_strategy import AddNewIngredient, ListIngredients, ListIngredientsByNameLIke, TerminateProgram

if __name__ == '__main__':
    loader.load_initial_data()
    strategy_map = {
        "1": AddNewIngredient(),
        "2": ListIngredients(),
        "3": ListIngredientsByNameLIke(),
        "0": TerminateProgram()
    }

    while True:
        print("Witamy w programie Ingridients. Dostępne opcje:",
              "1 – Dodanie nowego składnika",
              "2 – Wyświetlenie wszystkich składników",
              "3 – Wyświetlenie składnika po nazwie (like)",
              "0 – Zakończenie programu",
              sep='\n')
        decision = input("> ")

        if decision not in strategy_map:
            print("Proszę wybrać poprawną wartość")
        else:
            strategy_map[decision].execute()
