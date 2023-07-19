
#*Faca um programa que leia NOME E PESO de VÁRIAS PESSOAS. Guardando tudo em uma LISTA. No final, mostre:

#?A)QUANTAS pessoas foram cadastradas.

#?B)Uma listagem com as pessoas mais PESADAS.

#?C)Uma listagem com as pessoas mais LEVES.


pessoas = []
dados = []

resposta = 'N'

contador = 0

pesada = 0
leve = 0

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
    if resposta == 'N':
        break
print('\n',pessoas)
print('\nPessoas cadastradas: {}'.format(contador))
for pessoa in pessoas:
    if pessoa[1] >= 100:
        print('ºpesado: {}'.format(pessoa[0]))
    else:
        if pessoa[1] <= 65:
            print('ºleve: {}'.format(pessoa[0]))
