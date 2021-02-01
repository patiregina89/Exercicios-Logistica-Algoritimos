"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa perguntar se o usuário
quer ou não continuar. No final mostre:a) Quantas pessoas
tem mais de 18 anos. b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.

"""
homens = mais_18 = mulheres_20 =0
while True:
    idade = int(input('Idade: '))
    sexo = alternativa = ' '
    while sexo not in 'FM':
        sexo = (input('Sexo[F/M]: ')).strip().upper()[0]
    if idade > 18:
        mais_18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres_20 += 1
    while alternativa not in 'SN':
        """
        O strip () retorna uma cópia de uma string com certos 
        caracteres retirados do início e no final da string e [0] 
        pego só a primeira letra
        """
        alternativa = (input('Quer continuar [S/N]? ')).strip().upper()[0]
    if alternativa == 'N':
        break
print(f'Pessoas com mais de 18 anos: {mais_18}')
print(f'Número de homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres_20}')