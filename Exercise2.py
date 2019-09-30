import matplotlib.pyplot as plt
import numpy as np

def add_noise(img1,rate=5):
    img1[::rate,::rate,:]=1
    return

def getkernel (sigma,size):
    p=size//2
    kernel=np.ones((size,size))
    for i in range(size):
        for j in range(size):
            kernel[i,j]=np.e**(-((i-p)**2+(j-p)**2)/(2*(sigma**2)))
    return kernel/np.sum(kernel)

def gauss(getkernel,img,sigma=3,size=5):
    img2=np.zeros_like(img)
    p=size//2
    kernel=getkernel(sigma,size)
    for k in range(img.shape[2]):
        for i in range(p,img.shape[0]-p):
            for j in range(p,img.shape[1]-p):
                window=img[i-p:i+p+1,j-p:j+p+1,k]
                img2[i,j,k]=(window*kernel).sum()
    return img2

img1=plt.imread("cat.png") [:,:,:3]
add_noise(img1)
img2=gauss(getkernel,img1)


plt.subplot(1,2,1)
plt.imshow(img1)

plt.subplot(1,2,2)
plt.imshow(img2)

plt.show()
