# Mob psycho
Can you handle APKs?
Download the android apk [here](https://artifacts.picoctf.net/c_titan/52/mobpsycho.apk).

## Solution

In this challenge, we are tasked with finding the flag in an APK file. The APK file contains a large amount of files and content, so manually looking through the files would take a long time. To find the flag, I used the following commands:

```sh
aapt list mobpsycho.apk | grep flag
> res/color/flag.txt
```
With this command, I found the flag file. Now we have to extract it. To do that, use the following command:

```
unzip mobpsycho.apk res/color/flag.txt -d flag
```
This is the content of the file:

```
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f38356462643231357d
```

Convert from HEX to text:

picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_85dbd215}
