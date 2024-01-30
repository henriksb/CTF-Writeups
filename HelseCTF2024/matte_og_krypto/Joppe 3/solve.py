import sympy as sp
from Crypto.Util.number import long_to_bytes

def utregning(X=0):
    hemmeligheter = [
        (2344332245, 65530548079400370318528292311996782073761367365025193477153),
        (13429121073, 362422730191176971056722614457277134831341186224587467857920),
        (23429121073, 611905828855656382575774271667026570700762200408325616089780),
    ]

    # Lagrange Interpolation to find the polynomial
    x = sp.symbols('x')
    polynomial = sum([y * sp.prod([(x - sp.Rational(xj)) / (sp.Rational(xi) - sp.Rational(xj)) 
                    for xj in [h[0] for h in hemmeligheter if h[0] != xi]]) 
                    for xi, y in hemmeligheter])

    # Expand the polynomial (alternative to simplify for performance)
    expanded_polynomial = sp.expand(polynomial)

    # Evaluate the polynomial at x = 0 to find the secret and ensure it's an integer
    secret = expanded_polynomial.subs(x, X)

    return secret


x = long_to_bytes(utregning())
print(x)

x_number = int(x.decode("utf-8")[2:])
flagg = utregning(x_number)
print(long_to_bytes(flagg))