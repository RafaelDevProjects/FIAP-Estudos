#While : enquanto certa coisa for veradadeira


# senha com while.
senha = '1234'
senha_usuario = input('Diga sua senha: ')
repetições = 0

while senha != senha_usuario and repetições < 3:
    print(f'Tente novamente....\nTentativa {repetições + 1}')
    senha_usuario = input('Diga sua senha: ')
    repetições += 1
if senha_usuario == senha:
    print('Acesso permitido')
else:
    print('Acesso Bloquado')

