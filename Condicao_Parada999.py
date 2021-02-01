print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:Condição parada 999")
print(("*"*42))


'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor de 999 (flag), que é a condição de parada. No
final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag - 999)
'''

soma = 0
num_digitado = 0
while True:
    num = int(input("Digite um número ou 999 para sair: "))
    if num == 999:
        break
    soma = soma + num
    num_digitado = num_digitado + 1
print("A soma dos números digitados é: ",soma)
print("A quantidade de números digitados é: ", num_digitado)

'''
Criei uma variável soma atribuida o valor de 0, pois pedem a soma dos valores digitados.
Também criei a variável num_digitado com valor atribuido de 0 pois, o exercicio quer saber quantos números foram digitados.
Usei o while true pois significa que enquanto a condição for verdadeira, o sistema irá se repetir. Então:
enquanto o número digitado for diferente de 999, ele vai repetir o pedido de digitar novo número.
Assim que o usuário digitar 999, o programa se encerra e ele informa a soma dos números digitados e a quantidade de números digitados.
'''