dicionario = {}

for n in range(5):
    sobrenome = input(f"Sobrenome {n+1}: ")
    idade = int(input(f"Idade {n+1}: "))
    dicionario[sobrenome] = idade

valores = list(dicionario.values())
maior_idade = sorted(valores)[-1]
maior_sobrenome = list(dicionario.keys())[valores.index(maior_idade)]

print(maior_sobrenome, maior_idade)
