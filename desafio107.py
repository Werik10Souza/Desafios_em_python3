
#*Crie um módulo chamado "moeda.py" que tenha as funções incorporadas 'aumentar(), diminuir(), dobro(), e metade().'

#*Faça também um programa que 'importe' esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Digite o preço: '))

print(f'Aumentando em 10% é \033[0;32m{moeda.aumentar(valor, 10)}\033[m')
print(f'Diminuindo em 10%  é \033[0;32m{moeda.diminuir(valor, 10)}\033[m')
print(f'O dobro de \033[0;35m{valor}\033[m é \033[0;32m{moeda.dobro(valor)}\033[m')
print(f'A metade de \033[0;35m{valor}\033[m é \033[0;32m{moeda.metade(valor)}\033[m')
