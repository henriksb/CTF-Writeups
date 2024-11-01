# OceanLocust
Wow-ee zow-ee!! Some advanced persistent threats have been doing some tricks with hiding payloads in image files!

We thought we would try our hand at it too.

NOTE: this challenge includes a debug build of the binary used to craft the image, as well as a release build... so you may choose to go an easier route or a harder route ;)

## Solution
In this task, we received two executable files, `png-challenge.exe`, `png-challenge-debug.exe`, and one image `inconspicuous.png`. When running this program with a command like: `./png-challenge.exe image.png 1234567`, it will encode the message `1234567` into a new file called `encoded image.png`. The task is to figure out the message that is encoded in the image we received. The program does not have a function to decode the encoded message.

My solution for the task was to anylyze the output of images encoded with different messages. The first thing I noticed was the pattern of `biTx`, where the `x` is a letter from a-g. This can be seen in a HEX editor like HxD. I decided to encode single letters, extract the `biT` chunks to find a pattern.

When running `png-challenge.exe test.png aaaaaaa` (the program errors if we encode less than 7 characters), the chunks looked like this:

```python
[('biTa', b'F'), ('biTb', b'F'), ('biTc', b'F'), ('biTd', b'F'), ('biTe', b'F'), ('biTf', b'F'), ('biTg', b'F')]
```
It looks like the character `a` is encoded into `b'F` each time, and the amount of `biTx` is equal to the length of the message. After running some more tests is seems like each character has it's own unique value after being encoded. I decided to generate a mapping of characters to see if I could decode the flag. This worked when decoding my own messages, but it did not work on the encoded flag.

I did some more testing and saw that after encoding 14 characters, things started to change. When encoding 13 characters, this is how the chunks look:

```python
[('biTa', b'\x03'), ('biTb', b'\x03'), ('biTc', b'\x03'), ('biTd', b'\x03'), ('biTe', b'\x03'), ('biTf', b'\x03'), ('biTg', b'\x03'), ('biTh', b'\x03'), ('biTi', b'\x03'), ('biTj', b'\x03'), ('biTk', b'\x03'), ('biTl', b'\x03'), ('biTm', b'\x03')]
```

But when encoding 14 characters, it looks like this:
```python
[('biTa', b'\x03\x08'), ('biTb', b'\x03\x08'), ('biTc', b'\x03\x08'), ('biTd', b'\x03\x08'), ('biTe', b'\x03\x08'), ('biTf', b'\x03\x08'), ('biTg', b'\x03\x08')]
```

Encoding 40 characers, it looks like this:
```python
[('biTa', b'\x03\x085\x00\x03'), ('biTb', b'\x03\x085\x03\x03'), ('biTc', b'\x03\x085\x02\x03'), ('biTd', b'\x03\x085\x05\x03'), ('biTe', b'\x03\x085\x04\x03'), ('biTf', b'\x03\x085\x07\x03'), ('biTg', b'\x03\x085\x06\x03'), ('biTh', b'\x03\x085\t\x03')]
```

There seems to be some pattern, but also a little bit "random". Only the letter "a" is encoded in these tests. It seems to change a little bit with length. But since each character only changes one byte in the encoding, and the change seems consistent if the length is the same, I knew I could guess the flag.

The flag had 40 bytes in total, so I started encoding 40 zeroes. Then I changed the 5 first bytes to `flag{` and compared it with the encoded flag. `biTa` was the same in both:

```python
[('biTa', b'\x04\x055\x06\x19')
```

This means that the first 5 characters were correct. Then I could slowly guess my way up to the final flag by encoding and comparing chunks.