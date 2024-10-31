import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# rodar todos os arquivos csv e plotar em uma imagem só
algorithms = [
    'Bubble Sort',
    'Bubble Sort Melhorado',
    'Quick Sort (Início)',
    'Quick Sort (Meio)',
    'Insertion Sort',
    'Shell Sort',
    'Selection Sort',
    'Heap Sort',
    'Merge Sort'
]

for i in range(len(algorithms)):
    df_plot = pd.read_csv(f'./csvs/{algorithms[i]}.csv')
    order_data = df_plot[df_plot["Ordem"] == 'descending']
    smooth_time = gaussian_filter1d(order_data["Tempo"], sigma=1)
    plt.plot(order_data["Tamanho"], smooth_time, label=f'{algorithms[i]}')

plt.title('Comparação de Desempenho - Dados Descending')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo (segundos)')
plt.legend()
plt.grid(True)
plt.show()

