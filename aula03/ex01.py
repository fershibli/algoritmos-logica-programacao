name = input('Digite o seu nome:\n>>>')
while not(age := input("Entre com a sua idade:\n>>>")).isdigit():
    print(f'Sua idade precisa ser um número! \"{age}\" não é um número!')
age = int(age)

print(f'{name} tem {age} anos');

if age >=60:
    print('Você já pode pagar 1/2 no cinema!')
else:
    print('Parabéns, você ainda é jovem!')

print('Acabou o programa.')