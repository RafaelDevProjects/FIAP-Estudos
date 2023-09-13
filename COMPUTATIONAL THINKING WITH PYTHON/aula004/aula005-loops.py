#While : enquanto certa coisa for veradadeira


# senha com while.
senha = '1234'
senha_usuario = input('Diga sua senha: ')
repetições = 1

while senha != senha_usuario and repetições < 3:
    print('Errou')
    print(f'Tentativa {repetições}')
    senha_usuario = input('Diga sua senha: ')

    repetições += 1
if senha_usuario == senha:
    print('Acesso permitido')
else:
    print('Acesso Bloquado')

