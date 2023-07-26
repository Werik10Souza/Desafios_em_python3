
#*Faca um programa que leia NOME E PESO de VÁRIAS PESSOAS. Guardando tudo em uma LISTA. No final, mostre:

#?A)QUANTAS pessoas foram cadastradas.

#?B)Uma listagem com as pessoas mais PESADAS.

#?C)Uma listagem com as pessoas mais LEVES.


pessoas = []
dados = []

resposta = 'N'

contador = 0

pesada = [] 

leve = []

while True:
    nome = str(input('\nDigite o seu nome: '))
    peso = float(input('Digite o seu peso: '))
    contador = contador + 1
    resposta = str(input('\nQuer continuar[S/N]?: ').upper().strip() [0])
    if nome not in dados:
        dados.append(nome)
    if peso not in dados:
        dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    if peso >= 100:
        pesada.append(nome)
        pesada.append(peso)
    if peso <= 60:
        leve.append(nome)
        leve.append(peso)
    
    if resposta == 'N':
        break

print('\n',pessoas)
print('\nPessoas cadastradas: {} \n'.format(contador))
print('\n','='*40)
print('PESSOAS PESADAS')
print('='*40)
print(pesada)
print('\n', '='*40)
print('PESSOAS LEVES')
print('='*40)
print(leve)
