from PIL import Image
import numpy as np

def extract_following_bits(lsb_string, sequence_length=10):
    extracted_sequence = ""
    index = 0
    while index < len(lsb_string):
        index = lsb_string.find('1', index)
        if index == -1:
            break
        index += 1
        if index + sequence_length <= len(lsb_string):
            extracted_sequence += lsb_string[index:index + sequence_length] + " "
            index += sequence_length
        else:
            break
    return extracted_sequence

def extract_lsb(pixel):
    # pixel is a tuple with (R, G, B), we need to get the LSB from each component
    return (pixel[0] & 1, pixel[1] & 1, pixel[2] & 1)


img_path = 'zellweger.png'
img = Image.open(img_path)

img_data = np.array(img)

# Extract LSBs for the entire image
lsb_data = np.apply_along_axis(extract_lsb, 2, img_data)

# Since the image can be large, and we want to return a text-based representation,
# we'll need to flatten the lsb_data and convert it to a string of 0s and 1s.
# We'll concatenate the LSBs for R, G, B for each pixel.
lsb_flat = lsb_data.flatten()
lsb_str = ''.join(map(str, lsb_flat))

binary = lsb_str[0:27000]

print(extract_following_bits(binary))
