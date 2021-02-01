print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício: 2 - FOR e LISTAS")
print(("*"*42))

'''2) Pedir ao usuário que introduza 5 números.
Guardar em uma lista. Mostrar a lista.
1ªforma de resolver sem FOR, só com métodos das listas '''

num = 1
lista = []
while num <= 5:
    info = int(input('Informe um número: '))
    lista.append(info)
    num += 1
print(lista)
