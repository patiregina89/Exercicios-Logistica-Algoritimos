print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício 3 - Média notas")
print(("*"*42))

#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota:' ))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
lista = [nota1, nota2, nota3, nota4]
print('A suas notas foram:{}, e a sua média final é {:.2f}'.format(lista, media))