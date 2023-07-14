
#*Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que usa PARÊNTESES.Seu aplicativo deverá analisar se
#*a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.

expressao = str(input('Digite a expressão: '))

pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
