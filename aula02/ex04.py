salario = float(input('Entre com salário:\n>>>'))
porcentagem = float(input('Entre com o percentual(%) de aumento:\n>>>').replace('%', ''))/100
novo_salario = salario * (1+porcentagem)
print(f'Novo Salário: {novo_salario:36.3f}')