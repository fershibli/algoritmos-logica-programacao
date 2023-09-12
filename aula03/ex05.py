from digitInput import floatInput

x, y, z = [floatInput(f'Digite o {n+1}º lado:\n>>>') for n in range(3)]

if x>y+z or y>x+z or z>y+x:
    print(f'Os lados de tamanho {x:.2f}, {y:.2f} e {z:.2f} não formam um triângulo')
elif x==y==z:
    print(f'Os lados de tamanho {x:.2f}, {y:.2f} e {z:.2f} formam um triângulo equilátero')
elif x==y or x==z or y==z:
    print(f'Os lados de tamanho {x:.2f}, {y:.2f} e {z:.2f} formam um triângulo isósceles')
else:
    print(f'Os lados de tamanho {x:.2f}, {y:.2f} e {z:.2f} formam um triângulo escaleno')