import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

save_animation = "n"

pixel = 20
start_frames = 0
total_frames = 2 * start_frames + pixel

fig = plt.figure(num=None, figsize=(16, 9), dpi=100, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

title = ax1.text(0.5, 0.85, "", bbox={'facecolor': 'w', 'alpha': 0.5, 'pad': 5},
                 transform=ax1.transAxes, ha="center")

ax1.axis('off')
ax2.axis('off')
ima = ax1.imshow(np.zeros((pixel, pixel)), animated=True, interpolation='none', cmap='gray')
imb = ax2.imshow(np.zeros((pixel, pixel)), animated=True, interpolation='none', cmap='gray')

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

i = 0;
k = 0


def updatefig(*args):
    global i, k
    i += 1
    print(k, i)
    fourier_img = np.zeros((pixel, pixel))
    if i >= start_frames:
        k += 1
    if k > pixel - 1:
        k = pixel - 1
    fourier_img[k, k] = 1
    real_img = np.fft.ifft2(np.fft.ifftshift(fourier_img)).real
    ima.set_array(fourier_img)
    imb.set_array(real_img)
    ima.set_clim(0, np.max(fourier_img))
    imb.set_clim(np.min(real_img), np.max(real_img))
    title.set_text('Iteration=' + str(i) + "\t".expandtabs() + "Pixel =" + str(k))
    return ima, imb, title


ani = animation.FuncAnimation(fig, updatefig, blit=True, interval=50, save_count=total_frames)
if save_animation == "y":
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=-1)
    ani.save('video.mp4')

plt.show()