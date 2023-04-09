import cv2
import numpy as np
from matplotlib import pyplot as plt

def perataanHistogram(A):
    nilai_bin = 255 #angka value pixel maximal!
    A = A+1 #agar terhindari dari pixel bernilai 0
    [frekuensi,value] = np.histogram(A,bins=nilai_bin) #langkah 2
    cumulatif_histogram = frekuensi.cumsum() #langkah 3
    [baris,kolom] = A.shape
    probabilty_frekuensi = np.round((cumulatif_histogram/float(A.size))*nilai_bin) #langkah 4 dan 5
    B = np.empty(A.shape)
    for i in range(0,baris):
        for j in range(0,kolom):
            B[i,j] = probabilty_frekuensi[A[i,j]-1] #langkah 6
    return B

I = cv2.imread('parrot_color.jpg')
gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #ubah ke format gray
hasil = perataanHistogram(gray)
plt.figure('Hasil Histogram Equalization')
plt.subplot(1,2,1),plt.imshow(gray,cmap='gray'),plt.title('gray')
plt.subplot(1,2,2),plt.imshow(hasil,cmap='gray'),plt.title('Histogram Equalization')
plt.show()

plt.figure('Histogram Citra Asli')
plt.hist(gray.ravel(), 256, [0, 256]);
plt.title('Histogram Citra Asli')
plt.show()

plt.figure('Histogram Citra Hasil Equalization')
plt.hist(hasil.ravel(), 256, [0, 256]);
plt.title('Histogram Equalization')