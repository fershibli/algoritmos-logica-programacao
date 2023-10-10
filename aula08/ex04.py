lista=[]
for i in range(10):
    lista.append(int(input(f'entre o {i+1}º valor:')))

maior = sorted(lista, reverse=True)[0]
pos = lista.index(maior)

print(f'O maior número está na posição {pos} e seu valor é {lista[pos]}')
print(lista)