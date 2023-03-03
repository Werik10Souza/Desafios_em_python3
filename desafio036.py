casa = float(input('Digite o valor da casa: '))
salario = float(input('Quanto ganhar por mês?: '))
anos = int(input('Em quantos anos você vai pagar: '))

prestacao = casa / (anos * 12)
minimo = salario * 0.3

if prestacao <= minimo:
    print('\nPARABENS!!! O seu emprestimo foi APROVADO.')
elif prestacao > minimo:
    print('\nINFELIZMENTE, o seu emprestimo foi NEGADO.')
    