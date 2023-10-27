def leiaOpcoes(opcoes):
    print('-'*45)
    print('               MENU PRINCIPAL      ')
    print('-'*45)
    print('1- \033[0;36mVer Pessoas Cadastradas\033[m')
    print('2- \033[0;36mCadastrar Nova Pessoa\033[m')
    print('3- \033[0;36mSair Do Sistema\033[m')
    while True:
        try:
            escolha = int(input('Sua Opção: '))
            if escolha in [1, 2 , 3]:
                return escolha
        except ValueError:
            print('\033[0;31mErro! Escolha a opção 1, 2 ou 3.\033[m')
