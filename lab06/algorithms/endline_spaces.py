import sys

MESSAGE_BITS = 120  # 30 hex chars * 4 bits
END_MARKER = '00000000'

def embed_spaces_endlines(content, bits):
    lines = content.split('\n')
    # Only lines with <p are candidates
    candidate_indices = [i for i, l in enumerate(lines) if "<p" in l]
    if len(bits) > len(candidate_indices):
        print(f"Need {len(bits)} <p> lines but only {len(candidate_indices)} available")
        sys.exit(1)
    # Strip all trailing whitespace from all candidate lines
    for idx in candidate_indices:
        lines[idx] = lines[idx].rstrip()
    for bit, idx in zip(bits, candidate_indices):
        lines[idx] += "   " if bit == "1" else " "
    return '\n'.join(lines)

def extract_spaces_endlines(content):
    lines = content.split('\n')
    bits = ''
    candidate_indices = [i for i, l in enumerate(lines) if "<p" in l]
    for idx in candidate_indices:
        line = lines[idx]
        spaces = len(line) - len(line.rstrip())
        bits += '1' if spaces >= 3 else '0'
    # Find and trim at end marker
    end_index = bits.find(END_MARKER)
    if end_index != -1:
        bits = bits[:end_index]
    # Pad/truncate to MESSAGE_BITS
    bits = bits[:MESSAGE_BITS].ljust(MESSAGE_BITS, '0')
    return bits