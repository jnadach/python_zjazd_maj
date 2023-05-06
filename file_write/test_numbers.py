test_numbers = 'numbers.txt'

with open(test_numbers, 'w', encoding='utf-8') as number_file:
    for i in range(10):
        # number_file.write(str(i))
        print(i, "bla bla bla", file=test_numbers)

