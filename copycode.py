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
f = np.zeros_like(x)
f[nquart:2*nquart] = (4/n)*np.arange(1,nquart+1)
f[2*nquart:3*nquart] = np.ones(nquart) - (4/n)*np.arange(0,nquart)
#print(f)

fig, ax = plt.subplots()

ax.plot(x,f,'-',color='k')
fig.savefig("copytest")

#Compute fourier series
name = "Accent"
cmap = get_cmap('tab10')
#colors = cmap.colorbar_extend
#ax.set_prop_cycle(color=colors)

A0 = np.sum(f * np.ones_like(x)) * dx ## this is simulating a integral
fFS = A0/2

An = np.zeros(20)
Bn = np.zeros(20)

#an = 2/to * integral(f(t)*cos(nW0t)dt)
for k in range(20):
    #in some way this is doing the integral
    #but the integral is a sum so make sense
    ## x/L is the W0?
    An[k] = np.sum(f * np.cos(np.pi*(k+1)*x/L)) * dx #Inner product
    Bn[k] = np.sum(f * np.sin(np.pi*(k+1)*x/L)) * dx #Inner product
    fFS = fFS + An[k] * np.cos(np.pi*(k+1)*x/L) + Bn[k] * np.cos(np.pi*(k+1)*x/L)
    ax.plot(x,fFS,'-')

fig.savefig("transforming")