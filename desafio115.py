
#*Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

#*O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todos as pessoas cadastradas.

from menu import * 
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)


#*Programa Principal
while True:
    escolha = leiaOpcoes('\033[0;35mSua Opção:\033[m ')
    if escolha == 1:
        #? Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif escolha == 2:
        #? Opção de cadastrar uma nova pessoa.
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 3:
        #? Opção de sair do sistema
        print('\033[0;35m-\033[m'*40)
        print('\033[0;35m    Saindo do programa... Até logo!\033[m')
        print('\033[0;35m-\033[m'*40)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
    