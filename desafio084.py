
#*Faca um programa que leia NOME E PESO de VÁRIAS PESSOAS. Guardando tudo em uma LISTA. No final, mostre:

#?A)QUANTAS pessoas foram cadastradas.

#?B)Uma listagem com as pessoas mais PESADAS.

#?C)Uma listagem com as pessoas mais LEVES.


pessoas = []
dados = []

resposta = 'N'

contador = 0

maior = 0
menor = 0

while True:
    dados.append(str(input('\nDigite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))


    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    contador = contador + 1
    
    resposta = str(input('\nQuer continuar[S/N]?: ').upper().strip() [0])

    if resposta == 'N':
        break

print('\n',pessoas)
print(f'\nPessoas cadastradas: {contador} \n')
print(f'O MAIOR peso foi de {maior}KG.')
print(f'O MENOR peso foi de {menor}KG.')
