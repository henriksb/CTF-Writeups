import numpy as np
from PIL import Image

img_path = "ekorn.png"
img = Image.open(img_path).convert("L")
img_data = np.array(img)

ft = np.fft.fft2(img_data)
fshift = np.fft.fftshift(ft)
spectrum = np.log(np.abs(fshift))

im = Image.fromarray(spectrum.astype(np.uint8))
im.save("flagg.png")
