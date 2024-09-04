import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# Configurações do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('Uso de CPU e Memória')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Uso (%)')

# Linhas para CPU e Memória
cpu_line, = ax.plot([], [], label='CPU', color='#FF5733')
mem_line, = ax.plot([], [], label='Memória', color='#C70039')
ax.legend()

# Textos para exibir os valores atuais
cpu_text = ax.text(0.77, 0.7, '', transform=ax.transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
mem_text = ax.text(0.77, 0.6, '', transform=ax.transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Dados para a animação
max_len = 100
cpu_data = deque(maxlen=max_len)
mem_data = deque(maxlen=max_len)
times = deque(maxlen=max_len)


def init():
    """Inicializa as linhas do gráfico."""
    cpu_line.set_data([], [])
    mem_line.set_data([], [])
    return cpu_line, mem_line, cpu_text, mem_text


def update(frame):
    """Atualiza o gráfico com os dados mais recentes."""
    # Obtém informações de uso da CPU e memória
    cpu_percent = psutil.cpu_percent(interval=0.1)  # Intervalo menor para atualizações mais frequentes
    memory_percent = psutil.virtual_memory().percent

    # Atualiza os dados
    cpu_data.append(cpu_percent)
    mem_data.append(memory_percent)
    times.append(frame)

    # Atualiza as linhas do gráfico
    cpu_line.set_data(times, cpu_data)
    mem_line.set_data(times, mem_data)

    # Ajusta o eixo X para mostrar a janela mais recente
    if len(times) > 0:
        ax.set_xlim(max(0, frame - max_len), frame)

    # Atualiza os textos com os valores atuais
    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memória: {memory_percent:.1f}%')

    return cpu_line, mem_line, cpu_text, mem_text


# Animação do gráfico
animation = FuncAnimation(
    fig, update, frames=range(1000), init_func=init, interval=500, blit=True
)

# Estilização do gráfico
for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

ax.set_facecolor('#F5F5F5')

# Adiciona uma barra de rolagem horizontal (opcional)
fig.tight_layout(pad=3.0)

# Exibe o gráfico
plt.show()
