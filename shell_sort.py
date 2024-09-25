def shellSort(vetor, n, incrementos, numIncrementos):
    for i in range(0, numIncrementos):
        span = incrementos[i]
        for j in range(span, n):
            y = vetor[j]

            k=j-span

            while(k >= 0 and vetor[k] > y):
                vetor[k+span] = vetor[k]
                k -= span

            vetor[k+span] = y;

x = [6,1,3,5,9,10,-1,110]
increments = [4,2,1]

shellSort(x,len(x), increments, len(increments))

print(x)
