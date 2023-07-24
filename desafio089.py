
#*Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA. No final, mostre um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

pessoas = []
nomes_notas = []
pergunta = 'N'


while True:
    nome = str(input('\nDigite o nome: ').upper().strip())
    nomes_notas.append(nome)

    nota_01 = float(input('\nDigite a nota: '))
    nota_02 = float(input('Digite a nota: '))
    nomes_notas.append(nota_01)
    nomes_notas.append(nota_02)
    pessoas.append(nomes_notas[:])
    nomes_notas.clear()
    
    pergunta = str(input('\nQuer continuar ou não[S/N]?: ').upper().strip() [0])

    if pergunta == 'N':
        break


print('\n', pessoas, '\n')
 
print('='*50)
print('LISTA DE NOMES E NOTAS DE ALUNOS')
print('='*50)
print('\nNome: {} Média: {}'.format(pessoas[0][0], (pessoas[0][1]+pessoas[0][2])/2))
print('\nNome: {} Média: {}'.format(pessoas[1][0], (pessoas[1][1]+pessoas[1][2])/2))
print('\nNome: {} Média: {}'.format(pessoas[2][0], (pessoas[2][1]+pessoas[2][2])/2))

pergunta = str(input('\nQuer pesquisa um aluno expressifico?: ').upper().strip() [0])
if pergunta != 'N':
    print('-'*30)
    print('BUSCAR POR ALUNO EXPERSSIFICO...')
    print('-'*30)
    buscar = str(input('Nome do aluno: '))

    #?ANALISAR O CÓDIGO E RESOLVER
     
    if buscar == pessoas[0][0]:
        print(pessoas[0][0])
    else:
        print('ERRO!!!')
