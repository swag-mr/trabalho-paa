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

def mergeSort(vetor, esq, di):
    if esq < di:
        q =  math.floor((esq+di)/2)
        mergeSort(vetor, esq, q)
        mergeSort(vetor, q+1, di)
        merge(vetor, esq, q, di)

x = [5,1,3,5,9,10,-1,110]

mergeSort(x, 0, len(x)-1)

print(x)
