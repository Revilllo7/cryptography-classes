# Author: Oliver Gruba


import argparse
import os
import sys
import random

LINE_LENGTH = 64

# Define the file names for the different stages of the process
FILES = {
    "orig": "orig.txt",
    "plain": "plain.txt",
    "key": "key.txt",
    "crypto": "crypto.txt",
    "decrypt": "decrypt.txt",
}

def save_to_file(filename: str, data: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)



def read_from_file(filename: str) -> str:
    if not os.path.exists(filename):
        print(f"File {filename} not found. Creating an empty file. Please fill the file with data.")
        save_to_file(filename, "")
        sys.exit(1)
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()



def prepare():
    original = read_from_file(FILES["orig"]).replace("\r", "").replace("\n", " ").replace("  ", " ")
    lines = [original[i:i+LINE_LENGTH] for i in range(0, len(original) - LINE_LENGTH + 1, LINE_LENGTH)]
    save_to_file(FILES["plain"], "\n".join(lines))
    # generate a random key
    key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for _ in range(LINE_LENGTH))
    save_to_file(FILES["key"], key)



def encrypt():
    plain = read_from_file(FILES["plain"]).split("\n")
    key = read_from_file(FILES["key"])[:LINE_LENGTH].encode("utf-8")
    encrypted = []
    for line in plain:
        line_bytes = line.encode("utf-8")
        result = bytes([b ^ key[i % len(key)] for i, b in enumerate(line_bytes)])
        encrypted.append(result.hex())
    save_to_file(FILES["crypto"], "\n".join(encrypted))



def analysis():
    crypto_lines = read_from_file(FILES["crypto"]).split("\n")
    buffers = [bytes.fromhex(line) for line in crypto_lines]
    num_lines = len(buffers)
    line_length = len(buffers[0])
    key_guess = [None] * line_length
    threshold = int(num_lines * 0.6)
    for i in range(num_lines):
        space_votes = [0] * line_length
        for j in range(num_lines):
            if i == j:
                continue
            xor_line = bytes([buffers[i][k] ^ buffers[j][k] for k in range(line_length)])
            for k, ch in enumerate(xor_line):
                if (65 <= ch <= 90) or (97 <= ch <= 122):
                    space_votes[k] += 1

        for k in range(line_length):
            if space_votes[k] >= threshold and key_guess[k] is None:
                key_guess[k] = buffers[i][k] ^ 0x20

    decrypted = []
    for line in buffers:
        text = ""
        for i in range(line_length):
            if key_guess[i] is not None:
                ch = line[i] ^ key_guess[i]
                text += chr(ch) if 32 <= ch <= 126 else "_"
            else:
                text += "_"
        decrypted.append(text)
    save_to_file(FILES["decrypt"], "\n".join(decrypted))



def remove():
    for key in ["plain", "key", "crypto", "decrypt"]:
        try:
            os.remove(FILES[key])
        except FileNotFoundError:
            pass

def main():
    parser = argparse.ArgumentParser(description="XOR cipher tool")
    parser.add_argument("-p", "--prepare", action="store_true", help="Prepare text")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt a message")
    parser.add_argument("-k", "--analysis", action="store_true", help="Cryptanalysis of a cryptogram")
    parser.add_argument("-r", "--remove", action="store_true", help="Remove temporary files")

    args = parser.parse_args()
    if args.prepare:
        prepare()
    elif args.encrypt:
        encrypt()
    elif args.analysis:
        analysis()
    elif args.remove:
        remove()



if __name__ == "__main__":
    main()
