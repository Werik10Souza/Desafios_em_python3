
#*Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber várias notas de alunos e vai retornar um DICIONÁRIO com os sequintes informações:

#* - QUANTIDADE DE NOTAS.
#* - A MAIOR NOTA.
#* - A MENOR NOTA.
#* - A MÉDIA DA TURMA
#* - A SITUAÇÃO(OPCIONAL)

#*Adicione também os "docstrings" de função.

def nota():
    lista = []
    contador = 0
    soma = 0
    pergunta = 'N'
    while True:
        nota = float(input('Digite a nota do aluno: '))
        soma = soma + nota
        lista.append(nota)
        alunos = {'Total': lista, 'Maior': lista, 'Menor': lista, 'Média': lista}

        contador = contador + 1

        media = soma/contador

        alunos['Total'] = contador
        alunos['Maior'] = max(lista)
        alunos['Menor'] = min(lista)
        alunos['Média'] = f'{media:.2f}'

        mostra = f'TOTAL: {alunos["Total"]}, MAIOR: {alunos["Maior"]}, MENOR: {alunos["Menor"]}, MÉDIA: {alunos["Média"]}'
        
        pergunta = str(input('Quer continuar[S/N]?: ').upper().strip() [0])
        if pergunta == 'N':
            break
        
    print(mostra)

#?PROGRAMA PRINNCIPAL        
print(nota())
