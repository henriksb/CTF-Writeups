import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_path = "blabr.png"
blueberry_img = Image.open(img_path).convert('L') 
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

cutoffs = [3, 4, 5, 6, 7]
filtered_images = []

for cutoff in cutoffs:
    hp_filter = high_pass_filter_mask(blueberry_data.shape, cutoff)
    hp_fshift = fshift_blueberry * hp_filter
    
    inv_hp_img = np.fft.ifft2(np.fft.ifftshift(hp_fshift))
    inv_hp_img = np.abs(inv_hp_img)
    
    filtered_images.append(inv_hp_img)

fig, axes = plt.subplots(1, len(cutoffs) + 1, figsize=(20, 10))

axes[0].imshow(blueberry_data, cmap="gray")
axes[0].set_title("Originalt bilde")
axes[0].axis('off')

for i, img in enumerate(filtered_images, start=1):
    axes[i].imshow(img, cmap='gray')
    axes[i].set_title(f'(cutoff={cutoffs[i-1]})')
    axes[i].axis('off')

plt.show()
