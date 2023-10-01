
#*Adapte o código do "desafio 107", criando uma função adicional chamada 'moeda()' que consiga mostrar os valores como um valor monetário formatado.

import ex108    

valor = float(input('Digite o preço: R$'))

print(f'A metade {ex108.moeda(valor)} é {ex108.moeda(ex108.metade(valor))}')
print(f'O dobro de {ex108.moeda(valor)} é {ex108.moeda(ex108.dobro(valor))}')
