
#*Crie um pequeno sistema modularizadi que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

#*O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todos as pessoas cadastradas.

from menu import leiaOpcoes

#*Programa Principal
while True:
    escolha = leiaOpcoes('\033[0;35mSua Opção:\033[m ')
    if escolha == 1:
        print('\033[0;32mLista dos nomes e idade...\033[m')
    elif escolha == 2:
        print('\033[0;32mCadastrar Pessoas Novas Aqui...\033[m')
    elif escolha == 3:
        break
print('\033[0;38mFim do programa...\033[m')
    