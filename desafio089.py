
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
 