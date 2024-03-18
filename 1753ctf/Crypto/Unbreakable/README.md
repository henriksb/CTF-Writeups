# 🔗 Unbreakable (Score: 170 / Solves: 33)
Me: Is one-time-pad unbreakable?

Chat GPT: Yes, Your Awesomeness, a one-time pad is theoretically unbreakable when used correctly. This is because each bit of plaintext is encrypted with a completely random bit of the key, and each key is used only once, making it impossible to derive the original message without the exact key.

Me: Okay, let's get that completely random bits!
 
https://dl.1753ctf.com/unbreakable/enc.cs?s=FhCZiB1l

## Solution

In this challenge, we received a C# file which was used to encrypt a string. There is, however, a big flaw with the encryption. It uses the current date to encrypt the string, as you can see in the script.

```csharp
var seed = new DateTimeOffset(DateTime.Today).ToUnixTimeSeconds();
var random = new Random((int)seed);

var randomBuffer = new byte[flag.Length];
random.NextBytes(randomBuffer);

var flagBuffer = Encoding.ASCII.GetBytes(flag);
var resultBuffer = new byte[flag.Length];

for (var i = 0; i < flag.Length; i++)
    resultBuffer[i] = (byte)(randomBuffer[i] ^ flagBuffer[i]);

var encrypted = string.Concat(resultBuffer.Select(x => x.ToString("X").PadLeft(2, '0')));

Console.WriteLine(encrypted); // 22ECCDB90936D5C2454A65A5BB4C120FB1C8567381C6DB368EB57D4C6BE8B6D8C860E5C6FAC1F48BF2291A5C9EA3C354715857E7
```

To reverse this, I made a new script to reverse this. I manually tried different days until I finally found that it was -19 (this script will not currently work, you will probably have to bruteforce previous days).

```csharp
using System;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {
        var encryptedHex = "22ECCDB90936D5C2454A65A5BB4C120FB1C8567381C6DB368EB57D4C6BE8B6D8C860E5C6FAC1F48BF2291A5C9EA3C354715857E7";
        // Adjust the seed to be based on a previous date
        var seed = new DateTimeOffset(DateTime.Today.AddDays(-19)).ToUnixTimeSeconds();
        var random = new Random((int)seed);

        // Convert the encrypted hex string back to byte array
        var encryptedBytes = Enumerable.Range(0, encryptedHex.Length)
                             .Where(x => x % 2 == 0)
                             .Select(x => Convert.ToByte(encryptedHex.Substring(x, 2), 16))
                             .ToArray();

        var randomBuffer = new byte[encryptedBytes.Length];
        random.NextBytes(randomBuffer);

        var decryptedBytes = new byte[encryptedBytes.Length];

        // XOR operation to decrypt
        for (var i = 0; i < encryptedBytes.Length; i++)
            decryptedBytes[i] = (byte)(encryptedBytes[i] ^ randomBuffer[i]);

        var decrypted = Encoding.ASCII.GetString(decryptedBytes);
        Console.WriteLine(decrypted);
    }
}
```

1753c{you_will_never_guess_the_flag_coz_i_am_xorrro}
