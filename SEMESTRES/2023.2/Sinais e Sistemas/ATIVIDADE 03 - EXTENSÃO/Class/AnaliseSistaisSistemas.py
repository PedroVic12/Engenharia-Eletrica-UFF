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
