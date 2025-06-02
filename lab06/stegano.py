#Autor: Oliver Gruba
import argparse
import sys

from algorithms.endless_spaces import (
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
    # zapisz jako hex
    hexstr = hex(int(bits, 2))[2:]
    with open(filename, "w") as f:
        f.write(hexstr)

def main():
    parser = argparse.ArgumentParser(description="Steganografia HTML")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Zanurz wiadomość")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Wyodrębnij wiadomość")
    parser.add_argument("-1", "--one", action="store_true", help="Opcja 1: spacje na końcu linii")
    parser.add_argument("-2", "--two", action="store_true", help="Opcja 2: pojedyncza/podwójna spacja")
    parser.add_argument("-3", "--three", action="store_true", help="Opcja 3: literówki w atrybutach")
    parser.add_argument("-4", "--four", action="store_true", help="Opcja 4: znaczniki FONT")
    args = parser.parse_args()

    if args.encrypt == args.decrypt:
        print("Wybierz dokładnie jedną z opcji -e lub -d")
        sys.exit(1)

    if args.encrypt:
        if sum([args.one, args.two, args.three, args.four]) != 1:
            print("Wybierz dokładnie jedną z opcji -1, -2, -3, -4")
            sys.exit(1)
        bits = read_message_bits("mess.txt")
        with open("cover.html") as f:
            cover = f.read()
        if args.one:
            result = embed_spaces_endlines(cover, bits)
        elif args.two:
            result = embed_single_double_space(cover, bits)
        elif args.three:
            result = embed_typo_attributes(cover, bits)
        elif args.four:
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
        # Try all extraction methods, catch exceptions
        for extractor in [
            extract_spaces_endlines,
            extract_single_double_space,
            extract_typo_attributes,
            extract_font_tags
        ]:
            try:
                bits = extractor(watermarked)
                # Only accept if bits are not empty and can be converted to hex
                if bits and len(bits) % 4 == 0:
                    try:
                        int(bits, 2)
                        candidates.append(bits)
                    except ValueError:
                        pass
            except Exception:
                pass

        # Choose the longest valid result
        bits = max(candidates, key=len, default="")
        if not bits:
            print("Nie udało się wykryć ukrytej wiadomości.")
            sys.exit(1)
        write_message_bits(bits, "detect.txt")

if __name__ == "__main__":
    main()