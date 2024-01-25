import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_path = "ekorn.png"
img = Image.open(img_path).convert('L')  # konverter til gråskala
img_data = np.array(img)

ft = np.fft.fft2(img_data)

fshift = np.fft.fftshift(ft)

spectrum = np.log(np.abs(fshift))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Orginalt bilde
ax1.imshow(img_data, cmap="gray")
ax1.set_title("Orginalt bilde")
ax1.axis("off")

# Magnitude spectrum
ax2.imshow(spectrum, cmap="gray")
ax2.set_title("Magnitude Spectrum")
ax2.axis("off")

plt.show()
