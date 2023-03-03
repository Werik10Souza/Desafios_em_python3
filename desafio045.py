from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('JOGADOR VENCEU!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('JOGADOR PERDEU!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU!')

    elif jogador == 2:
        print('EMPATE!')

    else:
        print('JOGADA INVÁLIDA!')
