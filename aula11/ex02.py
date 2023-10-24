pessoas = {}
for i in range(10):
    sobrenome = input(f'Digite o sobrenome da {1+i}º pessoa:')
    idade = int(input(f'Digite a idade da {1+i}º pessoa:'))
    pessoas[sobrenome] = idade

pessoas = dict(sorted(pessoas.items(), key = lambda item: item[1], reverse=True))

print(pessoas)