print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:07")
print(("*"*42))

#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

num1=int(input("Informe o primeiro número: "))
num2=int(input("Informe o segundo número: "))
num3=int(input("Informe o terceiro número: "))
maior=num1
menor=num1

if num2>maior:
    maior=num2
if num3>maior:
    maior=num3

print("O número %d " "é o maior número informado"%maior)

if num2<menor:
    menor=num2
elif num3<menor:
    menor=num3
print("O número %d " "é o menor número informado"%menor)