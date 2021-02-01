print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:05")
print(("*"*42))

#5. Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1=float(input("Digite sua nota da N1: "))
n2=float(input("Digite sua nota da N2: "))
media=(n1+n2)/2
if media == 10:
    print("Aprovado com Distinção")
elif media < 7:
    print("Reprovado")
elif media >= 7:
    print("Aprovado")