import menu
import arquivo
from time import sleep

arq = "Pessoas.txt"
if not arquivo.arquivoExiste(arq):
    arquivo.arquivoCriar(arq)

while True:
    menu.menu()
    x = menu.escolha('\033[;1mSua opção: \033[0;0m')
    if x == 1:
        sleep(0.5)
        menu.cabeçalho('Opção 1')
        arquivo.arquivoLer(arq)
    elif x == 2:
        sleep(0.5)
        menu.cabeçalho('Opção 2')
        nome = str(input('Nome: ')).capitalize().strip()
        idade = menu.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif x == 3:
        sleep(0.5)
        menu.cabeçalho(' < SISTEMA ENCERRADO > ')
        sleep(1)
        break
    else:
        print('\033[1;31mOpção inválida!\033[0;0m')
    sleep(1.5)