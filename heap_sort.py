def heapify(vetor, n, i):
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and vetor[i] < vetor[l]:
        maior = l

    if r < n and vetor[maior] < vetor[r]:
        maior = r

    if maior != i:
        (vetor[i], vetor[maior]) = (vetor[maior], vetor[i])

def heapSort(vetor):
    n = len(vetor)

    for i in range(n // 2, -1, -1):
        heapify(vetor, n, i)

    for i in range(n-1, 0, -1):
        (vetor[i], vetor[0]) = (vetor[0], vetor[i])
        heapify(vetor, i, 0)

x = [5,1,3,5,9,10,-1,110, 200]
heapSort(x)

print(x)
