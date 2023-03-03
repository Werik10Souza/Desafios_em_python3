import random

numero = int(input('Digite um número entre 0 á 5: '))
sorteado = random.randint(0, 5)
if numero == sorteado:
    print('PARABENS!!! Você VENCEU. O número sorteado pelo computador foi {}'.format(sorteado))
else:
    print('Você PERDEU! Tente novamente. O número sorteado pelo computador foi {}'.format(sorteado))
