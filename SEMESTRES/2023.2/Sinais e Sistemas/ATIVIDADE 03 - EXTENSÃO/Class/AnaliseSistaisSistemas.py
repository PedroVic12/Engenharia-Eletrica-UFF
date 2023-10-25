import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


class AnaliseSinaisESistemas:

    def __init__(self) -> None:
        self._sinal = []
        self.timer = 0
        self.taxa_amostragem = ''
        self.frequency = ''

    def carregar_sinal(self, par=0):
        data, timer = hp.load_exampledata(par)
        return data, timer

    def visualizationSignal(self, _data, titulo):
        plt.figure(figsize=(12, 4))
        plt.plot(_data)
        plt.title(titulo)
        plt.show()

    def gerarSinalExemplo(self):
        # Criar um sinal de exemplo
        t = np.linspace(0, 1, 1000, endpoint=False)
        signal_freq = 5  # Frequência do sinal
        signal_amplitude = 1
        signal_waveform = signal_amplitude * \
            np.sin(2 * np.pi * signal_freq * t)

        return signal_waveform

    def filtragem_fir(self, signal_waveform):
        t = np.linspace(0, 1, 1000, endpoint=False)

        # Criar um filtro FIR passa-baixa
        cutoff_freq = 10  # Frequência de corte
        num_taps = 30
        fir_filter = scipy.signal.firwin(num_taps, cutoff_freq / (0.5 * 1000))

        # Aplicar o filtro ao sinal
        filtered_signal = scipy.signal.lfilter(
            fir_filter, 1.0, signal_waveform)

        # Plotar o sinal original e o sinal filtrado
        plt.plot(t, signal_waveform, label='Sinal Original')
        plt.plot(t, filtered_signal, label='Sinal Filtrado')
        plt.legend()
        plt.show()

    def resposta_frequencia_fir(self):
        # Parâmetros do filtro FIR
        num_taps = 64
        cutoff_freq = 0.1

        # Projeto da janela do filtro
        fir_coefficients = scipy.signal.firwin(num_taps, cutoff_freq)

        # Resposta em frequência do filtro
        w, h = scipy.signal.freqz(fir_coefficients)

        # Plotar a resposta em frequência
        plt.plot(w, abs(h))
        plt.title("Resposta em Frequência do Filtro FIR")
        plt.xlabel("Frequência normalizada")
        plt.ylabel("Magnitude")
        plt.grid()
        plt.show()

    def espectro_frequencia(self, signal_waveform):

        # Calcular a transformada de Fourier
        signal_spectrum = scipy.signal.fft(signal_waveform)

        # Plotar o espectro de frequência
        plt.plot(np.abs(signal_spectrum))
        plt.show()

    def janela(self):
        # Escolher uma janela (por exemplo, janela de Hamming)
        window = scipy.signal.get_window('hamming', 64)

        # Plotar a janela
        plt.plot(window)
        plt.title('Janela de Hamming')
        plt.xlabel('Amostra')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()

    def resposta_frequencia(self):
        # Parâmetros do filtro
        b = [0.1, 0.2, 0.3, 0.4, 0.5]
        a = [1, -0.5, 0.25, -0.125, 0.0625]

        # Calcular a resposta em frequência
        w, h = scipy.signal.freqz(b, a)

        # Plotar a resposta em frequência
        plt.plot(w, 20 * np.log10(abs(h)))
        plt.title('Resposta em Frequência')
        plt.xlabel('Frequência [radianos / amostra]')
        plt.ylabel('Ganho [dB]')
        plt.grid()
        plt.show()

    def convolucao(self, x, h):
        # Realizar a convolução
        y = scipy.signal.convolve(x, h, mode='full')

        # Plotar os sinais e o resultado da convolução
        plt.stem(x, basefmt=" ", linefmt="b-", markerfmt="bo", label='x[n]')
        plt.stem(h, linefmt="g-", markerfmt="go", label='h[n]')
        plt.stem(y, linefmt="r-", markerfmt="ro", label='x[n] * h[n]')
        plt.legend()
        plt.show()

    def calculaCoherence(self, _data1, _data2, taxa_amostragem):
        frequencies, coh = scipy.signal.coherence(
            _data1, _data2, fs=taxa_amostragem)
        return frequencies, coh

    def calculaFFT(self, _data, taxa_amostragem):
        fft_result = np.fft.fft(_data)
        fft_freq = np.fft.fftfreq(len(_data), 1 / taxa_amostragem)
        return fft_freq, fft_result

    def gerarGrafico(self, matriz, titulo, labels=[]):
        plt.figure(figsize=(12, 4))
        plt.plot(matriz)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.title(titulo)
        plt.show()

    def calculaPeriodograma(self, data):
        frequencies, Pxx_density = scipy.signal.periodogram(data, fs=100)
        plt.semilogy(frequencies, Pxx_density)
        plt.title('Periodograma')
        plt.xlabel('Frequencia [Hz]')
        plt.ylabel('PSD')
        plt.show()

    def calculaWelchMethod(self, data):
        frequencies, Pxx_den = scipy.signal.welch(data, fs=100)
        plt.semilogy(frequencies, Pxx_den)
        plt.title('Welch’s Method')
        plt.xlabel('Frequencia [Hz]')
        plt.ylabel('PSD')
        plt.show()
