def shell_sort(vetor, n, incrementos, numIncrementos):
    for i in range(0, numIncrementos):
        span = incrementos[i]
        for j in range(span, n):
            y = vetor[j]

            k=j-span

            while(k >= 0 and vetor[k] > y):
                vetor[k+span] = vetor[k]
                k -= span

            vetor[k+span] = y
