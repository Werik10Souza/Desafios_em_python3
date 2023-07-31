
#*Faça um programa que leia NOME e MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO.No final, mostre o conteúdo da estrutura na tela.
nome = str(input('Digite o nome: '))
media = float(input('Digite a média: '))

aluno = {'nome': ' ', 'media': ' '}
aluno['nome'] = nome
aluno['media'] = media

print('\n', aluno, '\n')

print(f'\nNome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')

if media >= 5.0:
    print('Situação é igual a APROVADO(a)')
else:
    print('Situação é igual a REPROVADO(a)') 
