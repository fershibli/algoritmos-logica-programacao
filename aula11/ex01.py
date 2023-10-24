l = []
for i in range(10):
    l.append(input(f'Digite o {1+i}º elemento: '))

t = tuple(l)
for i in range(-1, -len(t)-1, -1):
    print(t[i], end=' ')
print('')