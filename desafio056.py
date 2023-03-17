#FAÇA O PROGRAMA
soma = 0
maior = 0
contagem_mulheres = 0
media = 0
nome_do_homem_mais_velho = ''

for contador in range(1, 5):
    nome = input('Digite o seu nome: ')
    sexo = input('Homem ou Mulher? [H/M]: ').upper()[0]
    idade = int(input('Digite a sua idade: '))

    soma = soma + idade
    media = soma / contador

    if sexo == 'H' and idade > maior:
        maior = idade
        nome_do_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        contagem_mulheres
print('Media das idades é de {:.2f}'.format(media))
print('Nomw do homem mais velho: {}'.format(nome_do_homem_mais_velho))

if contagem_mulheres == 0:
    print('Não temos mulheres no grupo!!!')
else:
    print('Ao todo temos {} mulheres com menor de 20 anos'.format(contagem_mulheres))
