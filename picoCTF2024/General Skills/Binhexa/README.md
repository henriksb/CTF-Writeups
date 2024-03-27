# binhexa
How well can you perfom basic binary operations?
Start searching for the flag here nc titan.picoctf.net 50971

## Solution
This is a simple binary operation challenge. We receive two binary numbers and have to calculate the answers using different binary operations. I made a simple python script to enter the values and provide me with the answers:

```python
import sys

def binary_operations(bin1, bin2):
    # Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)

    # Perform the operations
    multiply = num1 * num2
    add = num1 + num2
    left_shift_num1 = num1 << 1
    right_shift_num1 = num2 >> 1
    and_operation = num1 & num2
    or_operation = num1 | num2

    # Print results in binary format
    print(f"{bin1} * {bin2} = {bin(multiply)} {hex(multiply)}")
    print(f"{bin1} + {bin2} = {bin(add)} {hex(add)}")
    print(f"{bin1} << 2 = {bin(left_shift_num1)} {hex(left_shift_num1)}")
    print(f"{bin1} >> 2 = {bin(right_shift_num1)} {hex(right_shift_num1)}")
    print(f"{bin1} & {bin2} = {bin(and_operation)} {hex(and_operation)}")
    print(f"{bin1} | {bin2} = {bin(or_operation)} {hex(or_operation)}")

binary_operations(sys.argv[1], sys.argv[2])
```

Completing these calculations revealed the flag:

picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6ab1ad84}
