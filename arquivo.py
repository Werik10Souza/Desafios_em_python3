def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        print('-'*20)
        print('PESSOAS CADASTRADAS'.center(20))
        print('-'*20)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError: 
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[0;31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
            try:
                a.write(f'{nome};{idade}\n')
            except:
                print('\033[0;31mHouve um ERRO de escrever os dados!\033[m')
            else:
                print(f'Novo registro de {nome} adicionado.')
                a.close()
