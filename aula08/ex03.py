lista=[]
for i in range(10):
    lista.append(input(f'entre o {i+1}º valor:'))

for i in lista[::-1]:
    print(i, end=',')