# Blast from the past
The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?
Set the timestamps on this picture to 1970:01:01 00:00:00.001+00:00 with as much precision as possible for each timestamp. In this example, +00:00 is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: 1969:12:31 19:00:00.001-05:00. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.

Use this [picture](https://artifacts.picoctf.net/c_mimas/74/original.jpg).

Additional details will be available after launching your challenge instance.

## Solution
This challenge was strange, but not very difficult. Exiftool can change metadata for most files, but cannot change all tags.

For changing the first 6 tags, the following commands were used:
```
exiftool "-ModifyDate=1970:01:01 00:00:00.001+00:00" original.jpg
exiftool "-DateTimeOriginal=1970:01:01 00:00:00.001+00:00" original.jpg
exiftool "-CreateDate=1970:01:01 00:00:00.001+00:00" original.jpg
exiftool "-SubSecCreateDate=1970:01:01 00:00:00.001" original.jpg
exiftool "-SubSecDateTimeOriginal=1970:01:01 00:00:00.001" original.jpg
exiftool "-SubSecModifyDate=1970:01:01 00:00:00.001" original.jpg
```

For the very last tag, I had to manually change the tag in a HEX editor. The "Time Stamp" tag is stored in Epoch time, and the number is seconds since 1970:01:01 00:00:00. To find the variable in the HEX editor, simply convert the time in "Time Stamp" to Epoch time and search for it. Then, change the number to "1".

picoCTF{71m3_7r4v311ng_p1c7ur3_b5f7bcb5}

