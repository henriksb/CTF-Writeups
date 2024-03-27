# endianess-v2
Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.

Download it [here](https://artifacts.picoctf.net/c_titan/36/challengefile) and see what you can get out of it

## Solution

In this challenge, we are tasked with changing the endianess of a file. To do this, I used a command from the following [stackexchange](https://unix.stackexchange.com/questions/239543/is-there-a-oneliner-that-converts-a-binary-file-from-little-endian-to-big-endian) answer.


`hexdump -v -e '1/4 "%08x"' -e '"\n"' challengefile | xxd -r -p > out`

This gave me the following image:

![image](out)


picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_b039bc14}
