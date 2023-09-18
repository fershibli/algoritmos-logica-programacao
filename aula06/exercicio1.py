number = int(input('Digite um número INTEIRO:\>>>'))
print(f'O número {number} {"é" if number%3==0 and number%5==0 else "não é"} divisível por 3 e por 5 ao mesmo tempo.')