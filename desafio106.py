
#*Faça um MINI-SISTEMA que utilize o 'Interactive Help' do python. O usuário digitar a palavra  o 'comando' e o MANUAL vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se ENCERRAR 

#*OBS: USE CORES

def mini_sistema(mensagem):
    global interativo
    msn = 'SISTEMA DE AJUDAR PYTHON'
    while True:
        print('~'*len(msn))
        print('SISTEMA DE AJUDAR PYTHON')
        print('~'*len(msn))
        interativo = str(input(mensagem).strip())
        help(interativo)

#?PROGRAMA PRINCIPAL
mini_sistema('\nFunção ou Biblioteca >  ')
