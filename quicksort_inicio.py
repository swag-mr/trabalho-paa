def particao(vetor, p, r):
    pivo = vetor[p]
    up = r
    down = p
    while down < up :
        while vetor[down] <= pivo:
            down = down+1
        while vetor[up] > pivo:
            up = up-1
        if(down < up):
            aux = vetor[down]
            vetor[down] = vetor[up]
            vetor[up] = aux
    vetor[p] = vetor[up]
    vetor[up] = pivo
    return up

def quickSortInicio(vetor, p, r):
    if(p < r):
        q = particao(vetor, p, r)
        quickSortInicio(vetor, p, q-1)
        quickSortInicio(vetor, q+1, r)

x = [5,1,3,5,9,10,-1,110]
quickSortInicio(x,0,len(x)-1)

print(x)
