# Base64by32
This is a dumb challenge. I'm sorry.

## Solution
In this challenge, we get a large base64 encoded string. Considering the title of the challenge, it seems like we have to decode base64 32 times, which is the solution.

To solve it, I created a python script:

```python
import base64

with open("base64by32", "r") as b:
    b = b.read().encode("ascii")  
    
for _ in range(32):
    b = base64.b64decode(b)
    
print(b)
```