print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:08")
print(("*"*42))

# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
valor3 = float(input("Informe o terceiro valor: "))

menor = valor1
if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3
print("O produto mais barato é o R$ %4.2f" % menor)
