'''lista = ['a','b','c','d']
print(lista[0])
for i in range(len(lista)):
    print(lista[i])

for elem in lista:
    print(elem)
#Printar 10 numeros
for i in range(10):
    print(i)
#Alterar uma lista
for elem in range(len(lista)):
    lista[i] = 1
print(lista)
    '''

'''
carros = ['Celta','Uno','Toro', 'UP']
precos = [1000000, 90, 500, 400]

for i in range(len(carros)):
    print(F'O carro é : {carros[i]} R$ {precos[i]:.2f}')

print('')

for i in range(len(carros)):
    if carros[i] == 'Celta':
        print(f'Celta : {precos[i]:.2f}')
        break
    elif i == len(carros) - 1:
        print('Carro não encontrado')
'''
def carros():
    carros = ['Celta','Uno','Toro', 'UP']
    precos = [1000000, 90, 500, 400]
    anos = [2004,2005,2010,1999]

    for i in range(len(carros)):
        print(f'{carros[i]}{precos[i]:.>20.2f}')

    carro = input('Digite um carro da lista: ')
    while carro not in carros:
        print('Digite um carro da lista!!')
        carro = input('Digite um carro da lista: ')

    for i in range(len(carros)):
        if carros[i] == carro:
            print('')
            print(f'Carro {carros[i]}{precos[i]:.>20.2f} feito em {anos[i]}')
            break

    indice_maior = 0
    maior = precos[indice_maior]
    for i in range(1, len(precos)):
        if precos[i] > maior :
            maior = precos[i]
            indice_maior = i
    print('')
    print(f'O carro que tem o maior preço é {carros[indice_maior]}{precos[indice_maior]:.>20.2f} ')

def inverte(lista):
    print(lista)
    for i in range(len(lista)//2):
        ultimo = len(lista) - 1
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return lista


# Funções

def input_numerico(msg):
    resposta = input(msg)
    while not resposta.isnumeric():
        resposta = input(msg)
    resposta = int(resposta)
    return resposta

def qntNumerosPares(numeros):
    pares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
    return pares

def mediaNumeros(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma / len(numeros)

def validarResposta(msg,opcoes_lista):
    resposta = input(msg).upper()
    while resposta not in opcoes_lista:
        resposta = input(msg).upper()
    return resposta




print(inverte([1,3,3,4,5]))