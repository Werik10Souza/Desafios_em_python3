
#*Dentro do pacote 'utilidadesCeV' que criamos no 'desafio 111, temos um "módulo" chamado "leiaDinheiro()" que seja capaz de funcionar como a função "input()", mas com uma 'validção de dados' para aceitar apenas valores que sejam "monetários".

from utilidadescev import moeda

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 20, 12)
