def bubble_sort_melhorado(vetor):
    troca = True
    for i in range(len(vetor)):
        if not troca:
            break
        troca = False
        for j in range(len(vetor)-1-i):
            if vetor[j] > vetor[j+1]:
                troca = 1
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
