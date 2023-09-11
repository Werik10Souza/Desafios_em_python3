
#*Faça um MINI-SISTEMA que utilize o 'Interactive Help' do python. O usuário digitar a palavra  o 'comando' e o MANUAL vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se ENCERRAR 

#*OBS: USE CORES

def mini_sistema(mensagem):
    global interativo
    msn01 = 'SISTEMA DE AJUDAR PYTHON'
    msn02 = 'ATÉ LOGO!'
    comando = 'fim'
    while True:
        print('~'*len(msn01))
        print('SISTEMA DE AJUDAR PYTHON')
        print('~'*len(msn01))
        interativo = str(input(mensagem).strip())

        if interativo == comando:
            print('~'*len(msn02))
            print('ATÉ LOGO!!!')
            print('~'*len(msn02))
            break
        else:
            help(interativo)

#?PROGRAMA PRINCIPAL
mini_sistema('\nFunção ou Biblioteca >  ')
