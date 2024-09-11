def insertionSort(vetor, n):
    for k in range(1, n):
        y = vetor[k]
        i = k-1
        while(i >= 0 and vetor[i] > y):
            vetor[i+1] = vetor[i]
            i -= 1
        vetor[i+1] = y

x = [5,1,3,5,9,10,-1,110]
insertionSort(x, len(x))

print(x)
