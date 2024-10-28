def shell_sort(vetor):
    n = len(vetor)
    incrementos = []
    numIncrementos = 1

    while (pow(2, numIncrementos) - 1 < n):
        incrementos.append(pow(2, numIncrementos) - 1)
        numIncrementos += 1

    numIncrementos -= 1
    print(incrementos)

    for i in range(0, numIncrementos):
        span = incrementos[i]
        for j in range(span, n):
            y = vetor[j]

            k = j-span

            while (k >= 0 and vetor[k] > y):
                vetor[k+span] = vetor[k]
                k -= span

            vetor[k+span] = y
