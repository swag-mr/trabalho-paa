from timeit import default_timer
import random

def particao(vetor, p, r):
    pivo = vetor[p]
    up = r
    down = p
    while down < up:
        while down < r and vetor[down] <= pivo:
            down = down+1
        while up > p and vetor[up] > pivo:
            up = up-1
        if down < up:
            aux = vetor[down]
            vetor[down] = vetor[up]
            vetor[up] = aux
    vetor[p] = vetor[up]
    vetor[up] = pivo
    return up

def quick_sort_inicio(vetor, p, r):
    stack = []

    stack.append(p)
    stack.append(r)

    while len(stack) != 0:
        temp_end = stack.pop()
        temp_ini = stack.pop()

        if temp_ini < temp_end:
            q = particao(vetor, temp_ini, temp_end)

            stack.append(temp_ini)
            stack.append(q-1)

            stack.append(q+1)
            stack.append(temp_end)
