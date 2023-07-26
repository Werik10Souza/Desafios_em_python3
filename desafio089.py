
#*[Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA.] No final, [mostre um BOLETIM contendo a MÉDIA de cada um] e [permita que o usuário possa mostrar as notas de cada aluno individualmente.]

pessoas = []
nomes_notas = []

pergunta = 'N'


while True:
    nome = str(input('\nDigite o nome: ').upper().strip())
    nomes_notas.append(nome)

    nota_01 = float(input('\nDigite a nota 1º: '))
    nota_02 = float(input('Digite a nota 2º: '))
    nomes_notas.append(nota_01)
    nomes_notas.append(nota_02)
    pessoas.append(nomes_notas[:])
    nomes_notas.clear()
    
    pergunta = str(input('\nQuer continuar ou não[S/N]?: ').upper().strip() [0])

    if pergunta == 'N':
        break

print('\n','¨'*50)
print(':'*15,'MÉDIA DOS ALUNOS',':'*15)
print('¨'*50)

print('-'*40)
print('   NOME', '                 MEDIA')

print('-'*40)
for posicao, nota in enumerate(pessoas):
    media = (nota[1] + nota[2]) / 2
    print(f'{posicao + 1} º {nota[0]:<20} {media:>5}')
print('-'*40)

while True:
    aluno = int(input('Escolhar aluno e sua nota [999 para finalizar ação]: '))
    if aluno == 999:
        print('FINALIZANDO OPERAÇÃO...')
        print('='*10)
        print('FIM!!!')
        print('='*10)
        break
    if len(pessoas) >= aluno > 0:
        print(len(pessoas), aluno)
        print(f'{pessoas[aluno-1][0]} tirou notas {pessoas[aluno-1][1]}, {pessoas[aluno-1][2]}')
    else:
        print('  \nALUNO NÃO LOCALIZANDO   ')