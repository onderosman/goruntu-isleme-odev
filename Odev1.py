import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./kedi.jpg")
shape = image.shape
cv2.imshow('image', image)


l = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('l', l)


Hist = np.zeros(shape=(256))
for v in range(shape[0]):
    for u in range(shape[1]):
        i = l[v,u]
        Hist[i] = Hist[i]+1


plt.plot(Hist)
plt.show()
