import subprocess
import re
import matplotlib.pyplot as plt

# Configuração do matplotlib
plt.ion()
fig, ax = plt.subplots()
latencies = []
window_size = 50  # número de pontos exibidos no gráfico de uma vez
plot_line, = ax.plot(latencies)
ax.set_ylim(0, 200)  # Defina um limite Y inicial


def update_plot(latency):
    latencies.append(latency)

    # Manter apenas os últimos 'window_size' pontos
    if len(latencies) > window_size:
        del latencies[0]

    plot_line.set_ydata(latencies)
    plot_line.set_xdata(range(len(latencies)))
    ax.set_xlim(0, len(latencies))

    # Atualizar os limites do eixo Y com base nos valores atuais
    ax.set_ylim(min(latencies) - 10, max(latencies) + 10)

    fig.canvas.flush_events()


try:
    process = subprocess.Popen(
        ["ping", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    while True:
        ping_output = process.stdout.readline().strip()
        if not ping_output:
            break

        # Procura o tempo de latência na saída
        match = re.search("time=([\d.]+) ms", ping_output)
        if match:
            latency = float(match.group(1))
            print(f"Latency: {latency} ms")
            update_plot(latency)

except KeyboardInterrupt:
    process.terminate()

plt.ioff()
plt.show()
