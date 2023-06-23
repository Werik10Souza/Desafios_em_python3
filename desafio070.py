
#*Crie um programa que leia o NOME e o PREÇO de várias produtos. O programa devevá perguntar SE o usuário vai continuar. No final, mostre:

#?A) Qual é o TOTAL GASTO na compra?
#?B) Quantos produtos custam MAIS de R$1000.
#?C) Qual é o NOME do produto mais BARATO.

nome = ''
preco = 0
continuar = 'N'
gasto = 0
produtos_mais_mil = 0
barato = 0

while True:
    nome = str(input('Digite o nome do produto, AQUI!: ').upper().strip())
    preco = float(input('Digite o preço do produto, AQUI!: '))
    gasto = gasto + preco
    if(preco > 1000):
        produtos_mais_mil = produtos_mais_mil + 1
    barato = nome 
    print('='*40,'\n')
    continuar = str(input('\nQuer continuar?[S/N]: ').upper().strip() [0])
    if(continuar == 'N'):
        break
print('\nTOTAL GASTO: R${}'.format(gasto))
print('\nPRODUTOS QUE CUSTAM MAIS DE MIL REAIS: {}'.format(produtos_mais_mil))
print('\nPRODUTO MAIS BARATO: {}'.format(barato))