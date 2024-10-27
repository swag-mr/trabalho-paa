def particao(vetor, p, r):
    pivo = vetor[p]
    up = r
    down = p
    while down < up:
        while down < r and vetor[down] <= pivo:
            down += 1
        while up > p and vetor[up] > pivo:
            up -= 1
        if down < up:
            vetor[down], vetor[up] = vetor[up], vetor[down]
    vetor[p], vetor[up] = vetor[up], pivo
    return up

def quick_sort_inicio(vetor):
    p = 0
    r = len(vetor) - 1
    stack = [p, r]

    while stack:
        temp_end = stack.pop()
        temp_ini = stack.pop()

        if temp_ini < temp_end:
            q = particao(vetor, temp_ini, temp_end)

            stack.append(temp_ini)
            stack.append(q - 1)

            stack.append(q + 1)
            stack.append(temp_end)

