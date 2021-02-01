print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício: 3 - FOR e LISTAS")
print(("*"*42))

#3) Pedir ao usuário que introduza 5 números. Guardar em uma lista. Mostrar a lista.2ªforma de resolver. Utilize um FOR

lista = []
for elementos in range(5):
    lista.append(int(input('Informe um número: ')))
print(lista)
