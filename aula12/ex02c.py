dicionario = {}

for n in range(5):
    sobrenome = input(f"Sobrenome {n+1}: ")
    idade = int(input(f"Idade {n+1}: "))
    dicionario[sobrenome] = idade

maior_sobrenome = max(dicionario, key=dicionario.get)
maior_idade = dicionario[maior_sobrenome]

print(maior_sobrenome, maior_idade)
