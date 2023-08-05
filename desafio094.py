
#*Crie um programa que leia NOME, SEXO e IDADE de VÁRIOS PESSOAS, guardando os dados de cada pessoa em um DICIONÁRIO
#*e todos os dicionários em uma LISTA. No final, mostre:
#?A) Quantas pessoas foram cadastradas.
#?B) A média de idade do grupo.
#?C) Uma lista com todas as mulheres.
#?D) Uma lista com todas as pessoas com idade acima da média.

contador = 0
soma_idades = 0

lista = []

mulheres_lista = []

acima_media = []

while True:
    nome = str(input('\nNome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ').upper().strip() [0])
        if  sexo in 'MmFf':
            break
        else:
            print('ERRO!!! [M]Masculino ou [F]Feminino?')
    idade = int(input('Idade: '))
    contador = contador + 1
    soma_idades = soma_idades + idade

    dados = {'Nome' : nome,
             'Sexo' : sexo,
             'Idade' : idade}
    
    lista.append(dados.copy())
    
    if sexo == 'F':
        mulheres_lista.append(nome)
    
    while True:
        resposta = str(input('\nQuer continuar [S/N]: ').upper().strip() [0])
        if resposta in 'SN':
            break
        else:
            print('Erro!!! [S]Sim ou [N]Não?')

    if resposta == 'N':
        break

media = soma_idades / contador


print('\n')
print(lista)
print('-='*40)
print(f'A) O grupo tem {contador} pessoas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres_lista}')
print(f'D) Lista das pessoas que estão acima da média:')
print('\n<<ENCERRADO>>')
