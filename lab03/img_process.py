from PIL import Image
import numpy as np

def load_image(path):
    img = Image.open(path).convert("L")  # Convert to grayscale
    return img

def save_image(image, path):
    image.save(path)

def split_blocks(image, block_size=8):
    pixels = np.array(image)
    h, w = pixels.shape
    # Pad the image to make dimensions divisible by block_size
    pad_h = (block_size - h % block_size) % block_size
    pad_w = (block_size - w % block_size) % block_size
    padded_pixels = np.pad(pixels, ((0, pad_h), (0, pad_w)), mode='constant', constant_values=0)
    blocks = []
    for i in range(0, padded_pixels.shape[0], block_size):
        for j in range(0, padded_pixels.shape[1], block_size):
            block = padded_pixels[i:i+block_size, j:j+block_size]  # Fixed indexing
            blocks.append(block)
    return blocks

def merge_blocks(blocks, image_size, block_size=8):
    h, w = image_size
    padded_h = (h + block_size - 1) // block_size * block_size
    padded_w = (w + block_size - 1) // block_size * block_size
    output = np.zeros((padded_h, padded_w), dtype=np.uint8)
    idx = 0
    for i in range(0, padded_h, block_size):
        for j in range(0, padded_w, block_size):
            if idx < len(blocks):
                output[i:i+block_size, j:j+block_size] = blocks[idx]
                idx += 1
    # Remove padding to restore original image size
    return Image.fromarray(output[:h, :w])
