print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:01")
print(("*"*42))

#1. Faça um Programa que peça dois números e imprima o maior deles.

num1=int(input("Digite primeiro número: "))
num2=int(input("Digite segundo número: "))

if num1>num2:
    print("O maior número é:",num1)
elif num2>num1:
    print("O maior número é:",num2)