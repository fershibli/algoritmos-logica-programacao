soma = 0
for i in range(1, 11):
    n = int(input(f"Entre com o {i}a. idade:\n>>>"))
    soma += n
media = soma / i
print(f"A média das {i} idades é {media:5.2f}")