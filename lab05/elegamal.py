#Autor: Oliver Gruba
import argparse

def main():
    parser = argparse.ArgumentParser(description="ElGamal encryption and decryption")
    parser.add_argument("-k", "--key", action="store_true", help="Generate a new key")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt a message")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt a message")
    parser.add_argument("-s", "--signature", action="store_true", help="Sign a message")
    parser.add_argument("-v", "--verify", action="store_true", help="Verify a signature")

    if args.key:
        # 
    
    if args.encrypt:
        #
    
    if args.decrypt:
        #
    
    if args.signature:
        #
    
    if args.verify:
        #

if __name__ == "__main__":
    main()