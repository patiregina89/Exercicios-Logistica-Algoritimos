print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício 5 - Operçòes matemáticas")
print(("*"*42))

#5. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
num5 = int(input('Digite o quinto númerp: '))
soma = [num1 + num2 + num3 + num4 + num5]
multiplicacao = [num1 * num2 * num3 * num4 * num5]
numeros = [num1, num2, num3, num4, num5]
print('A soma dos números digitados é {}, e o resultado da sua multiplicação é: {}'.format(soma, multiplicacao))
print('Os números digitados foram: ', numeros)