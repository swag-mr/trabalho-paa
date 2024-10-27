def bubble_sort(vetor):
    for j in range(0, len(vetor)):
        for i in range(0, len(vetor)-j-1):
            if vetor[i] > vetor[i+1] :
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux
