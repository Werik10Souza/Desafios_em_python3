
#*Adapte o código do "desafio 107", criando uma função adicional chamada 'moeda()' que consiga mostrar os valores como um valor monetário formatado.

import ex108    

valor = float(input('Digite o preço: R$'))

print(f'A metade \033[0;35m{ex108.moeda(valor)}\033[m é \033[0;32m{ex108.moeda(ex108.metade(valor))}\033[m')
print(f'O dobro de \033[0;35m{ex108.moeda(valor)}\033[m é \033[0;32m{ex108.moeda(ex108.dobro(valor))}\033[m')
print(f'Aumentando 10% de \033[0;35m{ex108.moeda(valor)}\033[m é \033[0;32m{ex108.moeda(ex108.aumentar(valor, 10))}\033[m')
