soma_massa=0
soma_altura=0
maior_imc=0
menor_imc=0
for i in range(1,6):
    massa = float(input(f'Insira a massa da {i}a pessoa:\n>>>'))
    altura = float(input(f'Insira a altura da {i}a pessoa:\n>>>'))
    soma_massa += massa
    soma_altura += altura

    imc = massa/(altura**2)

    if imc > maior_imc:
        maior_imc = imc
    if menor_imc == 0 or imc < menor_imc:
        menor_imc = imc

    print(f'O imc da {i}a pessoa é {imc:.2f}')

print(f'O peso médio é {soma_massa/5:.2f}')
print(f'A altura média é {soma_altura/5:.2f}')

print(f'O maior IMC é {maior_imc:.2f}')
print(f'O menor IMC é {menor_imc:.2f}')