lista_1 = [input(f'lista_1, elemento_{i}: ') for i in range(1, 11)]
print('----')
lista_2 = [input(f'lista_2, elemento_{i}: ') for i in range(1, 11)]
print('----')
set_1 = set(lista_1)
set_2 = set(lista_2)

print(set_1.union(set_2))
