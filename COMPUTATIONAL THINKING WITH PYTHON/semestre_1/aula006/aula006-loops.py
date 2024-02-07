
#validação de usuario e senha usando while
'''print('-=-=-=-=Validadação de usuário e senha=-=-=-=-')

usuario = 'rafael'
senha = '1234'

nome = input('Digite seu usuário: ')
senhap = input('Digite sua senha: ')
tentativas = 1
while tentativas < 3 and (usuario != nome or senha != senhap):   #parenteses por prioridade
    print(f'Você tem {3-tentativas} tentativas')
    nome = input('Digite seu usuário: ')
    senhap = input('Digite sua senha:')
    tentativas += 1
if usuario == nome and senha == senhap:
    print('Acesso Permitido')
else:
    print('Acesso Negado')'''




'''print(f'{"-="*5}Tabuada{"=-"*5}')

tabuada = int(input('Qual tabuada você quer? '))
mult = 1

while mult <= 10:
    print(f'|{tabuada}| X {mult} = \033[0;41;0m{tabuada*mult}\033[m')
    mult += 1

print(f'{"-="*10}')
'''

print(f'{"-="*5}\033[0;31m Media e Soma de 10 numeros \033[m{"=-"*5}')
rep = 0
media = 0
soma = 0
while rep < 10:
    num = int(input(f'Digite o numero {rep}: '))
    soma += num

    rep += 1
media = soma / 10
print(f'{"-="*10}')
print(F'sua media:\033[0;31m{media}\033[m')
print(f'sua soma: \033[0;31m{soma}\033[m')
print(f'{"-="*10}')


