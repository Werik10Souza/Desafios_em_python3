
#*Crie um módulo chamado "moeda.py" que tenha as funções incorporadas 'aumentar(), diminuir(), dobro(), e metade().'

#*Faça também um programa que 'importe' esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Digite o valor: '))

print(f'O valor aumentando -> {moeda.aumentar(valor)}')
print(f'O valor diminuindo ->  {moeda.diminuir(valor)}')
print(f'O valor dobrando -> {moeda.dobro(valor)}')
print(f'O valor dividindo -> {moeda.metade(valor)}')
