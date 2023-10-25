import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


class AnaliseSinaisESistemas:
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

    def gerarGrafico(self, matriz, titulo):
        plt.figure(figsize=(12, 4))
        plt.plot(matriz)
        plt.title(titulo)
        plt.show()


def main():
    signals = AnaliseSinaisESistemas()
    data, timer = signals.carregar_sinal(0)
    data2, timer2 = signals.carregar_sinal(1)
    signals.visualizationSignal(data, 'Sinal PPG Original 1')
    signals.visualizationSignal(data2, 'Sinal PPG Original 2')
    frequencies, coh = signals.calculaCoherence(data, data2, 100)
    plt.figure(figsize=(12, 4))
    plt.semilogy(frequencies, coh)
    plt.title('Coerência entre os Sinais')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Coerência')
    plt.show()


main()
