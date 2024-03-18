using System;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {
        var encryptedHex = "22ECCDB90936D5C2454A65A5BB4C120FB1C8567381C6DB368EB57D4C6BE8B6D8C860E5C6FAC1F48BF2291A5C9EA3C354715857E7";
        // Adjust the seed to be based on yesterday's date
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
