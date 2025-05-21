#Autor: Oliver Gruba
import random
from math import gcd

def sign(p, g, x, m):
    while True:
        k = random.randint(2, p - 2)
        if gcd(k, p - 1) == 1:
            break

    r = pow(g, k, p)
    k_inv = pow(k, -1, p - 1)
    s = ((m - x * r) * k_inv) % (p - 1)
    return r, s
