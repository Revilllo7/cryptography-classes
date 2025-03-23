import string
from math import gcd

def analyze_with_plaintext(encrypted_text, extra_text):
    alphabet = string.ascii_uppercase
    for shift in range(26):
        decrypted = ''.join(alphabet[(alphabet.index(c) - shift) % 26] if c in alphabet else c for c in encrypted_text.upper())
        if decrypted.startswith(extra_text.upper()):
            return f"{shift}", decrypted
    raise ValueError("Nie znaleziono pasującego klucza.")

def analyze_without_plaintext(encrypted_text, cipher_type):
    alphabet = string.ascii_uppercase
    possible_texts = []
    
    encrypted_text = encrypted_text.upper()  # Ensure uppercase input
    
    if cipher_type == 'caesar':
        for shift in range(26):
            decrypted = ''.join(
                alphabet[(alphabet.index(c) - shift) % 26] if c in alphabet else c 
                for c in encrypted_text
            )
            possible_texts.append(f"Shift {shift}: {decrypted}")
    
    elif cipher_type == 'affine':
        valid_multipliers = [m for m in range(1, 26, 2) if gcd(m, 26) == 1]

        for multiplier in valid_multipliers:
            try:
                inv_multiplier = pow(multiplier, -1, 26)
                for shift in range(26):
                    decrypted = ''.join(
                        alphabet[(inv_multiplier * ((alphabet.index(c) - shift) % 26)) % 26] if c in alphabet else c
                        for c in encrypted_text
                    )
                    possible_texts.append(f"a={multiplier}, b={shift}: {decrypted}")
            except ValueError:
                continue  # Skip invalid multipliers 
    
    return possible_texts