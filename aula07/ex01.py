leituras = int(input("Quantas idades você quer que eu leia?\n>>>"))
if leituras < 1:
    raise Exception("O número de leituras não pode ser negativo.")

soma = 0
for i in range(1, leituras+1):
    n = int(input(f"Entre com o {i}a. idade:\n>>>"))
    soma += n

media = soma / i

print(f"A média das {i} idades é {media:5.2f}")