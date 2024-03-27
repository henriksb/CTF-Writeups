# SansAlpha
The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols.
Additional details will be available after launching your challenge instance.

## Solution

We quickly found the flag located at `*/*` (blargh/flag.txt). The problem was that we could not print it. We started looking around the filesystem to find useful files using `???/???`.

I realized that base64 would print the output of the file, but when trying to run `/???/????64 */*` (/bin/base64 blargh/flag.txt) I would get the error "/bin/base64: extra operand ‘/bin/x86_64’". Then, I went on my own terminal and looked at the output:

```sh
henrik@henrik: echo /???/????64
>> /bin/base64 /bin/wine64 /bin/x86_64
```

There are three files that match the wildcard. This means that we have to select the first one, and ignore the rest. To do this, I made a variable. I tried using numbers as the variable name, but that didn't work. I also tried using special characters (æ,ø,å), but they did not work either. Finally, I tried "_1", which worked.

`_1=( /???/????64 )`

Now, I had the paths stored in a variable. Next, I had to select the first element and use it on the flag.

`"${_1[0]}" */????.???`

cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV83NzVhYzEyZH0=

return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_775ac12d}
