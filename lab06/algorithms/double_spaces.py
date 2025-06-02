import re

def embed_single_double_space(cover, bits):
    # Usuwamy podwójne spacje
    cover = re.sub(r" {2,}", " ", cover)
    spaces = [m.start() for m in re.finditer(r" ", cover)]
    if len(bits) > len(spaces):
        return None
    chars = list(cover)
    for i, bit in enumerate(bits):
        idx = spaces[i]
        if bit == "1":
            chars[idx] = "  "
    return "".join(chars)

def extract_single_double_space(watermarked):
    bits = ""
    i = 0
    while i < len(watermarked):
        if watermarked[i] == " ":
            if i+1 < len(watermarked) and watermarked[i+1] == " ":
                bits += "1"
                i += 2
            else:
                bits += "0"
                i += 1
        else:
            i += 1
    return bits.rstrip("0")