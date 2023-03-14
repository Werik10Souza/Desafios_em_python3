from  datetime import date
ano_atual = date.today().year

ano_de_nascimento = 0
idade = 0
maior = 0
menor = 0

for ano_de_nascimento in range(0, 7):
   ano_de_nascimento = int(input('\n\033[0mInsira a sua data de nascimento: '))
   idade = ano_atual - ano_de_nascimento
   if idade >= 18:
      maior += 1
   elif idade < 18:
      menor += 1
print('Pessoas que atingiram a maioridade\033[32m{}'.format(maior))
print('Pessoas que atingiram a maioridade\033[31m{}'.format(menor))
