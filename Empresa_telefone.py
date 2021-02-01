#Calcular a conta telefonica empresa tcau.
#-200 = 0,20 por minuto
# 200 a 400 = 0,18 por minuto
# +400  = 0,15 por minuto

minutos=int(input("Digite quantos minutos você utilizou neste mês:"))

if minutos<200:
    preco=0.20
else:
    if minutos<400:
        preco=0.18
    else:
        preco=0.15
valor_pago=minutos*preco
print("Você gastará este mês: R$ %6.2f" %valor_pago )