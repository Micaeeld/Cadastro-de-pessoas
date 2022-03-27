import menu

def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt', encoding='utf-8') # 'rt'(read text): tentar abrir por txt
        arq.close() #Fecha arquivo
    except FileNotFoundError: #FileNotFoundError: Aquivo não encontrado
        return False
    else:
        return True


def arquivoCriar(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def arquivoLer(nome):
    try:
        arq = open(nome)
    except:
        print('Erro ao ler o arquivo!')
    else:
        menu.cabeçalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos')
    finally:
        arq.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at') #'at'(append, txt): colocar coisas dentro do arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na escrita do arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arq.close()
