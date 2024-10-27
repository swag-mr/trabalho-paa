def insertion_sort(vetor, n):
    for k in range(1, n):
        y = vetor[k]
        i = k-1
        while(i >= 0 and vetor[i] > y):
            vetor[i+1] = vetor[i]
            i -= 1
        vetor[i+1] = y
