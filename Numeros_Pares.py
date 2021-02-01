print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:Números pares")
print(("*"*42))

#Programa que imprime a quantidade de números pares de 100 até 200, incluindo-o


num = 100
soma = 0
while num < 200:
    num +=2
    soma = soma + 1
    print(num-2)
print("A quantidade de números pares entre 100 e 200 é de: ", soma)

'''Atribui o valor de 100 a variável "num" pois queremos a quantidade de números pares entre 100 e 200.
Feito isso, criei a variavél soma atribuido a 0, pois o exercício pede a quantidade de números pares.
A "formula" usada foi while (repetição), que faz com que, enquanto a variavel num for menor que 200 - e maior que 100 - ele vai calculando o que se pede.
Em seguida, criei a repetição somando 2, pois queremos apenas os números pares, então a partir do 100, ele soma 2 e guarda, depois mais 2 até chegar em 200.
mandei imprimir todos os números de 100 até 200 e por fim, imprimiu a soma de quantos números pares já entre 100 e 200.
'''

