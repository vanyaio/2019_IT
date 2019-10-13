import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return

def gauss_fn(i, j, sigma):
    return np.exp(-(i*i + j*j) / 2 * sigma * sigma) / (sqrt(2 * np.pi) * sigma)

def get_kernel(window_size, sigma=1):
    kernel = np.zeros((window_size, window_size))
    mean = window_size // 2

    for x in range(window_size):
        for y in range(window_size):
            kernel[x][y] = gauss_fn(x - mean, y - mean, sigma)

    kernel /= kernel.sum()
    return kernel

def filter(img, window_size=3):
    img2 = np.zeros_like(img)
    kernel = get_kernel(window_size)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2



def main():
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img)

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()
