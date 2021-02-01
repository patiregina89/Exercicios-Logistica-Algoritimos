print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:Questionário")
print(("*"*42))

'''
3) Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa perguntar se o usuário quer ou não continuar. No final
mostre:
a. a) Quantas pessoas tem mais de 18 anos.
b. b) Quantos homens foram cadastrados.
c. c) Quantas mulheres tem menos de 20 anos.
'''

qtd_pessoa_18 = 0
qtd_homem = 0
qtd_mulher = 0

while True:
    idade = int(input("Informe a idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Informe o sexo [M/F]: "))
    if idade >= 18:
        qtd_pessoa_18 += 1
    if sexo == 'M':
        qtd_homem += 1
    if sexo == 'F' and idade < 20:
        qtd_mulher += 1

    resp = ' '
    while resp  not in 'SN':
        resp = str(input("Quer continuar [S/N]? "))
    if resp == 'N':
        break
print("Finalizado!")
print("A quantidade de pessoas, maior de 18 anos, cadastradas é: %d"%qtd_pessoa_18)
print("A quantidde de homens cadatsrados é: %d"%qtd_homem)
print("A quantidade de mulheres com menos de 20 anos cadastrdas é: %d"%qtd_mulher)

'''
Criei 3 variávei atribuidas o valor de 0 pois utilizamos para cacular as quantidades, conforme as perguntas.
Criei também a variável resp para saber se o usuário quer continuar respondendo ou finalizar o programa 'break'.
Usei o while true, pois quero que ele repita a perguntas várias vezes até que o usuáro decida parar com o comando 'N'
Pedi que informassem a idade; Pedi que informassem o sexo, porém fiz uma condição para que aceitem apenas M ou F, caso contrário, ele repete a pergunta.
Feito isso, utilizei o if para responder as perguntas e utilizei a formula para somar à variável existente+1.
'''