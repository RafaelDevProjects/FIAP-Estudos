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



inicio = int(input('Digite um numero para começar: '))
fim = int(input('Digite um numero para finalizar: '))

if fim > inicio:
    while inicio <= fim:
        if inicio % 2 == 0:
            print(f'O numero {inicio} é par')

        else:
            print(f'O numero {inicio} é impar')
        inicio += 1
else:
    print('Tente novamente...')




