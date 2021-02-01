from Funcao_calculos import *

#VARIAVEIS
opcao = 1
#MENU
while opcao:
    print('0 - Sair')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
#RECEBER AS INFORMAÇÕES
    opcao = int(input('Digite a opção desejada: '))
#INFORMAR AS CONDICÕES PARA A ESCOLHA
    if opcao == 1:
        somar()
    if opcao == 2:
        subtrair()
    if opcao == 3:
        multiplicar()
    if opcao == 4:
        dividir()
    if opcao == 0:
        sair()
