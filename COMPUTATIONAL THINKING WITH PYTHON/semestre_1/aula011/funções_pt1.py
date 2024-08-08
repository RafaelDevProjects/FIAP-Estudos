def somarLista(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma




def verificaNumero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num




def paresLista(lista):
    pares =[]
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares




def inverte(lista):
    ultimo = len(lista) - 1
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return lista




def tirarDuplicatados(lista):
    for i in range(len(lista)):
        if lista[i] == lista[i+1]:
            del lista[i]
    return lista




def elem_in_lista(alvo,lista):
    for elem in alvo:
        if elem == alvo:
            return True
    return False


def duplicados(lista):
    filtrada = []
    for elem_a in lista:
        pertence_ou_não = elem_in_lista(elem_a,filtrada)
        if pertence_ou_não == False:
            filtrada.append(elem_a)
    return filtrada




def maximo(numeros):
    maior = 0
    indice_maior = 0
    for i in range(len(numeros)):
        if maior < numeros[i]:
            indice_maior = i
            maior = numeros[i]
    return indice_maior




def comprimento(lista):
    cont = 0
    for elem in lista:
        cont += 1
    return cont


def numeroPrimos(lista):
    c = 2
    primos = []
    for i in range(len(lista)):
        if c >= lista[i]/2:
            primos.append(lista[i])
        c += 1
    return primos


lista = [1,2,10,2]
indice_maior =maximo(lista)
print(lista[indice_maior])

