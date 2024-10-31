
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from scipy.signal import butter, lfilter
import numpy as np


class signalMeu:
    def __init__(self):
        self.init = 0
 
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
        plt.xlim(0,2200)
        plt.show(block = False)

    def filtro_passa_baixa(self, signal):
        y = np.zeros_like(signal) 
        y[0] = signal[0]
        y[1] = signal[1]

        a = 0.0005655
        b = 0.0005528
        d = - 1.933
        e = 0.9342
        
        for k in range(2, len(signal)):
            y[k] = - d* y[k - 1] - e * y[k - 2] + a * signal[k - 1] + b * signal[k - 2]
        return y
    
    def butter_lowpass_filter(self, data, cutoff, fs, order=15):
        # Cria um filtro passa-baixa Butterworth
        nyquist = 0.5 * fs  # Frequência de Nyquist
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = lfilter(b, a, data)
        return y

    
    

