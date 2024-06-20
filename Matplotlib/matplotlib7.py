import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

img = mpimg.imread('/home/hp/Pictures/Screenshot from 2022-10-16 10-27-03.png')
plt.imshow(img)
plt.show()

imgcv2 = cv2.imread('/home/hp/Pictures/Screenshot from 2022-10-16 10-27-03.png')
imgcv2 = cv2.cvtColor(imgcv2, cv2.COLOR_BGR2RGB)    #for open cv we need image in rgb format so need to convert from bgr to rgb
plt.imshow(imgcv2)
plt.show()

#changing aspect
plt.imshow(img, aspect = 0.5)
plt.colorbar()
plt.show()

plt.imshow(img, cmap='gray')    #cmap for different color bars.
plt.colorbar()
plt.show()