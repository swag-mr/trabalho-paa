def bubbleSortMelhorado(vetor):
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

x = [5,1,3,5,9,10,-1,110]

bubbleSortMelhorado(x)

print(x)
