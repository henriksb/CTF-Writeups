import numpy as np
from PIL import Image

img_path = "blabr.png"
blueberry_img = Image.open(img_path)
blueberry_data = np.array(blueberry_img)

ft_blueberry = np.fft.fft2(blueberry_data)
fshift_blueberry = np.fft.fftshift(ft_blueberry)

def high_pass_filter_mask(size, cutoff):
    mask = np.ones(size, dtype=bool)
    center = np.array(size) // 2
    x, y = np.ogrid[:size[0], :size[1]]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= cutoff**2
    mask[mask_area] = False
    return mask

cutoff = 6
hp_filter = high_pass_filter_mask(blueberry_data.shape, cutoff)
hp_fshift = fshift_blueberry * hp_filter

inv_hp_img = np.fft.ifft2(np.fft.ifftshift(hp_fshift))
inv_hp_img = np.abs(inv_hp_img)

# Increase brightness
brightness_factor = 20  # Adjust this value to control brightness
inv_hp_img_bright = np.clip(inv_hp_img * brightness_factor, 0, 255)

Image.fromarray(inv_hp_img_bright.astype(np.uint8)).save("blåbær.png")

