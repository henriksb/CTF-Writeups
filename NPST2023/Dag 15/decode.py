from collections import Counter
import os
import hashlib

def MD5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('latin-1'))
    return m.hexdigest()

def read_file_content(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        return file.read()

def main(extract_path):
    backup_files = os.listdir(extract_path)

    file_contents = []
    for file in backup_files:
        content = read_file_content(os.path.join(extract_path, file))
        file_contents.append(content)

    max_length = 0
    for content in file_contents:
        if len(content) > max_length:
            max_length = len(content)

    common_chars_max_length = []
    for i in range(max_length):
        position_chars = []
        for content in file_contents:
            if i < len(content):
                if content[i].lower() not in "{}#$[]§¤@":
                    position_chars.append(content[i])
        most_common_char = Counter(position_chars).most_common(1)
        common_chars_max_length.append(most_common_char[0][0])

    reconstructed_string = "".join(common_chars_max_length)

    return reconstructed_string

if __name__ == "__main__":
    result = main("backups")
    with open("output.txt", "w", encoding="latin-1") as w:
        w.write(result)
    print("PST{" + MD5(result) + "}")
    
