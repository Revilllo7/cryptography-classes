# Autor: Oliver Gruba
import argparse
from img_process import load_image, save_image, split_blocks, merge_blocks
from cipher import ecb_encrypt, cbc_encrypt
from utils import load_key

def main():
    parser = argparse.ArgumentParser(description="Block-based image encryption in ECB/CBC mode")
    parser.add_argument("-ecb", action="store_true", help="Encrypt using ECB mode")
    parser.add_argument("-cbc", action="store_true", help="Encrypt using CBC mode")
    parser.add_argument("--key", default="key.txt", help="Path to key file (optional)")
    args = parser.parse_args()

    image_path = "plain.bmp"
    image = load_image(image_path)
    blocks = split_blocks(image, block_size=8)

    key = load_key(args.key)

    if args.ecb:
        encrypted_blocks = ecb_encrypt(blocks, key)
        ecb_image = merge_blocks(encrypted_blocks, image.size, 8)
        save_image(ecb_image, "ecb_crypto.bmp")

    if args.cbc:
        encrypted_blocks = cbc_encrypt(blocks, key)
        cbc_image = merge_blocks(encrypted_blocks, image.size, 8)
        save_image(cbc_image, "cbc_crypto.bmp")

if __name__ == "__main__":
    main()
