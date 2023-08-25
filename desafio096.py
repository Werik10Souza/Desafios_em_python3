
#*Faça um programa que tenha uma FUNÇÃO chamada AREA(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a ÁREA DO TERRENO.

def area(largura, comprimento):
    print('-'*30)
    largura = float(input('LARGURA(m): '))
    comprimento = float(input('COMPRIMENTO(m): '))
    tamanho = largura * comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {tamanho}m².')
    print('\n')

print('\n')
print('CONTROLE DE TERRENO')
area('largura', 'comprimento')

