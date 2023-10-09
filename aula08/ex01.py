lista = list(range(10, 18))

for index, item in enumerate(lista):
    print(item, end="," if index != len(lista)-1 else '')