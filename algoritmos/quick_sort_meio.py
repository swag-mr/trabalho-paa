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

def quick_sort_meio(vetor):
    p = 0
    r = len(vetor) - 1
    stack = []

    # Empilha os índices inicial e final
    stack.append(p)
    stack.append(r)

    while len(stack) != 0:
        temp_end = stack.pop()
        temp_ini = stack.pop()

        if temp_ini < temp_end:
            # Particiona o vetor e obtém o índice do pivô
            q = particao(vetor, temp_ini, temp_end)

            # Empilha os subvetores esquerdo e direito
            stack.append(temp_ini)
            stack.append(q - 1)

            stack.append(q + 1)
            stack.append(temp_end)
