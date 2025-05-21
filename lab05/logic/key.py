#Autor: Oliver Gruba
import random

def read_elgamal(filename):
    with open(filename, 'r') as f:
        p = int(f.readline().strip())
        g = int(f.readline().strip())
    return p, g

def generate_keys(p, g):
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return x, y

def save_key(filename, p, g, value):
    with open(filename, 'w') as f:
        f.write(f"{p}\n{g}\n{value}\n")

def read_key(filename):
    with open(filename, 'r') as f:
        p = int(f.readline().strip())
        g = int(f.readline().strip())
        value = int(f.readline().strip())
    return p, g, value
