'''
frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha'
frase = 'Alô, o tatu tá aí? – Não, o tatu não tá. Mas a mulher do tatu tando, é o mesmo que o tatu tá.'
print(frase)
frase = frase.lower()
print(frase)
acentos = {
    'àáãâ' : 'a',
    'éê' : 'e',
    'í' : 'i',
    'óõô' : 'o',
    'úü' : 'u',
    ',.!?:;-' : ''
}
for key in acentos.keys():
    for char in key:
        frase = frase.replace(char,acentos[key])
print(frase)
frase = frase.split(" ")
print(frase)
palavras = {}
for palavra in frase:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
    print(palavras)
'''


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


def comprar():
    local = pega_indice('Qual pizza você quer comprar?')
    quantidade = int(input('Quantidade: '))
    for key in pizzaria.keys():
        if key == "Estoque":
            if pizzaria[key][local] <= quantidade:
                print('A qauntidade é menor do que a pedida')
            else:
                pizzaria[key][local] -= quantidade
            
    return
    
    

pizzaria = {
    'Sabor' : ['Frango Catupiry','4 Queijos','Peperoni','Calabresa','Napoletana'],
    'Preço' : [50,70,60,55,65],
    'Origem' : ['Brasil','Minas Gerais','Itália','Rio Grande do sul','Nápoli'],
    'Ingredientes' : [6,12,8,6,12],
    'Avaliação' : [7,10,9,8,9],
    'Estoque' : [2,3,5,6,7]
}
#De as opções de pizza para o cliente
print(pizzaria['Sabor'])

#pergunte se o cliente quer comprar
comprar()

#se ele quiser, subtraia do estoque a qtd que ele escolheu
#se não houver disponibilidade, peça desculpas e apresente outras opções
#se houver, calcule o valor e adicione ao valor total
#Peça informações sobre o endereço
cria_indices()
opcoes = ["Cadastrar","Remover","Atualizar","Ler","Sair"]
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
