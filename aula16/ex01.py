def patosCoelhos(cabecas, pes):
    coelhos = (pes - (2*cabecas))/2
    patos = (-pes + (4*cabecas))/2

    return (patos, coelhos)


cabecas = int(input('Digite o numero de cabeças:\n>>>'))
pes = int(input('Digite o numero de pés:\n>>>'))
total = patosCoelhos(cabecas, pes)
print(f'Total de patos: {int(total[0])}')
print(f'Total de coelhos: {int(total[1])}')
