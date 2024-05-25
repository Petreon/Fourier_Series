import numpy as np
import scipy.integrate as integrate
import scipy
import matplotlib.pyplot as plt

# Definindo os parâmetros

#print(len(t))
# Gerando a onda quadrada
def pulso_quadrado(quantidade_de_funcoes,freq):
    ##função sendo montada em radianos por segundo
    frequency = freq
    time = np.linspace(0, quantidade_de_funcoes, 1000)  # Tempo variando de 0 a 1 com 500 pontos
    square_wave = scipy.signal.square(2*np.pi* frequency * time)
    #print(square_wave)

    for i in range(0,len(square_wave)):
        if(square_wave[i] < 0):
            square_wave[i] = 0
    print(square_wave)

    return square_wave,time

array_Pulso_quadrado,tempo_funcao = pulso_quadrado(freq=1)


# Plotando a onda quadrada
plt.figure(figsize=(10, 5))
plt.plot(tempo_funcao, array_Pulso_quadrado)
plt.title('Onda Quadrada Periódica')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
##plt.show()
plt.savefig("Onda_Quadrada_periodica.png")