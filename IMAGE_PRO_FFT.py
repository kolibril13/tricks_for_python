# import numpy as np
# import matplotlib.pyplot as plt
# pixel=30
# img = np.fromfunction(lambda u,v: np.sin(u)+np.cos(v) ,(pixel,pixel))
#
# print(img)
# fourier= np.fft.fft2(img)
# fourier_s=np.fft.fftshift(fourier)
# print(fourier)
# plt.subplot(1,2,1)
# plt.imshow(img)
# plt.subplot(1,2,2)
# plt.imshow(abs(fourier_s))
# plt.show()
# magnitude_spectrum = 20*np.log(np.abs(F2))
# b.pltx(bw_img,magnitude_spectrum)





import numpy as np
import matplotlib.pyplot as plt
pixels=30
k_fr1_ar= np.uint8(np.fromfunction(lambda i, j: 0 +i*0, (pixels, pixels)))
k_fr1_ar[10,10]=255
#
k_fr1_ar_shift= np.fft.ifftshift(k_fr1_ar)
real_out_ar =  np.fft.ifft2(k_fr1_ar_shift)

plt.subplot(121)
plt.imshow(k_fr1_ar)


plt.subplot(122)
plt.imshow(np.uint8(real_out_ar.real))
plt.show()