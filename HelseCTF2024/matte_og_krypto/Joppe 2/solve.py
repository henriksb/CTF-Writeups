import sympy as sp

# The provided parts of the secret
parts = [
    (4745696227450807, 655305480794027129181307180701455045712682321660286466368078),
    (2588682506107567, 655305480793967733879479427128553132958736140573542016023878),
    (4035090358829972, 655305480794003703185282913192696782073761367365025193477153)
]

# Lagrange Interpolation to find the polynomial
x = sp.symbols('x')
polynomial = sum([y * sp.prod([(x - xj) / (xi - xj) for xj in [part[0] for part in parts if part[0] != xi]]) for xi, y in parts])

# Simplify the polynomial
simplified_polynomial = sp.simplify(polynomial)

# Evaluate the polynomial at x = 0 to find the secret
secret = simplified_polynomial.subs(x, 0)

def number_to_text(number):
    """ Convert a large number into a string assuming it's ASCII encoded """
    text = ""
    while number > 0:
        # Extract the least significant byte (8 bits)
        byte = number & 0xff
        # Convert the byte to a character and prepend it to the text
        text = chr(byte) + text
        # Shift the number 8 bits to the right
        number >>= 8
    return text

# Convert the number to text
decoded_text = number_to_text(secret)
print(decoded_text)
