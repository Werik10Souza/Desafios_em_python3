
#*Crie um módulo chamado "moeda.py" que tenha as funções incorporadas 'aumentar(), diminuir(), dobro(), e metade().'

#*Faça também um programa que 'importe' esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Digite o preço: '))

print(f'Aumentando em 10% é {moeda.aumentar(valor, 10)}')
print(f'Diminuindo em 10%  é {moeda.diminuir(valor, 10)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
