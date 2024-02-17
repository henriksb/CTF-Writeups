# Cosmic Caesar
While traveling through the debris of exploded planets, a signal arrived. We've determined the alien alphabet used, but the message is still encrypted. Your mission is to decrypt the secret message.

## Filer
encrypt.py \
flag.txt.enc

## Løsning
Reverser scriptet og bruk det på den krypterte filen. Scriptet shifter annenhver bokstav med +3 eller -3. Den eneste delen som trenger å bli endret på er den følgende:

```python
if idx % 2 == 0:
    flag_enc += alphabet[(alphabet.index(char)+3) % len(alphabet)]
else:
    flag_enc += alphabet[(alphabet.index(char)-3) % len(alphabet)]
```

som blir endret til:

```python            
if idx % 2 == 0:
    flag_dec += alphabet[(alphabet.index(char)-3) % len(alphabet)]
else:
    flag_dec += alphabet[(alphabet.index(char)+3) % len(alphabet)]
```

`UiTHack24{1nt3rg4lact1c_ca3s4r}`