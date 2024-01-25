def is_valid_word(word, patterns):
    if len(word) != len(patterns):
        return False
    return all(word[i] == patterns[i] for i in range(len(word)))

def main():
    # Patterns from your list
    patterns = ['fdaj', 'eiqu', 'd', 'ldg', 'halk', 'oier', 'tu', 'eqiu', 'sd', 'teor']

    # Adjust the patterns to be the exact length of 11 by repeating characters if needed
    patterns = [p[min(i, len(p) - 1)] for i, p in enumerate(patterns)]

    # Read the wordlist with the specified encoding
    with open('Ordliste/boying_grupper.txt', 'r', encoding="ISO-8859-1") as file:
        words = file.read().splitlines()

    # Filter the words
    valid_words = [word for word in words if is_valid_word(word, patterns)]

    # Print the valid words
    for word in valid_words:
        print(word)
    
if __name__ == "__main__":
    main()
