def intersecao(lista1, lista2):
    nova_lista = []
    for i in range(len(lista1)):
        for c in range(len(lista2)):
            if lista1[i] == lista2[c]:
                nova_lista.append(lista1[i])
    return nova_lista



def maximo(numeros):
    maior = 0
    indice_maior = 0
    for i in range(len(numeros)):
        if maior < numeros[i]:
            indice_maior = i
    return indice_maior

def minimo(numeros):
    minimo = 9999
    indice_menor = 0
    for i in range(len(numeros)):
        if minimo < numeros[i]:
            indice_menor = i
    return indice_menor

def valida_opcao(opcao):
    while not (opcao == 'B' or opcao == 'C'):
        opcao = input('Você quer o carro mais caro ou o mais barato?[B/C]').upper()
    return opcao


carros = ['UNO','FOX','CELTA']
potencia = [100,200,1000]
preco = [200,30, 500]

resposta = input('Você quer o carro mais caro ou o mais barato?[B/C]').upper()
valida_opcao(resposta)
if resposta == 'C':
    print(carros[maximo(preco)])
elif resposta == 'B':
    print(carros[minimo(preco)])






