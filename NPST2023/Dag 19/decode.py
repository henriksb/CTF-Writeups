import ast

def decode_message_from_file(code_file, text_file):
    with open(code_file, 'r') as file:
        indices = ast.literal_eval(file.read())

    with open(text_file, 'r') as file:
        text = file.read()

    return ''.join(text[i] for i in indices)

decoded_message = decode_message_from_file('code', 'nissetekst')
print(decoded_message)
