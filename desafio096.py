
#*Faça um programa que tenha uma FUNÇÃO chamada AREA(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a ÁREA DO TERRENO.

def area(largura, comprimento):
    tamanho = largura * comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {tamanho}m².')
    print('\n')

#?PROGRAMA PRINCIPAL
print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)  

