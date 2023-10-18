print(f"{'-='*5}Boas Vindas{'-='*5}")
nome = input('Qual é o seu nome?')
endereço = input(f'{nome} qual é o seu endereço?')
anoNascimento = input(f'{nome} qual é o seu ano de nascimento? ')
anoAtual = 2023
total = 0
frete = 10
qntVinhoTinto = 0
qntVinhoRose = 0
qntVinhoBranco = 0



while not anoNascimento.isnumeric():
    print(f'{nome} Digite um numero!!')
    anoNascimento = input(f'{nome} qual é o seu ano de nascimento? ')
anoNascimento = int(anoNascimento)
idade = anoAtual - anoNascimento

if idade >= 18:
    while True:
        print(f"{'-='*5}Opções de vinho{'-='*5}\n ROSE R$ 50 \n BRANCO R$ 100 \n TINTO R$ 200")
        print(f"{'-='*10}")


        vinho = input(f'{nome} Escolha uma das opções: ')
        while not (vinho == 'ROSE' or vinho == 'BRANCO' or vinho == 'TINTO'):
            print('Escolha uma opção!')
            vinho = input(f'{nome} Escolha uma das opções: ')

        quantidadeGarrafas = input(f'{nome} Qual é a quantidade de garradas? ')
        while not quantidadeGarrafas.isnumeric():
            print('Escolha um valor valido')
            quantidadeGarrafas = input(f'{nome} Qual é a quantidade de garradas? ')
        quantidadeGarrafas = int(quantidadeGarrafas)


        if vinho == 'BRANCO':
            preco = 50
            total = quantidadeGarrafas * 50
            qntVinhoBranco = quantidadeGarrafas
        elif vinho == 'ROSE':
            total = quantidadeGarrafas * 100
            qntVinhoRose = quantidadeGarrafas
        else:
            total = quantidadeGarrafas * 200
            qntVinhoTinto = quantidadeGarrafas


        continuar = input('Deseja continuar a compra? [S/N]')
        while not (continuar == 'S' or continuar == 'N'):
            continuar = input('[ Digite um valor VALIDO ] Deseja continuar a compra? [S/N]')

        if continuar == 'S':
            pass
        else:
            break

    print(f"{'-='*5}Obrigado pela preferencia{'-='*5}")
    if total > 500:
        print('O total foi maior que R$ 500 você tem Frete GRATIS!!')
    else:
        print(f'A taxa de frete é 10 R$')
        total = total + frete

    print(f'O Endereço de entrega É {endereço}')
    print(f'Total = {total}')
    print(f'Vinho TINTO: {qntVinhoTinto} Unidades')
    print(f'Vinho ROSE: {qntVinhoRose} Unidades')
    print(f'Vinho BRANCO {qntVinhoBranco}')





else:
    print('Não é permitida a venda de bebidas alcoolicas para menores de idade!!!')

