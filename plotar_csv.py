import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# rodar todos os arquivos csv e plotar em uma imagem só
df_plot = pd.read_csv("Heap Sort.csv")

order_data = df_plot[df_plot["Ordem"] == 'random']
smooth_time = gaussian_filter1d(order_data["Tempo"], sigma=1)
plt.plot(order_data["Tamanho"], smooth_time, label=f'{'Heap Sort'}')

plt.title(f'Comparação de Desempenho - Dados Random')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo (segundos)')
plt.legend()
plt.grid(True)
plt.show()
