# zapisywanie do pliku
F = open('zwierzeta.txt', 'w')

# sprawdzic jaki jest tryb domyslny
for param in ['name', 'mode', 'closed']:
    print(getattr(F, param))

F.write('ZWIERZĘTA\n')
animals = ['słoń', 'lew', 'pingwin']

F.writelines([animal + '\n' for animal in animals])


# readlines
F = open('zwierzeta.txt', 'r')
for el in F.readlines():
    print(el)






