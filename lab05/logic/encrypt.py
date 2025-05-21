#Autor: Oliver Gruba
import sys
import random

def encrypt(p, g, y, m):
    if m >= p:
        print("Error: Nie spełniono warunku m < p")
        sys.exit(1)

    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2
