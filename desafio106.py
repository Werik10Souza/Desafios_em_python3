
#*Faça um MINI-SISTEMA que utilize o 'Interactive Help' do python. O usuário digitar a palavra  o 'comando' e o MANUAL vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se ENCERRAR 

#*OBS: USE CORES

def mini_sistema(p= ' '):
    global interativo
    mensagem = 'SISTEMA DE AJUDAR PYTHON'
    while True:
        print('~'*len(mensagem))
        print('SISTEMA DE AJUDAR PYTHON')
        print('~'*len(mensagem))
        interativo = str(input('\nFunção ou Biblioteca >  ').strip())
        help(interativo)

#?PROGRAMA PRINCIPAL
mini_sistema()
