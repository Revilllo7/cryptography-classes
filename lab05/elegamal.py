#Autor: Oliver Gruba
import argparse

import sys
from logic.key import read_elgamal, generate_keys, save_key, read_key
from logic.encrypt import encrypt
from logic.decrypt import decrypt
from logic.signature import sign
from logic.verify import verify
from logic.message import read_message

def main():
    parser = argparse.ArgumentParser(description="ElGamal encryption and decryption")
    parser.add_argument("-k", "--key", action="store_true", help="Generate a new key")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt a message")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt a message")
    parser.add_argument("-s", "--signature", action="store_true", help="Sign a message")
    parser.add_argument("-v", "--verify", action="store_true", help="Verify a signature")

    args = parser.parse_args()

    if args.key:
        p, g = read_elgamal('elegamal.txt')
        x, y = generate_keys(p, g)
        save_key('private.txt', p, g, x)
        save_key('public.txt', p, g, y)
    
    if args.encrypt:
        p, g, y = read_key('public.txt')
        m = read_message('plain.txt')
        c1, c2 = encrypt(p, g, y, m)
        with open('crypto.txt', 'w') as f:
            f.write(f"{c1}\n{c2}\n")
    
    if args.decrypt:
        p, g, x = read_key('private.txt')
        with open('crypto.txt', 'r') as f:
            c1 = int(f.readline().strip())
            c2 = int(f.readline().strip())
        m = decrypt(p, x, c1, c2)
        with open('decrypt.txt', 'w') as f:
            f.write(f"{m}\n")
    
    if args.signature:
        p, g, x = read_key('private.txt')
        m = read_message('message.txt')
        r, s = sign(p, g, x, m)
        with open('signature.txt', 'w') as f:
            f.write(f"{r}\n{s}\n")
    
    if args.verify:
        p, g, y = read_key('public.txt')
        m = read_message('message.txt')
        with open('signature.txt', 'r') as f:
            r = int(f.readline().strip())
            s = int(f.readline().strip())
        is_valid = verify(p, g, y, m, r, s)
        result = 'T' if is_valid else 'N'
        print(result)
        with open('verify.txt', 'w') as f:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()