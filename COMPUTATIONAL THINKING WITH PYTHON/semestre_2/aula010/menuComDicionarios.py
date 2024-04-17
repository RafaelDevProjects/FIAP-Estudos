import requests


def forca_opcao(msg,opcoes,msg_erro=None):
    escolha = input(msg)
    while escolha not in opcoes:
        print("Opção inválida!")
        if msg_erro:
            print(msg_erro)
        escolha = input(msg)
    return escolha


def pega_indice(msg):
    opcoes = pizzaria["Sabor"]
    pizza = forca_opcao(msg,opcoes,'\n'.join(opcoes))
    local = indices[pizza]
    return local


def cadastrar():
    for key in pizzaria.keys():
        info = input(f"Diga o/a novo/a {key}: ")
        pizzaria[key].append(info)
    return


def remover():
    local = pega_indice("Qual pizza vc deseja remover? ")
    for key in pizzaria.keys():
        pizzaria[key].pop(local)
    return


def atualizar():
    local = pega_indice("Qual pizza vc deseja atualizar? ")
    for key in pizzaria.keys():
        info = input(f"Diga o novo {key}")
        pizzaria[key][local] = info
    return


def ler():
    local = pega_indice("Qual pizza vc deseja ver? ")
    for key in pizzaria.keys():
        print(pizzaria[key][local])
    return


def cria_indices():
    pizzas = pizzaria["Sabor"]
    global indices
    indices = {pizzas[i] : i for i in range(len(pizzas))}
    return


def mostra_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            mostra_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")


def verificaNumero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        print("Deve ser um numero")
        numero = input(msg)
    return int(numero)


def revisa_conta(qtd, local, escolha):
    valor = qtd*pizzaria['Preço'][local]
    carrinho["Valor"] += valor
    if escolha not in pizzaria.keys():
        carrinho["Pizzas"][escolha] = qtd
    else:
        carrinho["Pizzas"][escolha] += qtd
    pizzaria["Estoque"][local] -= qtd


def comprar():
    sabores = pizzaria['Sabor']
    sabores_msg = '\n'.join(sabores)
    print("Seja bem vindo a pizzaria Agnello!!")
    while True:
        escolha = forca_opcao(f"Essas são as nossas opções: \n{sabores_msg}\n ->", sabores)
        local = indices[escolha]
        qtd = verificaNumero("Quantas unidades deseja comprar:\n -> ")
        if pizzaria['Estoque'][local] < qtd:
            qtd_min = pizzaria['Estoque'][local]
            compra_minima = forca_opcao(f"Infelizmente não temos essa quantidade disponivel",
                  f"somente {qtd_min}. Vai querer (s/n)\n->", ["s","n"])
            if compra_minima == "s":
                revisa_conta(qtd, local, escolha)
            else:
                continue
        else:
             revisa_conta(qtd, local, escolha)
        continuar = forca_opcao("Voce quer ver mais pizzas? (sim/não)", ["sim", "não"])
        if continuar == "não":
            print("Obrigado por comprar :)")
            mostra_dicionario(carrinho)
            return


def cadastrar_endereco(api = True):
    if api:
        while True:
            cep = input("Diga seu CEP: ")
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            while not len(cep) == 8 or cep.isnumeric() or 'erro' in response.json() or response.status_code != 200:
                print("Cep invalido")
                cep = input("Diga seu CEP: ")
                response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            mostra_dicionario(response.json())
            resposta = forca_opcao("Informações corretas? (s/n)", ['s','n'])
            if resposta == 's':
                break
        endereco = response.json()
        numero = verificaNumero("Diga o nuemro da sua casa")
        endereco['N'] = numero
        carrinho["Endereco"] = endereco
        return
    for key in carrinho['Endereco'].keys():
        info = input(f"Diga o {key}: ")
        carrinho['Endereco'][key] = info
    return



pizzaria = {
    'Sabor' : ['Frango Catupiry','4 Queijos','Peperoni','Calabresa','Napoletana'],
    'Preço' : [50,70,60,55,65],
    'Origem' : ['Brasil','Minas Gerais','Itália','Rio Grande do sul','Nápoli'],
    'Ingredientes' : [6,12,8,6,12],
    'Avaliação' : [7,10,9,8,9],
    'Estoque' : [2,3,5,6,7]
}


cria_indices()
opcoes = ["Cadastrar","Remover","Atualizar","Ler","Sair"]

carrinho = {
    'Endereco': {
        'Rua': '',
        "N": '',
        "Cep": ""
    },
    "Valor" : 0,
    "Pizzas" : {

    }
}


resposta = input("Voce é cliente ou funcionario? ")
if resposta == "funcionario":
    while True:
        opcao = forca_opcao("O que deseja fazer hoje? ",opcoes,'\n'.join(opcoes))
        if opcao == opcoes[0]:
            cadastrar()
            cria_indices()
        elif opcao == opcoes[1]:
            remover()
            cria_indices()
        elif opcao == opcoes[2]:
            atualizar()
        elif opcao == opcoes[3]:
            ler()
        else:
            print("Tchau")
            break
else:
    cadastrar_endereco()
    comprar()



url = "https://imdb188.p.rapidapi.com/api/v1/searchIMDB"

querystring = {"query":"inception"}

headers = {
	"X-RapidAPI-Key": "{id}",
	"X-RapidAPI-Host": "imdb188.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
mostra_dicionario(response.json())



url = "https://waze.p.rapidapi.com/alerts-and-jams"

querystring = {"bottom_left":"40.66615391742187,-74.13732147216798","top_right":"40.772787404902594,-73.76818084716798","max_alerts":"20","max_jams":"20"}

headers = {
	"X-RapidAPI-Key": "{id}",
	"X-RapidAPI-Host": "waze.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

mostra_dicionario(response.json())
