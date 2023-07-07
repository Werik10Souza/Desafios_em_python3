
#*Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastra-os em uma lista.
#*Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os VALORES ÚNICOS
#*digitados, em ORDEM CRESCENTE.

valores = []
resposta = 'N'

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print('\nValor duplicado! Não será possivel adicionar...')
    resposta = str(input('\nQuer continuar[S/N]: ').upper().strip() [0])
    if resposta == 'N':
        break
print('\n', sorted(valores))
print('\nFIM!')
