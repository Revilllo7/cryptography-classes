import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt a message using Ceaser or Affine cipher')
    parser.add_argument('-c', '--ceaser', help='Use Ceaser cipher', action='store_true')
    parser.add_argument('-a', '--affine', help='Use Affine cipher', action='store_true')
    parser.add_argument('-e', '--encrypt', help='Encrypt a message', action='store_true')
    parser.add_argument('-d', '--decrypt', help='Decrypt a message', action='store_true')
    parser.add_argument('-j', '--plaintext', help='cryptoanalysis based on plaintext')
    parser.add_argument('-k', '--cryptogram', help='cryptoanalysis based on cryptogram')
    args = parser.parse_args()

    if args.ceaser:
        print('ceaser')
        if args.encrypt:
            print('encrypt')
        elif args.decrypt:
            print('decrypt')
        elif args.plaintext:
            print('cryptoanalysis based on plaintext')
        elif args.cryptogram:
            print('cryptoanalysis based on cryptogram')
        else:
            print('Please select an action to perform')
    elif args.affine:
        print('affine')
        if args.encrypt:
            print('encrypt')
        elif args.decrypt:
            print('decrypt')
        elif args.plaintext:
            print('cryptoanalysis based on plaintext')
        elif args.cryptogram:
            print('cryptoanalysis based on cryptogram')
    else:
        print('Please select a cipher to use')

if __name__ == '__main__':
    main()

# we literally do nothing on these labs, oh my god, i am son done wiht life.