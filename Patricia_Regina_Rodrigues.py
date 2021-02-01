'''Implemente um script em Python que leia dados do tipo ID (devendo ser um código (ALFANUMÉRICO – Ex.: A000, ) em uma lista (tamanho máximo
de 100) e depois utilize o método bubble sort (tem que ser uma função - ORDENA) para ordenar os registros na lista. Ao final apresente os
elementos ordenados na tela (tem que ser uma função - IMPRIME)'''

print("*"*12,"FACULDADE CESUSC","*"*12)
print("CURSO: ANÁLISE E DESENV. DE SISTEMAS")
print("Discipl.: Lógica Computacional e Algorítimos")
print("Turma: ADS11")
print("Nome: Patricia Regina Rodrigues")
print("Desafio Bubble Sort")
print(("*"*42))
print()

lista = ['A001', 'B002', 'C003', 'D004', 'E005', 'F006', 'G007', 'H008', 'I009', 'J010',
         'A101', 'B102', 'C103', 'D104', 'E105', 'F106', 'G107', 'H108', 'I109', 'J110',
         'A201', 'B202', 'C203', 'D204', 'E205', 'F206', 'G207', 'H208', 'I209', 'J210',
         'A301', 'B302', 'C303', 'D304', 'E305', 'F306', 'G307', 'H308', 'I309', 'J310',
         'A401', 'B402', 'C403', 'D404', 'E405', 'F406', 'G407', 'H408', 'I409', 'J410',
         'A501', 'B502', 'C503', 'D504', 'E505', 'F506', 'G507', 'H508', 'I509', 'J510',
         'A601', 'B602', 'C603', 'D604', 'E605', 'F606', 'G607', 'H608', 'I609', 'J610',
         'A701', 'B702', 'C703', 'D704', 'E705', 'F706', 'G707', 'H708', 'I709', 'J710',
         'A801', 'B802', 'C803', 'D804', 'E805', 'F806', 'G807', 'H808', 'I809', 'J810',
         'A901', 'B902', 'C903', 'D904', 'E905', 'F906', 'G907', 'H908', 'I909', 'J910']

def imprime(lista_final):
    fim = 100   #quantidade de elementos da lista
    while fim > 1:  #verifica se há mais de 2 elementos e é possível a comparação destes.
        troca = False   #indica que não houve troca de elementos na lista
        x = 0  #índice da lista, começa da posição 0.
        while x < (fim - 1):    #fica condicionado a saída à variavel fim-1, ou seja, último elemento.
            if lista[x] > lista[x + 1]:   #compara se o primeiro elemento for maior que o próximo elemento (x+1)
                troca = True    #se for maior, faz a troca.
                var_temporaria = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = var_temporaria
            x += 1
        if not troca:
            break
        fim -= 1
    return lista_final
print(imprime(lista))
