'''
#PRIMEIRO EXEMPLO
x = 12
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print('Erro: Você dividiu por 0.')'''


'''
#SEGUNDO EXEMPLO
def ler_int(mensagem, mensagem_erro):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print(mensagem_erro)

msg = 'Digite um número inteiro: '
msg_erro = 'Número inválido!'

x = ler_int(msg, msg_erro)
y = ler_int(msg, msg_erro)
print(x+y)'''

#TERCEIRO EXEMPLO
print('Vamos dividir dois números inseridos por você')
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
resultado = int(num1)/int(num2)
print('O resultado é: '+ str(resultado))

# como eu trato a exceção de divisão por zero?
# como eu trato a questão de digitar uma letra ao invés de um número?