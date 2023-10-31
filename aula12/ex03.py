dicionario = {}

for n in range(5):
    sobrenome = input(f"Sobrenome {n+1}: ")
    idade = int(input(f"Idade {n+1}: "))
    dicionario[sobrenome] = idade

media_idades = sum(dicionario.values())/len(dicionario)
print(media_idades)

maior_que_media = {}
for sobrenome, idade in dicionario.items():
    if sobrenome >= media_idades:
        maior_que_media[sobrenome] = media_idades

print(maior_que_media)
