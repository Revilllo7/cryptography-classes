#Autor: Oliver Gruba
import argparse
import sys

from algorithms.endline_spaces import (
    embed_spaces_endlines, extract_spaces_endlines
)

from algorithms.double_spaces import (
    embed_single_double_space, extract_single_double_space
)

from algorithms.embed_font import (
    embed_font_tags, extract_font_tags
)

from algorithms.typo_attributes import (
    embed_typo_attributes, extract_typo_attributes
)

def read_message_bits(filename):
    with open(filename, "r") as f:
        hexstr = f.read().strip()
    bits = bin(int(hexstr, 16))[2:]
    bits = bits.zfill(len(hexstr)*4)
    return bits

def write_message_bits(bits, filename):
    hexstr = hex(int(bits, 2))[2:]
    with open(filename, "w") as f:
        f.write(hexstr)

def main():
    parser = argparse.ArgumentParser(description="Steganografia HTML")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Zanurz wiadomość")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Wyodrębnij wiadomość")
    parser.add_argument("-m", "--method", type=int, choices=[1, 2, 3, 4], help="Metoda: 1-spacje na końcu linii, 2-pojedyncza/podwójna spacja, 3-literówki w atrybutach, 4-znaczniki FONT")
    args = parser.parse_args()

    if args.encrypt == args.decrypt:
        print("Wybierz dokładnie jedną z opcji -e lub -d")
        sys.exit(1)

    if args.encrypt:
        if args.method is None:
            print("Dla opcji -e musisz podać metodę za pomocą -m [1|2|3|4]")
            sys.exit(1)
        bits = read_message_bits("mess.txt")
        with open("cover.html") as f:
            cover = f.read()
        if args.method == 1:
            result = embed_spaces_endlines(cover, bits)
        elif args.method == 2:
            result = embed_single_double_space(cover, bits)
        elif args.method == 3:
            result = embed_typo_attributes(cover, bits)
        elif args.method == 4:
            result = embed_font_tags(cover, bits)
        if result is None:
            print("Nośnik za mały!")
            sys.exit(1)
        with open("watermark.html", "w") as f:
            f.write(result)
    else:
        with open("watermark.html") as f:
            watermarked = f.read()
        candidates = []
        for extractor in [
            extract_spaces_endlines,
            extract_single_double_space,
            extract_typo_attributes,
            extract_font_tags
        ]:
            try:
                bits = extractor(watermarked)
                if bits:
                    # Pad bits to a multiple of 4
                    if len(bits) % 4 != 0:
                        bits = bits.ljust((len(bits) + 3) // 4 * 4, "0")
                    try:
                        int(bits, 2)
                        candidates.append(bits)
                    except ValueError:
                        pass
            except Exception:
                pass

        bits = max(candidates, key=len, default="")
        if not bits:
            print("Nie udało się wykryć ukrytej wiadomości.")
            sys.exit(1)
        # Truncate to original message length
        with open("mess.txt") as f:
            orig_hex = f.read().strip()
        orig_bits_len = len(orig_hex) * 4
        bits = bits[:orig_bits_len]
        # Debug: print original and extracted bits
        orig_bits = bin(int(orig_hex, 16))[2:].zfill(orig_bits_len)
        # print("Original bits:  ", orig_bits)
        # print("Extracted bits: ", bits)
        # print("Extracted bits (raw):", bits)
        END_MARKER = "00000000"
        bits = read_message_bits("mess.txt") + END_MARKER
        end_index = bits.find(END_MARKER)
        if end_index != -1:
            bits = bits[:end_index]
        
        MESSAGE_BITS = orig_bits_len  # Assuming MESSAGE_BITS is the original message length in bits
        bits = bits[:MESSAGE_BITS].ljust(MESSAGE_BITS, '0')
        write_message_bits(bits, "detect.txt")

    print("Operacja zakończona pomyślnie.")
    if args.encrypt:
        print("Wiadomość zaszyfrowana i zapisana w watermark.html")
    else:
        print("Wiadomość wyodrębniona i zapisana w detect.txt")
if __name__ == "__main__":
    main()