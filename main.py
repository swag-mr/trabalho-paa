import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from bubble_sort import bubble_sort
from bubble_melhorado import bubble_sort_melhorado
from quick_sort_inicio import quick_sort_inicio
from quick_sort_meio import quick_sort_meio
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from selection_sort import selection_sort
from heap_sort import heap_sort
from merge_sort import merge_sort

# Função para medir o tempo de execução
# -------------------------------------
# Esta função mede o tempo que um algoritmo de ordenação leva para ordenar
# uma cópia do array dado. Ela retorna o tempo total de execução em segundos.
#
# Parâmetros:
# - sort_fn: A função de ordenação que será medida.
# - arr: O array de entrada a ser ordenado.
#
# Retorno:
# - O tempo de execução em segundos.
def measure_time(sort_fn, arr):
    start_time = time.time()

    # Copia o array para evitar modificações
    sort_fn(arr.copy())

    end_time = time.time()

    return end_time - start_time

# Função para gerar vetores de entrada
# -------------------------------------
# Esta função gera um array de inteiros com base no tamanho e ordem desejados.
#
# Parâmetros:
# - size: O tamanho do array a ser gerado.
# - order: A ordem dos dados no array. Pode ser 'random', 'ascending' ou 'descending'.
#          - 'random': Gera números aleatórios.
#          - 'ascending': Gera números em ordem crescente.
#          - 'descending': Gera números em ordem decrescente.
#
# Retorno:
# - O array gerado com base nos parâmetros fornecidos.
def generate_data(size, order):
    if order == 'random':
        return random.sample(range(size*10), size)
    if order == 'ascending':
        return list(range(size))
    if order == 'descending':
        return list(range(size, 0, -1))

# Função principal
# -------------------------------------
# Esta função é o ponto de entrada do programa. Ela permite que o usuário escolha
# um algoritmo de ordenação, gera arrays de diferentes tamanhos e ordens (aleatório,
# crescente, decrescente), e então mede o tempo de execução do algoritmo escolhido
# para cada conjunto de dados. Finalmente, um gráfico é gerado para visualizar
# o desempenho.
def main():
    # Dicionário contendo os algoritmos disponíveis e suas funções associadas
    algorithms = {
        '1': ('Bubble Sort', bubble_sort),
        '2': ('Bubble Sort Melhorado', bubble_sort_melhorado),
        '3': ('Quick Sort (Início)', quick_sort_inicio),
        '4': ('Quick Sort (Meio)', quick_sort_meio),
        '5': ('Insertion Sort', insertion_sort),
        '6': ('Shell Sort', shell_sort), '7': ('Selection Sort', selection_sort),
        '8': ('Heap Sort', heap_sort),
        '9': ('Merge Sort', merge_sort)
    }

    # Exibe os algoritmos de ordenação disponíveis
    print("Escolha um algoritmo de ordenação:")
    for key, (name, _) in algorithms.items():
        print(f"{key}: {name}")

    # Recebe a escolha do usuário
    choice = input("Digite o número do algoritmo: ")

    if choice not in algorithms:
        print("Escolha inválida!")
        return

    algorithm_name, algorithm_fn = algorithms[choice]
    print(f"Você escolheu: {algorithm_name}")

    # Tamanhos de vetores a serem testados
    sizes = [1000, 5000, 10000, 15000, 20000, 25000]

    # Tipos de ordenação dos dados
    orders = ['random', 'ascending', 'descending']

    # Dicionário para armazenar os resultados de tempo para cada tipo de ordenação
    results = []

    # Testa o algoritmo escolhido com diferentes tamanhos e ordens de dados
    for order in orders:
        print(f"\nTestando com dados: {order}")
        for size in sizes:
            # Gera o array de acordo com o tamanho e a ordem
            arr = generate_data(size, order)

            # Mede o tempo de execução
            time_taken = measure_time(algorithm_fn, arr)

            results.append({"Ordem": order, "Tamanho": size, "Tempo": time_taken})
            print(f"Tamanho: {size}, Tempo: {time_taken:.6f} segundos")

    # Gera o dataframe para análise posterior
    df_results = pd.DataFrame(results)

    # Ao invés de printar, vou colocar em um arquivo csv
    print(df_results)

    # Geração do gráfico de desempenho
    plt.figure(figsize=(10, 6))
    for order in orders:
        order_data = df_results[df_results["Ordem"] == order]
        smooth_time = gaussian_filter1d(order_data["Tempo"], sigma=1)
        plt.plot(order_data["Tamanho"], smooth_time, label=f'Dados {order}')

    plt.title(f'Comparação de Desempenho - {algorithm_name}')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Tempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ponto de entrada do programa
# -------------------------------------
# Quando o script é executado, ele chama a função `main` para iniciar a interação
# com o usuário e realizar os testes de desempenho.
if __name__ == "__main__":
    main()
