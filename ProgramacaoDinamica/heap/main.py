def promove(heap, indice):
    """Move o elemento para cima até restaurar a propriedade do heap."""

    # Se for menor que o pai, troca
    pai = (indice - 1) // 2
    if indice > 0 and heap[indice] < heap[pai]:
        heap[indice], heap[pai] = heap[pai], heap[indice]
        promove(heap, pai)  # Continua promovendo recursivamente

def inserir(heap, elemento):
    """Move o elemento para cima ate restaurar a propriedade do heap"""
    heap.append(elemento)
    i = len(heap) - 1
    while i > 1:
        pai = i // 2
        if heap[i] > heap[pai]:
            heap[i], heap[pai] = heap[pai], heap[i]
            i = pai
        else:
            break


def demove(A):
    i = 1
    n = len(A)
    A[1], A[-1] = A[-1], A[1]
    A.pop()
    while True:
        c = 2 * i
        # Elemento não tem mais filhos.
        if c > n:
            break
            # Encontra o índice do maior dos filhos.
        if c + 1 <= n:
            if A[c + 1] > A[c]:
                c += 1
        # O elemento é msior que seu maior filho.
        if A[i] >= A[c]:
            break
        # Troca elemento de lugar com o maior filho.
        A[c], A[i] = A[i], A[c]
        i = c


heap = [None]

inserir(heap, 15)
inserir(heap, 20)
inserir(heap, 10)
inserir(heap, 30)
