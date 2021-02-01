Lista = [8, 9, 15, 20, 48]
procurado = int(input("Digite  um número a pesquisar: "))
for elementos in Lista:
    if elementos == procurado:
        print("Elemento encontrado!")
        break
    else:
        print("Elemento não encontrado!")