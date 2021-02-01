#escreva um programa que pergunte  a velocidade do carro d eum usuãrio.
#caso ultrapasse 80km/h, exiba uma msg dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa cobrado, cobrando R$ 5.00 por Km acima de 80Km/h.

velocidade_registrada= int(input("Informe a velocidade do carro:"))
valor_ultrapassado=velocidade_registrada-80
valor_multa=valor_ultrapassado*5

if velocidade_registrada>80:
    print("Você ultrapassou o limite de velocidade em %d." %valor_ultrapassado, "Sua multa é de R$ %d." %valor_multa)