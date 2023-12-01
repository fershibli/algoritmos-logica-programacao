def sumDigits(str_number):
    total = 0
    for d in str_number:
        total += int(d)
    return total


def multiplyDigits(str_number):
    total = 1
    for d in str_number:
        total *= int(d)
    return total


entrada = input("Digite um número de vários dígitos:\n>>>")
print(f'A soma dos dígitos de {entrada} é: {sumDigits(entrada)}')
print(f'A multiplicação dos dígitos de {entrada} é: {multiplyDigits(entrada)}')
