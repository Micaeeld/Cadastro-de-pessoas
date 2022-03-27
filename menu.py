from time import sleep

def linha():
    print('\033[;1m'+'-'*40+'\033[0;0m')


def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')



def cabeçalho(txt):
    linha()
    print('\033[;1m'+txt.center(40)+'\033[0;0m')
    linha()


def menu():
    cabeçalho('MENU PRINCIPAL')
    print('\033[1;34m1\033[0;0m - \033[1;96mPessoas cadastradas\033[0;0m')
    print('\033[1;34m2\033[0;0m - \033[1;96mCadastrar nova pessoa\033[0;0m')
    print('\033[1;34m3\033[0;0m - \033[1;96mSair do sistema\033[0;0m')
    linha()


def escolha(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[1;31mOpção inválida! Digite um número inteiro.\033[0;0m')
        else:
            return n
