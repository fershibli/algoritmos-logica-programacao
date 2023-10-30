dicionario = {}

for n in range(5):
    sobrenome = input(f"Sobrenome {n+1}: ")
    idade = int(input(f"Idade {n+1}: "))
    dicionario[sobrenome] = idade

maior_idade = -1
maior_sobrenome = ""

for key_sobrenome, value_idade in dicionario.items():
    if maior_idade == -1 or maior_idade < value_idade:
        maior_idade = value_idade
        maior_sobrenome = key_sobrenome

print(maior_idade, maior_sobrenome)
