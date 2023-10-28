print("Seja bem vindo à Vinheria!")
ano = input("Diga seu ano de nascimento : ")
endereco = input("Diga seu endereco : ")
while not ano.isnumeric():
    print("Deve ser um número com 4 caracteres!")
    ano = input("Diga seu ano de nascimento : ")
ano = int(ano)
if 2023 - ano < 18:
    print("Isso é muito feio!!!")
else:
    vinho1 = 'tinto'
    vinho2 = 'suave'
    vinho3 = 'seco'
    preco1 = 30
    preco2 = 40
    preco3 = 50
    qtd1 = 0
    qtd2 = 0
    qtd3 = 0
    valor_total = 0
    while True:
        print(f"Temos as seguintes opcoes: {vinho1} por R${preco1},00,\n"
              f"{vinho2} por R${preco2},00,\n"
              f"{vinho3} por R${preco3},00,")
        opcao = input("Qual voce vai levar ? (sair para encerrar) ")
        while opcao != vinho1 and opcao != vinho2 and opcao != vinho3 and opcao != 'sair':
            print("Deve ser uma opcao cadastrada!")
            opcao = input("Qual voce vai levar ? (sair para encerrar) ")
        if opcao == 'sair':
            if valor_total>500:
                print("Frete Grátis!!!")
            else:
                frete = 50
                print(f"Frete de R${frete},00")
                valor_total += frete

            print(f"Obrigado por comprar aqui. Voce comprou {qtd1} do {vinho1}, "
                  f"{qtd2} do {vinho2} e {qtd3} do {vinho3} totalizando"
                  f" R${valor_total},00 a ser entregue em {endereco}.")
            break
        qtd = input(f"Quantas garrafas do vinho {opcao} você vai levar ? ")
        while not qtd.isnumeric():
            print("Tem que ser um número!")
            qtd = input(f"Quantas garrafas do vinho {opcao} você vai levar ? ")
        qtd = int(qtd)
        if opcao == vinho1:
            valor_total += qtd*preco1
            qtd1 += qtd
        elif opcao == vinho2:
            valor_total += qtd*preco2
            qtd2 += qtd
        elif opcao == vinho3:
            valor_total += qtd*preco3
            qtd3 += qtd
