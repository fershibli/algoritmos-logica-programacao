purchase_value = float(input('Digite o valor da compra em forma de número FLOAT:\n>>>'))
print(f'Sua compra no valor de {purchase_value} receberá o desconto de ', end='')
if purchase_value <= 1000:
    print('10%.')
    purchase_value*=0.9
elif purchase_value <= 5000:
    print('20%.')
    purchase_value*=0.8
else:
    print('30%.')
    purchase_value*=0.7

print(f'O valor final a ser pago, com desconto é de: {purchase_value}.')