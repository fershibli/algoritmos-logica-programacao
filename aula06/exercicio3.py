from math import floor
print('Insira as dimensões do aposento a ser pintado, conforme pedido.')
# dados iniciais
walls_width = float(input('Largura (em número):\n>>>'))
walls_length = float(input('Comprimento (em número):\n>>>'))
walls_height = 2.8
door_area = 0.8*2.1 

# cálculo das paredes
width_area = walls_width*walls_height
length_area = walls_length*walls_height

# dobro de paredes (cômodo quadrado), menos porta
total_area = ((width_area+length_area)*2)-door_area
print(f'A área total a ser pintada é de {total_area:.2f}m².')

# a cada 3 metros quadrados = 1 L, basta dividir todos os metros quadrados por 3
tint_liters = total_area/3
print(f'Para pintar essa área são necessários {tint_liters:.2f}L de tinta.')

# a cada lata = 18L 
tin_quantity = floor(tint_liters/18)
# o que sobrar da divisão da lata, dividir por 3.6
gallon_quantity = floor((tint_liters%18)/3.6)

print('Você precisará ter:')
print(f'> {tin_quantity} latas de tinta;')
print(f'> {gallon_quantity} galões de tinta;')
print(f'> e ainda faltarão {tint_liters-(tin_quantity*18)-(gallon_quantity*3.6):.2f}L de tinta para completar a pintura.')