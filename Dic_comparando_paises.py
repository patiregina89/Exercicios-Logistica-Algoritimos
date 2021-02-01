
print()
#Criar dicionário
dic_Paises = {'Brasil': 211049519,
              'França': 65129731,
              'Portugal': 10226178,
              'México': 10226178,
              'Uruguai': 3461731}

#utilizar os métodos do dicionário
print('********************** 1 - Método **********************')
print(dic_Paises)
print(dic_Paises.keys())
print(dic_Paises.values())
print('A população extimada do Brasil é: ', dic_Paises.get('Brasil'))
print()
print()

#percorrer todos os elementos do meu dicionário
print('***** 2 - Percorrer todos os elemnetos do dicionário *****')
for k, v in dic_Paises.items():
    print(k, '-->', v)
print()
print()

#usando outras funções
print('******************** 3 - Outras Funções ********************')
print('----- 3.1 - Len (contar número de chaves do dicionário -----')
print('Total de chaves: ', len(dic_Paises))
print()
print('---------- 3.2 - Min e Max (maior e menor chave) ----------')
print('Menor chaves: ', min(dic_Paises), '(ordem alfabética)')
print('Maior chaves: ', max(dic_Paises), '(ordem alfabética)')
print()
print()

#combinar dicionários
dic_Novos_Paises = {'Belize': 390351,
                   'Tanzânia': 58005461}
print('**************** 4 - Atualizando dicionários ****************')
dic_Paises.update(dic_Novos_Paises)
print('Dicionário Atualizado', dic_Paises)
print()
print()

#limpeza do dicionário
print('**************** 5 - Destruindo dicionário ****************')
dic_Paises.clear()
print(dic_Paises)