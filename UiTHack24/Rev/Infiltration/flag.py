class Flag:
    str = ['x', 'D', 'y', 'e', 'L', 'N', 'F', 31, 25, 'V', 'z', 'E', 30, '_', 30, 'r', 28, 24, 'r', '@', 'T', 'r', 'N', 'X', ']', 'r', 29, 'K', 'r', 'G', 25, '[', 25, 18, 'P']

    @staticmethod
    def show():
        for i in range(35):
            # For characters in the array, convert them to their ASCII values before XOR
            # For numbers, use them directly
            char = Flag.str[i]
            if isinstance(char, str):
                print(chr(ord(char) ^ ord('-')), end='')
            else:
                print(chr(char ^ ord('-')), end='')

# Call the show method to display the result
Flag.show()