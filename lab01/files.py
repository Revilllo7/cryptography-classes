import os

def read_file(filename):
    if not os.path.exists(filename):
        return ""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
