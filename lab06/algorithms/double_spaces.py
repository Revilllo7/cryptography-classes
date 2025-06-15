import re

def embed_single_double_space(cover, bits):
    # Split into tokens: words and whitespace
    tokens = re.split(r'(\s+)', cover)
    bit_idx = 0
    for i, token in enumerate(tokens):
        if token == " " and bit_idx < len(bits):
            tokens[i] = "  " if bits[bit_idx] == "1" else " "
            bit_idx += 1
    if bit_idx < len(bits):
        return None
    return ''.join(tokens)

def extract_single_double_space(watermarked):
    tokens = re.split(r'(\s+)', watermarked)
    bits = ""
    for token in tokens:
        if token == " ":
            bits += "0"
        elif token == "  ":
            bits += "1"
    return bits