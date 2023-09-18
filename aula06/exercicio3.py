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
print(f'A área total a ser pintada é de {total_area}m².')

# a cada 3 metros quadrados = 1 L, basta dividir todos os metros quadrados por 3
tint_liters = total_area/3
print(f'Para pintar essa área são necessários {tint_liters}L de tinta.')

# a cada lata = 18L 
tin_quantity = floor(tint_liters/18)
# o que sobrar da divisão da lata, dividir por 3.6
gallon_quantity = floor((tint_liters%18)/3.6)

print(f'Você precisará de:\n-> {tin_quantity} latas de tinta\n-> {gallon_quantity} galões de tinta\n-> Faltarão {tint_liters-gallon_quantity-tin_quantity}L para completar.')