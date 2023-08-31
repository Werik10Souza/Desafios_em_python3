
#*Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como PARÂMETRO o ANO DE NASCIMENTO de uma pessoa retornanda um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIA nas eleições.

from datetime import date
9ii


data = date.today()
ano = data.year
ano_nasc = int(input('Em qual ano você nasceu?: '))
ano_atual = ano - ano_nasc

print(f'Com {ano_atual} anos: ')
