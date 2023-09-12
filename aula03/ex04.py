from digitInput import intInput

day = intInput('Digite o número do dia da semana:\n>>>')

match day:
    case 1:
        name = 'Domingo'
    case 2:
        name = 'Segunda'
    case 3:
        name = 'Terça'
    case 4:
        name = 'Quarta'
    case 5:
        name = 'Quinta'
    case 6:
        name = 'Sexta'
    case 7:
        name = 'Sábado'
    case _:
        name = 'Error'

if name == 'Error':
    print('Você digitou um número inválido')
else:
    print(f'O dia da semana é {name}')