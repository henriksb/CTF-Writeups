# Verify
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

You can download the challenge files here:
[challenge.zip](https://artifacts.picoctf.net/c_rhea/11/challenge.zip)

Additional details will be available after launching your challenge instance.

## Solution
Instead of looking through the code or thinking logically about the challenge, I decided to bruteforce it with the following command:

```sh
for file in files/*; do ./decrypt.sh "$file"; done
```
This didn't take long at all. There are not many files in the "files" directory.

picoCTF{trust_but_verify_8eee7195}
