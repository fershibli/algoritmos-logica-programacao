from random import randint

rodadas=1000

placar = [0, 0, 0, 0, 0, 0]
for i in range(rodadas):
    lado = randint(1,6)
    placar[lado-1] += 1
    print(placar, lado)

ocorrencias = sorted(placar, reverse=True)[0]
face = placar.index(ocorrencias)+1

print('\nEstatísticas:')
for i in range(len(placar)):
    print(f'{i+1} : {placar[i]/rodadas*100:.2f}%')

print(f'Das {rodadas} rodadas, a face {face} foi a que mais apareceu, com {ocorrencias} ocorrencias')