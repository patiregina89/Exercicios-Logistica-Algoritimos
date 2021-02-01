print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Exercício:Atividade 1 - Hipermercado Tabajara")
print(("*"*42))

'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
Até 5 Kg Acima de 5 Kg
File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos
tipos de carne da promoção, porém não há limites para a quantidade de carne
por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''
preco_total = 0
tipo_carne = str(input("Qual o tipo de carne comprada: alcatra, file ou picanha? "))
qtd_carne = float(input("Informe a quantidade de carne comprada: "))
tipo_pgto = str(input("O pagamento será no cartao ou dinheiro? "))

file1 = qtd_carne*4.90
file2 = qtd_carne*5.80

alcatra1 = qtd_carne*5.90
alcatra2 = qtd_carne*6.80

picanha1 = qtd_carne*6.90
picanha2 = qtd_carne*7.80

if tipo_carne == "file":
    if qtd_carne < 5:
        preco_total = file1
    else:
        preco_total = file2
elif tipo_carne == "alcatra":
    if qtd_carne < 5:
        preco_total = alcatra1
    else:
        preco_total = alcatra2
elif tipo_carne == "picanha":
    if qtd_carne < 5:
        preco_total = picanha1
    else:
        preco_total = picanha2
else:
    print("Favor informar o item comprado.")

if tipo_pgto == "cartao":
    valor_desconto = preco_total*0.05
    print("O valor do desconto foi de: ", valor_desconto)
    print("Forma de pagamento: ", tipo_pgto)
    print("Valor total da compra é R$ ", preco_total-valor_desconto)
elif tipo_pgto == "dinheiro":
    print("Forma de pagamento: ", tipo_pgto)
    print("O valor total é R$ ", preco_total)
else:
    print("Tipo de pagamento não aceito!")

'''
Sobre o script do Hipermercado TABAJARA , resolva o seguinte desafio: O usuário poderá digitar o tipo de carne e o tipo de pagamento da forma como ele quiser. Ex.: File, fILE, file, etc, o mesmo para o tipo de pagamento – Ex.: CARTAO, CarTAO, carTAO, DINHEIRO, dinheiro, ETC.
Como o se script aceitará todas essas formas de entradas? Altere o script 3 acima para que aceite a entrada de dados que o usuário fizer.
Adicione o seu script com uma ou duas linhas de comentários explicando o que você fez para resolver o desafio.
'''