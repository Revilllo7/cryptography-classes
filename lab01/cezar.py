import argparse
from cipher import caesar_cipher, affine_cipher
from crypto_analysis import analyze_with_plaintext, analyze_without_plaintext
from files import read_file, write_file

def main():
    parser = argparse.ArgumentParser(description='Szyfrowanie i deszyfrowanie tekstu.')
    parser.add_argument('-c', action='store_true', help='Użyj szyfru Cezara')
    parser.add_argument('-a', action='store_true', help='Użyj szyfru afinicznego')
    parser.add_argument('-e', action='store_true', help='Szyfrowanie')
    parser.add_argument('-d', action='store_true', help='Odszyfrowywanie')
    parser.add_argument('-j', action='store_true', help='Kryptoanaliza z tekstem jawnym')
    parser.add_argument('-k', action='store_true', help='Kryptoanaliza bez tekstu jawnego')
    
    args = parser.parse_args()
    
    if args.c:
        cipher_type = 'caesar'
    elif args.a:
        cipher_type = 'affine'
    else:
        print("Błąd: Musisz wybrać -c (Cezar) lub -a (Afiniczny)")
        return
    
    if args.e:
        plain_text = read_file('data/plain.txt')
        key_line = read_file('data/key.txt')
        key_parts = key_line.split()
        
        if cipher_type == 'caesar':
            try:
                shift = int(key_parts[0])
            except (ValueError, IndexError):
                print("Błąd: Niepoprawny klucz dla szyfru Cezara.")
                return
            encrypted_text = caesar_cipher(plain_text, shift)
        else:
            try:
                shift, multiplier = int(key_parts[0]), int(key_parts[1])
            except (ValueError, IndexError):
                print("Błąd: Niepoprawny klucz dla szyfru afinicznego.")
                return
            encrypted_text = affine_cipher(plain_text, shift, multiplier)
        
        write_file('data/crypto.txt', encrypted_text)
    
    elif args.d:
        encrypted_text = read_file('data/crypto.txt')
        key_line = read_file('data/key.txt')
        key_parts = key_line.split()
        
        if cipher_type == 'caesar':
            try:
                shift = int(key_parts[0])
            except (ValueError, IndexError):
                print("Błąd: Niepoprawny klucz dla szyfru Cezara.")
                return
            decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
        else:
            try:
                shift, multiplier = int(key_parts[0]), int(key_parts[1])
            except (ValueError, IndexError):
                print("Błąd: Niepoprawny klucz dla szyfru afinicznego.")
                return
            decrypted_text = affine_cipher(encrypted_text, shift, multiplier, decrypt=True)
        
        write_file('data/decrypt.txt', decrypted_text)
    
    elif args.j:
        encrypted_text = read_file('data/crypto.txt')
        extra_text = read_file('data/extra.txt')
        found_key, decrypted_text = analyze_with_plaintext(encrypted_text, extra_text)
        write_file('data/key-found.txt', found_key)
        write_file('data/decrypt.txt', decrypted_text)
    
    elif args.k:
        encrypted_text = read_file('data/crypto.txt')
        possible_texts = analyze_without_plaintext(encrypted_text, cipher_type)
        write_file('data/decrypt.txt', "\n".join(possible_texts))
    
    else:
        print("Błąd: Musisz wybrać jedną z opcji: -e, -d, -j, -k")
        return
    
if __name__ == "__main__":
    main()
