#Autor: Oliver Gruba
def verify(p, g, y, m, r, s):
    if not (0 < r < p and 0 < s < p - 1):
        return False

    left = (pow(y, r, p) * pow(r, s, p)) % p
    right = pow(g, m, p)
    return left == right
