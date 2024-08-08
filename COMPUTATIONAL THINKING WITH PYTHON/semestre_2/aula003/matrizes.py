import matplotlib.pyplot as plt

def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    return


def criar_matriz(linhas, colunas):
    matriz = []
    for linha in range(linhas):
        lista = []
        for coluna in range(colunas):
            lista.append(linha+coluna)
        matriz.append(lista)
    return matriz


def divide_matriz_trigonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = 0
            if j > i:
                matriz[i][j] = 1
            elif j < i:
                matriz[i][j] = 2
            else:
                matriz[i][j] = 0

def tabuleiro_de_xadrez(matriz):
    """
    [0,1,0,1,0,1] par
    [1,0,1,0,1,0] impar
    [0,1,0,1,0,1] par
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i % 2 == 0:
                if j % 2 == 0:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
            else:
                if j % 2 == 0:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] = 1

def matriz_de_permutacao():
    matriz = []
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i in range(len(lista)):
        linha = []
        linha.append(i)
    matriz.append(linha)
    return matriz





segunda_matriz = criar_matriz(8, 8)
tabuleiro_de_xadrez(segunda_matriz)
print_matriz(segunda_matriz)
plt.imshow(segunda_matriz, cmap= 'grey')
plt.colorbar()
plt.show()

print(matriz_de_permutacao())


