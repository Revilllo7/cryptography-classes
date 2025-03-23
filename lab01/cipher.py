import string

def caesar_cipher(text, shift, decrypt=False):
    alphabet = string.ascii_uppercase
    shift = -shift if decrypt else shift
    trans = str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])
    return text.upper().translate(trans)

def affine_cipher(text, shift, multiplier, decrypt=False):
    alphabet = string.ascii_uppercase
    m = len(alphabet)
    
    if decrypt:
        try:
            inv_multiplier = pow(multiplier, -1, m)
        except ValueError:
            raise ValueError("Nie można znaleźć odwrotności modularnej dla podanego współczynnika.")
        return ''.join(alphabet[(inv_multiplier * (alphabet.index(c) - shift)) % m] if c in alphabet else c for c in text.upper())
    else:
        return ''.join(alphabet[(multiplier * alphabet.index(c) + shift) % m] if c in alphabet else c for c in text.upper())
