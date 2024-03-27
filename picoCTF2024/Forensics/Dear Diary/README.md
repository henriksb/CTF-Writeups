# Dear Diary

If you can find the flag on this disk image, we can close the case for good!
Download the disk image [here](https://artifacts.picoctf.net/c_titan/63/disk.flag.img.gz).

## Solution
This task can be solved using Autopsy, but for some reason I could not solve it on my Ubuntu/Windows machine. Only the Kali version of Autopsy could solve it.

The important file is "innocuous-file.txt". If you run strings on the entire disk image `strings disk.flag.img | grep innocuous`, you can see that there are a lot of files with the name "innocuous-file.txt". This is the only file that has several copies. If you open the disk image with Autopsy on Kali, and search for the file, you can see all the files. Open each individually and combine them to get the flag.

picoCTF{1_533_n4m35_80d24b30}
