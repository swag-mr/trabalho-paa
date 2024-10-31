import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

algorithms = {
    '1': 'Bubble Sort',
    '2': 'Bubble Sort Melhorado',
    '3': 'Quick Sort (Início)',
    '4': 'Quick Sort (Meio)',
    '5': 'Insertion Sort',
    '6': 'Shell Sort',
    '7': 'Selection Sort',
    '8': 'Heap Sort',
    '9': 'Merge Sort',
}

print("Escolha um algoritmo de ordenação:")
for key, name in algorithms.items():
    print(f"{key}: {name}")

# Recebe a escolha do usuário
choice = input("Digite o número do algoritmo: ")

algorithm_name = algorithms[choice]
print(f"Você escolheu: {algorithm_name}")

# Tipos de ordenação dos dados
orders = ['random', 'ascending', 'descending']

df_plot = pd.read_csv(f'./csvs/{algorithm_name}.csv')
# Geração do gráfico de desempenho
plt.figure(figsize=(10, 6))
for order in orders:
    order_data = df_plot[df_plot["Ordem"] == order]
    smooth_time = gaussian_filter1d(order_data["Tempo"], sigma=1)
    plt.plot(order_data["Tamanho"], smooth_time, label=f'Dados {order}')

plt.title('Comparação de Desempenho - Dados Ascending')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo (segundos)')
plt.legend()
plt.grid(True)
plt.show()

