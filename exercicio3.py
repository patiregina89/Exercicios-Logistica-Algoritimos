print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:03")
print(("*"*42))

#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo=str(input("Informe a inicial do seu sexo: "))
if sexo=="f":
    print("Feminino")
elif sexo=="F":
    print("Feminino")
elif sexo=="m":
    print("Masculino")
elif sexo=="M":
    print("Masculino")
else:
    print("Sexo inválido")