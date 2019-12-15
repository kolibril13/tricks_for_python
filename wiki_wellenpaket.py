import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.ion()
fig= plt.figure(1)
i=1


a=1. ; dt =0.2 ; N=30
xmin=-0.1  ;  xmax= N ;  ymin= -1  ;  ymax=  1.1
x = np.arange(0,N,0.01)
t = np.arange(0.0, 100.0, 0.01)
karray = np.arange(0.1,10,0.1)
print (karray)
def E(karray,x):
    return karray
def E2(karray,x):
    return np.power(karray,.95)
def E3(karray,x):
    return np.power(karray,1.05)
def f(x,t,a):
    wert = 0
    for k in karray:
        wert += np.exp(1j*(k*x-E(k,x)*t)).real/len(karray)
    return wert
def g(x,t,a):
    wert = 0
    for k in karray:
        wert += np.exp(1j*(k*x-E2(k,x)*t)).real/len(karray)
    return wert
def h(x,t,a):
    wert = 0
    for k in karray:
        wert += np.exp(1j*(k*x-E3(k,x)*t)).real/len(karray)
    return wert
def updatefig(*args):
    global i

    plt.subplot(211)
    plt.cla()
    plt.axis([xmin, xmax, ymin, ymax]) ### achsenabschnitte
    #plt.xlabel('Ort x')
    plt.ylabel('Amplitude $\Re(\psi)$')
    im = plt.plot(x,f(x,i,a), marker = '' ,c='r' ,ls='-', label = r'ohne Dispersion: $\frac{\partial \omega_j}{\partial k_j} = konstant$')
    plt.legend()

    plt.subplot(212)
    plt.cla()
    plt.axis([xmin, xmax, ymin, ymax]) ### achsenabschnitte 
    plt.xlabel('Ort x')
    plt.ylabel('Amplitude $\Re(\psi)$')
    im = plt.plot(x,g(x,i,a), marker = '' ,c='r' ,ls='-', label = r'mit Dispersion: $\frac{\partial \omega_j}{\partial k_j} \neq konstant$')
    plt.legend()
    print(i)
    i = i+dt
    return im,
#plt.subplot(211)
#plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
ani = animation.FuncAnimation(fig, updatefig, save_count=400, interval = 1)
#Writer = animation.writers['imagemagick'] #für gif
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#ani.save('wiki.gif', writer=writer)
input()

    
    
