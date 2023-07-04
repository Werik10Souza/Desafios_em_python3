
#*Crie um programa que tenha uma tupla única com 'nomes de produtos' e seus respectivos preços, na sequência.

#*No final, mostre uma listagem de preços, organizando os dados em forma 'tabular'.

lista_de_compras = ('Queijo ',7.20,
                    'Batata Doce ',5.00,
                    'Arroz ',6.25,
                    'Feijão ',4.78,
                    'Carne ',50.00,
                    'Farinha ',2.82,
                    'Manteiga ',4.58,
                    'Lata de sardinha ',3.12)

print('='*60)
print('                     LISTA DE COMPRAS')
print('='*60)

for posicao in range(0, len(lista_de_compras)):
    if posicao % 2 == 0:
        print('{:.<30}'.format(lista_de_compras[posicao]), end='')
    else:
        print('R${:.>4.2f}'.format(lista_de_compras[posicao]))
print('='*60)
