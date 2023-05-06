import csv

medals_table = [
    {'athlete': 'CASLAVSKA, Vera', 'gold': 7, 'silver': 4, 'bronze': 0, 'country': 'Czechoslovakia', 'total': ''},
    {'athlete': 'FISCHER, Birgit', 'gold': 8, 'silver': 4, 'bronze': 0, 'country': 'East Germany', 'total': ''},
    {'athlete': 'NURMI, Paavo', 'gold': 9, 'silver': 3, 'bronze': 0, 'country': 'Finland', 'total': ''},
    {'athlete': 'VAN ALMSICK, Franziska', 'gold': 0, 'silver': 4, 'bronze': 6, 'country': 'Germany', 'total': ''},
    {'athlete': 'GEREVICH, Aladar', 'gold': 7, 'silver': 1, 'bronze': 2, 'country': 'Hungary', 'total': ''},
    {'athlete': 'KELETI, Agnes', 'gold': 5, 'silver': 3, 'bronze': 2, 'country': 'Hungary', 'total': ''},
    {'athlete': 'MANGIAROTTI, Edoardo', 'gold': 6, 'silver': 5, 'bronze': 2, 'country': 'Italy', 'total': ''},
    {'athlete': 'GAUDINI, Giulio', 'gold': 3, 'silver': 4, 'bronze': 2, 'country': 'Italy', 'total': ''},
    {'athlete': 'ONO, Takashi', 'gold': 5, 'silver': 4, 'bronze': 4, 'country': 'Japan', 'total': ''},
    {'athlete': 'KATO, Sawao', 'gold': 8, 'silver': 3, 'bronze': 1, 'country': 'Japan', 'total': ''},
    {'athlete': 'NAKAYAMA, Akinori', 'gold': 6, 'silver': 2, 'bronze': 2, 'country': 'Japan', 'total': ''},
    {'athlete': 'COMANECI, Nadia', 'gold': 5, 'silver': 3, 'bronze': 1, 'country': 'Romania', 'total': ''},
    {'athlete': 'NEMOV, Alexei', 'gold': 4, 'silver': 2, 'bronze': 6, 'country': 'Russia', 'total': ''},
    {'athlete': 'LATYNINA, Larisa', 'gold': 9, 'silver': 5, 'bronze': 4, 'country': 'Soviet Union', 'total': ''},
    {'athlete': 'ANDRIANOV, Nikolay', 'gold': 7, 'silver': 5, 'bronze': 3, 'country': 'Soviet Union', 'total': ''},
    {'athlete': 'SHAKHLIN, Boris', 'gold': 7, 'silver': 4, 'bronze': 2, 'country': 'Soviet Union', 'total': ''},
    {'athlete': 'CHUKARIN, Viktor Ivanovich', 'gold': 7, 'silver': 3, 'bronze': 1, 'country': 'Soviet Union',
     'total': ''},
    {'athlete': 'ASTAKHOVA, Polina', 'gold': 5, 'silver': 2, 'bronze': 3, 'country': 'Soviet Union', 'total': ''},
    {'athlete': 'DITYATIN, Aleksandr', 'gold': 3, 'silver': 6, 'bronze': 1, 'country': 'Soviet Union', 'total': ''},
    {'athlete': 'SCHERBO, Vitaly', 'gold': 6, 'silver': 0, 'bronze': 4, 'country': 'Unified team', 'total': ''},
    {'athlete': 'PHELPS, Michael', 'gold': 14, 'silver': 0, 'bronze': 2, 'country': 'United States', 'total': ''},
    {'athlete': 'THOMPSON, Jenny', 'gold': 8, 'silver': 3, 'bronze': 1, 'country': 'United States', 'total': ''},
    {'athlete': 'TORRES, Dara', 'gold': 4, 'silver': 4, 'bronze': 4, 'country': 'United States', 'total': ''},
    {'athlete': 'BIONDI, Matthew', 'gold': 8, 'silver': 2, 'bronze': 1, 'country': 'United States', 'total': ''},
    {'athlete': 'COUGHLIN, Natalie', 'gold': 3, 'silver': 4, 'bronze': 4, 'country': 'United States', 'total': ''},
    {'athlete': 'OSBURN, Carl Townsend', 'gold': 5, 'silver': 4, 'bronze': 2, 'country': 'United States', 'total': ''},
    {'athlete': 'SPITZ, Mark', 'gold': 9, 'silver': 1, 'bronze': 1, 'country': 'United States', 'total': ''},
    {'athlete': 'HALL, Gary Jr.', 'gold': 5, 'silver': 3, 'bronze': 2, 'country': 'United States', 'total': ''},
    {'athlete': 'LEWIS, Carl', 'gold': 9, 'silver': 1, 'bronze': 0, 'country': 'United States', 'total': ''},
]

column_names = ['athlete', 'gold', 'silver', 'bronze', 'country', 'total']
filename = 'athlete_medal_write.csv'



def sort_key(d: dict) -> str:
    return d['athlete']

print(sort_key(medals_table))

# print(sorted(medals_table, key=sort_key))




with open(filename, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=column_names, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(sorted(medals_table, key=sort_key))

# Opcja druga
# for row in medals_table:
# 	writer.writerow(row)
