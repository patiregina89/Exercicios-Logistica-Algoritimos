soma = 0
while True:
    valor = int(input("Digite o número para somar e 0 para sair: "))
    if valor == 0:
        break
    soma = soma + valor
print("A soma dos valores é: ", soma)