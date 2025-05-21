#Autor: Oliver Gruba
def read_message(filename):
    with open(filename, 'r') as f:
        m = int(f.readline().strip())
    return m