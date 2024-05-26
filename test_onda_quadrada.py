import numpy as np
import matplotlib.pyplot as plt
from teste1 import pulso_quadrado
from matplotlib.pyplot import get_cmap

plt.rcParams['figure.figsize'] = [8,8]
plt.rcParams.update({'font.size':18})

# define domain
dx = 0.001
L = np.pi
x = L * np.arange(-1+dx,1+dx,dx)
n = len(x)
nquart = int(np.floor(n/4))
#print(x)


#quadratic_Pulse = pulso_quadrado(1,points=x)
#define hat function
f,timedsa = pulso_quadrado(1,2,points=n)
#print(f)
fig, ax = plt.subplots()
#f[0] = 1
#plt.subplot(1,2,2)
#plt.plot(f)
#ax.plot(f)

#ax.plot(x,f,'-',color='k')
#plt.savefig("teste_onda")

#Compute fourier series
name = "Accent"
cmap = get_cmap('tab10')
#colors = cmap.colorbar_extend
#ax.set_prop_cycle(color=colors)

A0 = np.sum(f * np.ones_like(x)) * dx ## this is simulating a integral
fFS = A0/2
print(f"A0 = {fFS}")

An = np.zeros(30)
Bn = np.zeros(30)

#an = 2/to * integral(f(t)*cos(nW0t)dt)
for k in range(30):
    #in some way this is doing the integral
    #but the integral is a sum so make sense
    ## x/L is the W0?
    An[k] = np.sum(f * np.cos(np.pi*(k+1)*x/L)) * dx #Inner product
    print(f"An = {An[k]}")
    Bn[k] = np.sum(f * np.sin(np.pi*(k+1)*x/L)) * dx #Inner product
    print(f"Bn = {Bn[k]}")

    fFS = fFS + An[k] * np.cos(np.pi*(k+1)*x/L) + Bn[k] * np.cos(np.pi*(k+1)*x/L)
    ax.plot(x,fFS,'-')

#ax.plot(f)
fig.savefig("transforming_onda")