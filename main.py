import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def calcFFT(self, signal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N = len(signal)
        # W = windows.hamming(N)  # Corrigido
        T = 1 / fs
        xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
        yf = fft(signal)
        return xf, np.abs(yf[0:N // 2])

def plotFFT(self, signal, fs):
        x, y = self.calcFFT(signal, fs)
        plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Magnitude')
        plt.grid()
        plt.xlim(600,1700)
        plt.show()

def filtro_passa_baixo(signal):
    y = np.zeros_like(signal) 
    y[0] = signal[0]
    y[1] = signal[1]

    a = 0.001547
    b = 0.00149
    d = -1.89
    e = 0.8928
    
    for k in range(2, len(signal)):
        y[k] = - d* y[k - 1] - e * y[k - 2] + a * signal[k - 1] + b * signal[k - 2]
    return y


