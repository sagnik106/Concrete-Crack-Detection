import cv2
import numpy as np
import matplotlib.pyplot as plt

def convolution(image, kernel):
    k_size=kernel.shape[0]
    image_size=image.shape
    n_img=np.zeros((image_size[0]+2,image_size[1]+2))
    n_img[1:-1,1:-1]=image[:,:]
    image=n_img
    del n_img
    l=list()
    for i in range(k_size):
        for j in range(k_size):
            l.append(image[i:-(k_size)+i,j:-(k_size)+j]*kernel[-i-1][-j-1])
    return sum(l)
def correlation(image, kernel):
    k_size=kernel.shape[0]
    image_size=image.shape
    n_img=np.zeros((image_size[0]+2,image_size[1]+2))
    n_img[1:-1,1:-1]=image[:,:]
    image=n_img
    del n_img
    l=list()
    for i in range(k_size):
        for j in range(k_size):
            l.append(image[i:-(k_size)+i,j:-(k_size)+j]*kernel[i][j])
    return sum(l)
