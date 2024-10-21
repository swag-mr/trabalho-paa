def selectionSort(vetor):
    for i in range(len(vetor)-1):
        menor = vetor[i]
        index = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < menor:
                menor = vetor[j]
                index = j

        vetor[index] = vetor[i]
        vetor[i] = menor

x = [5,1,3,5,9,10,-1,110]

selectionSort(x)

print(x)
