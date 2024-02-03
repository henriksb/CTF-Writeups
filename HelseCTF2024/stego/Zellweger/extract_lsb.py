from PIL import Image
import numpy as np

def extract_following_bits(lsb_string, sequence_length=10):
    """Hent binærteksten som inneholder flagget.
        Dette må bli konvertert fra decabit til tekst
        for å få flagget. https://www.dcode.fr/decabit-code"""
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
    # piksel er en tupple med (R, G, B), vi må få LSB fra hver del
    return (pixel[0] & 1, pixel[1] & 1, pixel[2] & 1)


img_path = 'zellweger.png'
img = Image.open(img_path)

img_data = np.array(img)

# Ekstraher LSB fra hele bildet
lsb_data = np.apply_along_axis(extract_lsb, 2, img_data)

# Siden bildet kan være stort, og vi ønsker og returnere en tekstbasert representasjon,
# må vi flate ut lsb_data og konvertere den til en streng med 0-er og 1-ere.
# Så setter vi sammen LSB-ene for R,G,B for hver piksel.
lsb_flat = lsb_data.flatten()
lsb_str = ''.join(map(str, lsb_flat))

# Korter ned på den enorme mengden data
binary = lsb_str[0:27000]

print(extract_following_bits(binary))
