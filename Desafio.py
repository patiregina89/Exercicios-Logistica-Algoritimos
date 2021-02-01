'''Faça uma função para calcular o pagamento.Essa função receberá dois parâmetros qtd_hora e valor_hora, que representam respectivamente
a quantidade de hora a serem calculadas e o valor da hora. Esses valores deverão ser convertidos para o tipo float, pois serão recebidos como
string por meio da instrução input.
Na função deve se calcular o salário com a seguinte regra:
Se hora <=40
    salário = horas*taxa
senão:
    horas_excedidas = horas-40
    salario = 40*taxa+(horas_excedidas*taxa)'''

#definição da função
def calcular_pagamento(qtd_hora, valor_hora):
    qtd_hora = float(input(str_horas))
    valor_hora = float(input(str_taxa))
    if qtd_hora <= 40:
        salario = qtd_hora*valor_hora
    else:
        horas_excedidas = qtd_hora-40
        salario = 40*valor_hora + (horas_excedidas*valor_hora)
    return (salario)

#programa principal
str_horas = input('Digite as horas trabalhadas: ')
str_taxa = input('Digite a taxa: ')
#chamada da função
total_salario = calcular_pagamento(str_horas, str_taxa)
print('O valor de seus rendimentos é R$: ', total_salario)