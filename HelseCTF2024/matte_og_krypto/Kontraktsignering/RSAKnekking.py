from Crypto.Util.number import inverse, bytes_to_long

# Constants
N=0 # Fyll inn verdien av N
contract = b"Dette er en superviktig kontrakt for veeldig viktige ting med store ord og uforstaaelige kruseduller."
m1 = 17  # Tilfeldig nummer

# Kalkuler m2
m2 = bytes_to_long(contract) * inverse(m1, N) % N

# Kombinere de to signaturene
def combine_signatures(sig1, sig2, N):
    return (sig1 * sig2) % N

def main():
    # Konverter m1 og m2 til HEX
    print("m1 in hex:", hex(m1)[2:])
    print("m2 in hex:", hex(m2)[2:])

    # Hent og skriv inn signaturene
    sig_m1_hex = input("Skriv inn signatur for m1: ")
    sig_m2_hex = input("Skrif inn signatur for m2: ")

    # Konverter signaturene til HEX
    sig_m1 = int(sig_m1_hex, 16)
    sig_m2 = int(sig_m2_hex, 16)

    # Kombiner signatur
    combined_signature = combine_signatures(sig_m1, sig_m2, N)

    print("Kombibert signatur i HEX:", hex(combined_signature)[2:])

if __name__ == "__main__":
    main()
