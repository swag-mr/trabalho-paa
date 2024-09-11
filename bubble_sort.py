def bubbleSort(vetor):
    for j in range(0, len(vetor)):
        for i in range(0, len(vetor)-j-1):
            if(vetor[i] > vetor[i+1]):
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux

x = [5,1,3,5,9,10,-1,110]
bubbleSort(x)

print(x)
