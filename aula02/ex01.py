from math import pow, sqrt

print('Insira os pontos dos catetos para obter a hipotenusa')
x1, x2 = [int(x) for x in input('x1,x2>>>').replace(' ', '').split(',')]
y1, y2 = [int(y) for y in input('y1,y2>>>').replace(' ', '').split(',')]

dx, dy = x2 - x1, y2 - y1

distancia = sqrt(pow(dx, 2) + pow(dy, 2))

print(f'A hipotenusa é igual a: {distancia}')