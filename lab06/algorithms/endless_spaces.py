def embed_spaces_endlines(cover, bits):
    lines = cover.splitlines()
    if len(bits) > len(lines):
        return None
    # Usuń spacje na końcu linii
    lines = [l.rstrip() for l in lines]
    for i, bit in enumerate(bits):
        if bit == "1":
            lines[i] += " "
    return "\n".join(lines)

def extract_spaces_endlines(watermarked):
    lines = watermarked.splitlines()
    bits = ""
    for l in lines:
        bits += "1" if l.endswith(" ") else "0"
    return bits.rstrip("0")  # usuwamy nadmiarowe zera