import re

def count_extensions(files):
    extensions = {}
    for file in files:
        match = re.search(r'\.[a-zA-Z0-9]+$', file)
        if match:
            ext = match.group()
            extensions[ext] = extensions.get(ext, 0) + 1
    return extensions

files = ["a.txt", "b.pdf", "c.txt", "d.png", "e.pdf", "f.txt"]

print(count_extensions(files))