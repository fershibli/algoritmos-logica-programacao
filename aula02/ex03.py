# ano_nascimento = int(input('Que ano você nasceu?\n>>>'))
# ano_atual = int(input('Em que ano estamos?\n>>>'))
#
# diff_anos = ano_atual - ano_nascimento
#
# print('Este ano você terá...')
# print(f'em Anos: {diff_anos}')
# print(f'em Meses: {diff_anos*12}')
# print(f'em Dias: {diff_anos*365}')
# print(f'em Semanas: {diff_anos*53}')

from datetime import date

date_hoje = date.today()
date_nascimento = date(*[int(i) for i in input('Digite sua data de nascimento no formato yyyy/mm/dd:\n>>>').split('/')])

date_delta = date_hoje - date_nascimento

print('Sua idade é...')
print(f'Em anos: {int(date_delta.days//365.25)}')
print(f'Em meses: {(int(date_delta.days//365.25)*12)+date_hoje.month-date_nascimento.month}')
print(f'Em semanas: {int(date_delta.days//7)}')
print(f'Em dias: {date_delta.days}')