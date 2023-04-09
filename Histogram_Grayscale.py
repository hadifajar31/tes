import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('parrot_grayscale.jpg', 0)
plt.hist(img.ravel(), 256, [0, 256]);
plt.title('Histogram Grayscale')
plt.show()