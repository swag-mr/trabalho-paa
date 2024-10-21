def particao(vetor, p, r):
    meio = (p + r) // 2
    pivo = vetor[meio]
    
    vetor[meio], vetor[r] = vetor[r], vetor[meio]
    
    up = r - 1
    down = p
    while down <= up:
        while down <= up and vetor[down] <= pivo:
            down += 1
        while down <= up and vetor[up] > pivo:
            up -= 1
        if down < up:
            vetor[down], vetor[up] = vetor[up], vetor[down]

    vetor[r], vetor[down] = vetor[down], vetor[r]
    return down

def quickSortMeio(vetor, p, r):
    if p < r:
        q = particao(vetor, p, r)
        quickSortMeio(vetor, p, q - 1)
        quickSortMeio(vetor, q + 1, r)

x = [5, 1, 3, 5, 9, 10, -1, 110]

quickSortMeio(x, 0, len(x) - 1)

print(x)
