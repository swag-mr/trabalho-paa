def merge(vetor, esq, q, di):
    esquerda = vetor[esq:q + 1]
    direita = vetor[q + 1:di + 1]

    i = 0
    j = 0
    k = esq

    # Mescla as sub-listas de volta no vetor original
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            vetor[k] = esquerda[i]
            i += 1
        else:
            vetor[k] = direita[j]
            j += 1
        k += 1

    # Copia os elementos restantes da sub-lista esquerda, se houver
    while i < len(esquerda):
        vetor[k] = esquerda[i]
        i += 1
        k += 1

    # Copia os elementos restantes da sub-lista direita, se houver
    while j < len(direita):
        vetor[k] = direita[j]
        j += 1
        k += 1

def merge_sort(vetor):
    n = len(vetor)

    # Subdivide o vetor em partes cada vez menores
    sublista_tamanho = 1
    while sublista_tamanho < n:
        # Percorre o vetor dividindo em sublistas do tamanho atual
        for esq in range(0, n, 2 * sublista_tamanho):
            q = min(esq + sublista_tamanho - 1, n - 1)
            di = min(esq + 2 * sublista_tamanho - 1, n - 1)
            if q < di:  # Mescla apenas se q e di forem válidos
                merge(vetor, esq, q, di)

        # Dobra o tamanho das sublistas a cada iteração
        sublista_tamanho *= 2

