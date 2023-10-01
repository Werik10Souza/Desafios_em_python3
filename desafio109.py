
#*Modifique as funções que foram criadas no 'desafio107' para que elas aceitem um "um parâmetro" a mais, informando se o valor retornado por elas vai ser ou não formatado pela função 'moeda()', desenvolvida no 'desafio 108'.

import ex109

valor = float(input('Digite o preço: R$'))

valor_metade = ex109.metade(valor, False)
valor_dobro = ex109.dobro(valor, False)
valor_aumentado = ex109.aumentar(valor, 10, True)
valor_reduzido = ex109.diminuir(valor, 13, True)

print(f'A metade de {ex109.moeda(valor)} é {valor_metade}')
print(f'O dobro de {ex109.moeda(valor)} é {valor_dobro}')
print(f'Aumentando 10%, temos {ex109.moeda(valor)} é {valor_aumentado}')
print(f'Reduzindo 13%, temos {ex109.moeda(valor)} é {valor_reduzido}')
