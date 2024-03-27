# packer
Reverse this linux executable?
[binary](https://artifacts.picoctf.net/c_titan/21/out)

Hint: What can we do to reduce the size of a binary after compiling it.

## Solution

When trying to run the program, we have to enter a password to get the flag. Running commands such as `strings` does not reveal the flag. This is because the binary file is compressed, practically making all data unreadable. However, we can see a very important keyword at the very end of the `strings` command, which is "UPX!". UPX is a compression software. To solve the challenge, decompress the program using the following command:

`upx -d out -o out_unpacked`

Now, if we try to run `strings`, we get the flag:

`Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d`

Use a HEX to text converter and we get the flag:

picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_371aa9ff}
