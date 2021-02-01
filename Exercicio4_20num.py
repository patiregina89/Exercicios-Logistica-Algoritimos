print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício 4 - 20 números inteiros")
print(("*"*42))

'''
4. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

numeros = 1
listavetor = []
vpar = []
vimpar = []

while numeros <= 20:
    lista = int(input('Informe um número: '))
    numeros += 1
    listavetor.append(lista)
    if lista%2 == 0:
        vpar.append(lista)
    else:
        vimpar.append(lista)
print('Os números digitados são: ', listavetor)
print('Os números pares digitados são: ', vpar)
print('Os númeos ímpares digitados são: ', vimpar)