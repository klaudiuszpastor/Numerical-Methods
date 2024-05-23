import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Macierz maski / filtru
filtr = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Wczytanie i przygotowanie obrazu
image = Image.open('obraz.jpg').convert("L")  # grayscale
image = image.resize(size=(682, 682))
img_array = np.array(image)

# Funkcja konwolucji iteracyjnej
def konwolucja_iter(obraz, macierz):
    size = obraz.shape[0] - macierz.shape[0] + 1
    k = macierz.shape[0]
    convolved_img = np.zeros(shape=(size, size))
    for i in range(size):
        for j in range(size):
            mat = obraz[i:i+k, j:j+k]
            pixel = np.sum(np.multiply(mat, filtr))
            if pixel > 0:
                convolved_img[i, j] = pixel
            else:
                convolved_img[i, j] = 0
    return convolved_img

# Funkcja konwolucji w dziedzinie częstotliwości
def konwolucja_fft(obraz, macierz):
    size = obraz.shape[0] - macierz.shape[0] + 1
    convolved_img = np.fft.fft2(obraz, s=(size, size)) * np.fft.fft2(macierz, s=(size, size))
    convolved_img = np.fft.ifft2(convolved_img).real
    return convolved_img

# Wykonanie konwolucji iteracyjnej
img_conv_iter = konwolucja_iter(img_array, filtr)

# Wykonanie konwolucji w dziedzinie częstotliwości
img_conv_fft = konwolucja_fft(img_array, filtr)

# Wyświetlanie wyników
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Oryginalny obraz')

plt.subplot(1, 3, 2)
plt.imshow(img_conv_iter, cmap='gray')
plt.title('Konwolucja iteracyjna')

plt.subplot(1, 3, 3)
plt.imshow(img_conv_fft, cmap='gray')
plt.title('Konwolucja FFT')

plt.show()
