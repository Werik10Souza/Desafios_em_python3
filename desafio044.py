preco = float(input('Preço das compras R$: '))
print('''FORMAS DE PAGAMENTOS
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?: '))
if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.2)
    total_de_parcelas = int(input('Em quantas parcelas?: '))
    parcela = total / total_de_parcelas
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(total_de_parcelas, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} no final R${}'.format(preco, total))
