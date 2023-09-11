from digitInput import intInput

a,b = [intInput(f'Digite o {n+1}º número:\n>>>') for n in range(2)]

if (a==b):
    print(f'Os números {a} e {b} são iguais!')
else:
    print(f'O menor número é {a if a < b else b}')