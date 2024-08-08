def acha_maior(lista):
    local_maior = 0
    maior = lista[local_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            local_maior = i
    return local_maior


def forca_opcao(msg, opcoes, msg_erro):
    resp = input(msg)
    while resp not in opcoes:
        print(msg_erro)
        resp = input(msg)
    return resp


def acha_menor(lista):
    local_menor = 0
    menor = lista[local_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            local_menor = i
    return local_menor


def cria_indices():
    carro = carros["nomes"]
    global indices
    indices = {carro[i] : i for i in range(len(carro))}
    return


def cadastrar():
    resposta = forca_opcao('Deseja cadastrar um carro? [sim/nao] ', ['sim','nao'], 'erro digite: [sim/nao]')
    if resposta == 'sim':
        for key in carros.keys():
            carro = input(f'Digite o {key}: ')
            carros[key].append(carro)
    else:
        return


# 1
'''saudacoes = {
    'oi' : 'ola',
    'tchau' : 'falou'
}
frase = '/n'.join(saudacoes.keys())
resposta = forca_opcao(f'Digite oi ou tchau: \n{frase}\n', saudacoes.keys(), 'opcao invalida')
print(saudacoes[resposta])'''


# 2
carros = {
 'nomes' : ['celta','up','kombi','uno'],
 'portas' : [4,2,6,2],
 'preço' : [1000,200,300,100],
 'ano de fabricação' : [2014,2018,1970,2005]
}

cria_indices()

#2
'''frase_erro = '\n'.join(carros['nomes'])
escolha = forca_opcao('Qual carro deseja ver?\n ',carros['nomes'], 'opcao invalida' + '\n'.join(carros['nomes'], f'Opção invalida \n {frase_erro}'))
indice = indices[escolha]
for key in carros.keys():
    print(f'{key} = {carros[key][indice]}')'''

# 3
'''maior_preco_index = acha_maior(carros['preço'])
print('Carro com maior preço')
for key in carros.keys():
    print(carros[key][maior_preco_index])'''

#4
'''menor_index = acha_menor(carros['preço'])
print('Carro com menor preço')
for key in carros.keys():
    print(carros[key][menor_index])'''

#5

'''cadastrar()'''

#6
'''def remover():
    resposta2 = forca_opcao('Deseja remover um carro? [sim/nao] ', ['sim','nao'], 'erro digite: [sim/nao]')
    if resposta2 == 'sim':
        carro = input('Qual carro deseja remover? ')
        carro_remover = indices[carro]
        for key in carros.keys():
            carros[key].pop(carro_remover)
    else:
        return

remover()
cria_indices()
print(indices)'''



#7 replace split lower

'''frase = f"O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será"
frase = frase.lower()
for char in '.,:;/?()`´':
    frase = frase.replace(char,'')
frase = frase.split(" ")

palavras = {}
for palavra in frase:
    if palavra in palavras.keys():
        palavras[palavra] += 1
    else:
        palavras[palavra] = 1
print'''(palavras)

#8 .join()
'''numeros = {
    'zero':'0',
    'um': '1',
    'dois': '2',
    'tres': '3',
    'quatro': '4',
    'cinco': '5',
    'seis': '6',
    'sete': '7',
    'oito': '8',
    'nove': '9',
    'dez:': '10'
}

frase = 'Eu tenho aula na sala cinco zero dois'


for key in numeros:
    if key in frase:
        frase = frase.replace(key,numeros[key])

print(frase)

'''

#9
'''dicionario1 = {
    'chave1' : '1',
    'chave2' : '2',
}

dicionario2 = {
    'chave1' : '1',
    'chave3' : '3',
}

lista = []
for key in dicionario1:
    if key in dicionario2.keys():
        lista.append(key)
print(lista)'''



#10
'''
lista_exclusao = []

for key in dicionario2:
    if key not in dicionario1.keys():
        lista_exclusao.append(key)
        
print(lista)'''
