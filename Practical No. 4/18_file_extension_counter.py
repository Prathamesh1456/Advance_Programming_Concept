import re

filenames = input("Enter filenames: ").split()

extensions = {}

for filename in filenames:
    match = re.search(r'\.([A-Za-z0-9]+)$', filename)

    if match:
        extension = "." + match.group(1).lower()
        extensions[extension] = extensions.get(extension, 0) + 1

print("Extension frequencies:", extensions)