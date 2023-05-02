
#* Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma P.A, mostrando os 10 primeiros termos da progressão usando o estrutura WHILE.

'''
#!USANDO FOR(DESAFIO 051):
enesimo_termo = 0
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for primeiro_termo in range(enesimo_termo + 1, 11): 
    enesimo_termo = primeiro_termo + (10 - 1) * razao
    print(enesimo_termo)
'''

an = 0
contador = 0
primeiro_termo = 0
razao = 0

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
an = primeiro_termo + (10 - 1) * razao

while contador <= 10:
    an = primeiro_termo + (10 - 1) * razao
    contador = contador + 1
    print(an + contador)
print('FIM!')