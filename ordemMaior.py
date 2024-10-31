import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft



#Importe todas as bibliotecas
from suaBibSignal import *
from scipy.signal import find_peaks #troquei para encontrar os picos do gráfico
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
from scipy.io.wavfile import write

def main():

    #*****************************instruções********************************
    #declare um objeto da classe da sua biblioteca de apoio (cedida)   
    # algo como:
    signal = signalMeu() 
       
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    sd.default.samplerate = 44100  #taxa de amostragem
    sd.default.channels = 1 #numCanais # o numero de canais, tipicamente são 2. Placas com dois canais. Se ocorrer problemas pode tentar com 1. No caso de 2 canais, ao gravar um audio, terá duas listas.
    #Muitas vezes a gravação retorna uma lista de listas. Você poderá ter que tratar o sinal gravado para ter apenas uma lista.
    duration =  5 # #tempo em segundos que ira aquisitar o sinal acustico captado pelo mic   
    #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisições) durante a gravação. Para esse cálculo você deverá utilizar a taxa de amostragem e o tempo de gravação
    freqDeAmostragem = 44100
    numAmostras = freqDeAmostragem*duration
    #faca um print na tela dizendo que a captação comecará em n segundos. e então 
    #use um time.sleep para a espera.
    for i in range(3):
        print(f"A gravação vai começar em {3-i} segundos!")
        time.sleep(1)
    
    
    #A seguir, faca um print informando que a gravacao foi inicializada
    print("A gravação começou!")
    

    #para gravar, utilize
    audio = sd.rec(int(numAmostras), freqDeAmostragem, channels=1)
    
    sd.wait()
    print("...     FIM")
    # Salvar o áudio como um arquivo .wav
    write("minha_gravacao.wav", freqDeAmostragem, audio)
    print("Áudio salvo como 'minha_gravacao.wav'")

    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, ou uma lista, ou ainda uma lista de listas (isso dependerá do seu sistema, drivers etc...).
    #extraia a parte que interessa da gravação (as amostras) gravando em uma variável "dados". Isso porque a variável audio pode conter dois canais e outas informações). 
    dados = [dado[0] for dado in audio]
       
    ## Calcule e plote o Fourier do sinal audio. como saída tem-se a amplitude e as frequências.
    
    # filtrado = signal.filtro_passa_baixa(dados)
    filtrado = signal.butter_lowpass_filter(dados, 1500, freqDeAmostragem)
    # ------------- PLOTA FOURRIER ANTES -----------#
    signal.plotFFT(dados, freqDeAmostragem)
    plt.title("Fourrier antes do filtro")
    # plt.show(block = False)
    # ------------- PLOTA FOURRIER DEPOIS -----------#
    signal.plotFFT(filtrado, freqDeAmostragem)
    plt.title("Fourrier depois do filtro")
    plt.show()
    
   
if __name__ == "__main__":
    main()

