# Função simples e sem parâmetros
def ola_mundo():
    print('Olá Mundo!')

# Função com um parâmetros
def ola_pessoa(nome):
    print('Olá '+ nome + ', como vai você?' )

# Função com dois parâmetros
def ola_pessoa_email(nome, email):
    print('Olá ' + nome + ', seu e-mail é: ' + email)



# programa principal
ola_mundo()

ola_pessoa('Patricia')

meu_nome = 'Patricia'
meu_email = 'patriciarr89@gmail.com'
ola_pessoa_email(meu_nome, meu_email)