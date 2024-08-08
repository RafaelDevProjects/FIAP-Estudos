import matplotlib.pyplot as plt


def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    return


def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz


def diagonal_da_matriz(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1

    return matriz


def contra_diagonal_da_matriz(matriz):
    tam = len(matriz)
    for i in range(tam):
        matriz[i][tam - 1 - i] = 1
    return matriz


def contra_diagonal_da_matriz_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == len(matriz) - 1:
                matriz[i][j] = 1
    return matriz


def altera_diagonal_acima(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i < j:
                matriz[i][j] = 1
    return matriz

def altera_diagnonal_acima_bom(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return matriz


def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return matriz


def tabuleiro_xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i + j) % 2 == 0:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    return matriz



notas = [[1, 2],[4, 5],[7, 8],[10, 11],[13, 14]]
pesos_notas = [1, 2, 3, 4, 5]
soma_pesos = 0
media_ponderada = []

for j in range(len(notas[0])):
    soma = 0
    for i in range(len(pesos_notas)):
        soma += notas[i][j] * pesos_notas[i]
        soma_pesos += pesos_notas[i]
    media_ponderada.append(soma/soma_pesos)
print(media_ponderada)


def cinema(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (i + j) % 2 == 0:
                matriz[linha][coluna] = 'ocupada'
            else:
                matriz[linha][coluna] = 'vaga'
    return matriz


matriz = cria_matriz(50,50)
print_matriz(cinema(matriz))

