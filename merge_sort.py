import math

def merge(vetor, esq, q, di):
    esquerda = vetor[esq:q + 1]
    direita = vetor[q + 1:di + 1]

    i = 0
    j = 0
    k = esq

    # Mescla as sub-listas de volta no vetor original
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            vetor[k] = esquerda[i]
            i += 1
        else:
            vetor[k] = direita[j]
            j += 1
        k += 1

    # Copia os elementos restantes da sub-lista esquerda, se houver
    while i < len(esquerda):
        vetor[k] = esquerda[i]
        i += 1
        k += 1

    # Copia os elementos restantes da sub-lista direita, se houver
    while j < len(direita):
        vetor[k] = direita[j]
        j += 1
        k += 1

def merge_sort(vetor, esq, di):
    if esq < di:
        q =  math.floor((esq+di)/2)
        merge_sort(vetor, esq, q)
        merge_sort(vetor, q+1, di)
        merge(vetor, esq, q, di)
