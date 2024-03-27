# Binary Search
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.

Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!
You can download the challenge files here:

[challenge.zip](https://artifacts.picoctf.net/c_atlas/5/challenge.zip)

Additional details will be available after launching your challenge instance.

## Solution

With 10 tries, the number can always be guessed. Start at 500 and half/double difference until the correct number is found. I did not even bother looking into the code, and just used this technique.

picoCTF{g00d_gu355_3af33d18}
