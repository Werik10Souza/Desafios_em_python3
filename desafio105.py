
#*Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber várias notas de alunos e vai retornar um DICIONÁRIO com os sequintes informações:

#* - QUANTIDADE DE NOTAS.
#* - A MAIOR NOTA.
#* - A MENOR NOTA.
#* - A MÉDIA DA TURMA
#* - A SITUAÇÃO(OPCIONAL)

#*Adicione também os "docstrings" de função.

def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['média'] = f'{sum(n)/len(n):.2f}'

    if sit:
        if r['média'] >= str(7):
            r['Situação'] = 'BOA'
        elif r['média'] >= str(5):
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r

#?PROGRMA PRINCIPAL
resposta = notas(5.5, 2.5, 8.5, sit=True)
print(resposta)
