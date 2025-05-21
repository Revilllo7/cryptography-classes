#Autor: Oliver Gruba
def decrypt(p, x, c1, c2):
    s = pow(c1, x, p)
    m = (c2 * pow(s, p - 2, p)) % p
    return m