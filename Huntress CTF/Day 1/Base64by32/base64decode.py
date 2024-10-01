# -*- coding: utf-8 -*-
import base64

with open("base64by32", "r") as b:
    b = b.read().encode("ascii")
    
    
for i in range(0, 32):
    b = base64.b64decode(b)
    
print(b)
    