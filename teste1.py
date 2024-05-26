import numpy as np
import scipy.integrate as integrate
import scipy
import matplotlib.pyplot as plt

# Definindo os parâmetros

#print(len(t))
# Gerando a onda quadrada
def pulso_quadrado(freq,quantidade_de_funcoes=1,points=1000):
    ##função sendo montada em radianos por segundo
    frequency = freq
    #before = np.linspace(0,0,250)
    after = np.linspace(0,0,250)
    time = np.linspace(0, quantidade_de_funcoes, points)  # Tempo variando de 0 a 1 com 500 pontos
    square_wave = scipy.signal.square(2*np.pi* frequency * time)
    #print(square_wave)

    for i in range(0,len(square_wave)):
        if(square_wave[i] < 0):
            square_wave[i] = 0
    #print(square_wave)

    #newarray = np.concatenate((before,square_wave),axis=None)
    #newarray = np.concatenate((newarray,after),axis=None)

    return square_wave,time

#array_Pulso_quadrado,tempo_funcao = pulso_quadrado(1)

#print(array_Pulso_quadrado)
#plt.plot(array_Pulso_quadrado)
#plt.savefig("alooooo")

##fourier transform 
#fourierTransform = np.fft.rfft(array_Pulso_quadrado,2,norm="backward")
#real = np.real(fourierTransform)
#print(fourierTransform)
#print(real)


# Plotando a onda quadrada
#plt.figure(figsize=(10, 5))
#plt.subplot(1,2,1)
#plt.plot(array_Pulso_quadrado)
#plt.title('Onda Quadrada Periódica')
#plt.xlabel('Tempo')
#plt.ylabel('Amplitude')
#plt.grid(True)
##plt.show()
#plt.figure(figsize=(10, 5))
#plt.subplot(1,2,2)
#plt.plot(fourierTransform)
#plt.title('Onda Quadrada Periódica')
#plt.xlabel('Tempo')
#plt.ylabel('Amplitude')
#plt.grid(True)
##plt.show()

#plt.savefig("Onda_Quadrada_periodica.png")
