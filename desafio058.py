
#* Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até 
#* acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

numero = 1
sorteado = 0
while numero != sorteado:
    numero = int(input('\nDigite um  valor entre 0 á 10: '))
    sorteado = random.randint(0, 10)
    if numero != sorteado:
        print('\nVocê ERROU, o número sorteado pelo computador foi {}'.format(sorteado))
if numero == sorteado:
    print('\nPARABENS!!! Você VENCEU. O número sorteado pelo computador foi {}'.format(sorteado))
else:
    print('\nVocê PERDEU! Tente novamente. O número sorteado pelo computador foi {}'.format(sorteado))
