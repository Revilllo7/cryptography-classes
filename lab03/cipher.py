import hashlib
import numpy

def hash_block(block, key):
    flat = block.flatten()
    data = bytes(flat) + key
    digest = hashlib.sha512(data).digest()
    return numpy.frombuffer(digest[:64], dtype=numpy.uint8).reshape((8, 8))

def xor_blocks(a, b):
    return numpy.bitwise_xor(a, b)

def ecb_encrypt(blocks, key):
    return [hash_block(block, key) for block in blocks]

def cbc_encrypt(blocks, key):
    encrypted = []
    prev = numpy.zeros_like(blocks[0], dtype=numpy.uint8)
    for block in blocks:
        input_block = xor_blocks(block, prev)
        encrypted_block = hash_block(input_block, key)
        encrypted.append(encrypted_block)
        prev = encrypted_block
    return encrypted
