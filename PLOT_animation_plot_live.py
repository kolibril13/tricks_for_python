import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

save_animation = "n"

pixel = 20
start_frames = 0
total_frames = 2 * start_frames + pixel

fig = plt.figure(num=None, figsize=(16, 9), dpi=100, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

i = 1
a = 1.;
dt = 0.2;
N = 30
xmin = -0.1;
xmax = N;
ymin = -1;
ymax = 1.1
x = np.arange(0, N, 0.01)
t = np.arange(0.0, 100.0, 0.01)
karray = np.arange(1, 10, 0.1)


def E(karray, x):
    return karray


def E2(karray, x):
    return karray


def f(x, t, a):
    wert = 0
    for k in karray:
        wert += np.exp(1j * (k * x - E(k, x) * t)).real / len(karray)
    return wert


def g(x, t, a):
    wert = 0
    for k in karray:
        wert += np.exp(1j * (k * x - E2(k, x) * t)).real / len(karray)
    return wert


def updatefig(*args):
    global i
    ax1.cla()
    ax1.axis([xmin, xmax, ymin, ymax])  ### achsenabschnitte
    ax1.set_xlabel('Ort x')
    ax1.set_ylabel('Amplitude $\Re(\psi)$')
    im = ax1.plot(x, f(x, i, a), marker='', c='r', ls='-',
                  label=r'ohne Dispersion: $\frac{\partial \omega_j}{\partial k_j} = konstant$')
    ax1.legend()

    ax2.cla()
    ax2.axis([xmin, xmax, ymin, ymax])  ### achsenabschnitte
    ax2.set_xlabel('Ort x')
    ax2.set_ylabel('Amplitude $\Re(\psi)$')
    im = ax2.plot(x, g(x, i, a), marker='', c='r', ls='-',
                  label=r'mit Dispersion: $\frac{\partial \omega_j}{\partial k_j} \neq konstant$')
    ax2.legend()

    i = i + dt
    return im,


ani = animation.FuncAnimation(fig, updatefig, interval=50, save_count=total_frames)
if save_animation == "y":
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=-1)
    ani.save('video.mp4')

plt.show()


