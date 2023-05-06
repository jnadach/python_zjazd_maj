# lord_of_the_rings = open('C:/Users/nadachow/PycharmProjects/pythonProject/file_read/lor.txt', 'r')

# try:
#     lord_of_the_rings = open('lor.txt', 'r')
#
#     for line in lord_of_the_rings:
#         print(line)
# except Exception:
#     print("Exception!")
# finally:
#     print("ZAWSZE SIE WYKONA")
#     #zamykanie zawsze w finally
#     lord_of_the_rings.close()

lord_of_the_rings = open('lor.txt', 'r', encoding='utf-8')
for line in lord_of_the_rings:
    print(line.rstrip())

lord_of_the_rings.close()

text = "'Trzy Pierścienie dla królów elfów pod otwartym niebem,\n"
print(len(text))