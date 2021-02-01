lista = [7, -1, 4, 3, 12, 8, 0]
fim = 7 #marca a quantidade de elementos da lista
while fim > 1: #verifica se a variável fim>1, tem pelo menos 2 elementos na lista.
    trocou = False #a variável indica que nao realizamos nenhuma troca de elementos na lista.
    x = 0 #o x é usado como índice para percorer a lista, iniciando em 0.
    while x < (fim-1): #isso faz com que a condição de saida (x) seja nterior ao último elemento.
        if lista[x] > lista[x + 1]:
            trocou = True
            var_temporaria = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = var_temporaria
        x = x + 1
    if not trocou:
        break
    fim = fim - 1

for elemento in lista:
    print(elemento)