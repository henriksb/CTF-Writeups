import sympy as sp
from Crypto.Util.number import long_to_bytes

hemmeligheter = [
    (4745696227450807, 655305480794027129181307180701455045712682321660286466368078),
    (2588682506107567, 655305480793967733879479427128553132958736140573542016023878),
    (4035090358829972, 655305480794003703185282913192696782073761367365025193477153)
]

# Lagrange Interpolation to find the polynomial
x = sp.symbols('x')
polynomial = sum([y * sp.prod([(x - xj) / (xi - xj) for xj in [h[0] for h in hemmeligheter if h[0] != xi]]) for xi, y in hemmeligheter])

# Simplify the polynomial
simplified_polynomial = sp.simplify(polynomial)

# Evaluate the polynomial at x = 0 to find the secret
secret = simplified_polynomial.subs(x, 0)


# Convert the number to text
decoded_text = long_to_bytes(secret)
print(decoded_text)
