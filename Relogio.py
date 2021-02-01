print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:Relógio")
print(("*"*42))


'''
Criar um relógio :
agora são 1h 1min
agora são 1h 2min
agora são 1h 3min
'''
hora = 0
minuto = 0
while hora < 24:
    minuto = 0
    while minuto <= 59:
        print("Agora são %dh %dmin"%(hora, minuto))
        minuto = minuto + 1
    hora = hora + 1
