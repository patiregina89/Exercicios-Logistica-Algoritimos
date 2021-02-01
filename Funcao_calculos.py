import sys

'''ARQUIVOS NÃO EXECUTAVEIS. sao apenas funções pré-determinadas.'''
def somar():
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    print('Somar: ', x + y)

def subtrair():
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    print('Subtrair: ', x - y)

def multiplicar():
    x = float(input('Digite o priemiro número: '))
    y = float(input('Digite o segundo número: '))
    print('Multiplicar: ', x * y)

def dividir():
    x = float(input('Digite o primeiro número: '))
    y = float(input('Digite o segundo número: '))
    print('Dividir: ', x / y)

def sair():
    print('Saindo do sistema!')
    sys.exit(0)