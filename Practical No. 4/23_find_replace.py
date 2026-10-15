filename = input("Enter input file name: ")
target = input("Enter word or phrase to replace: ")
replacement = input("Enter replacement: ")

choice = input("Ignore case? (yes/no): ")

with open(filename, "r") as file:
    text = file.read()

if choice.lower() == "yes":
    import re
    text = re.sub(re.escape(target), replacement, text, flags=re.IGNORECASE)
else:
    text = text.replace(target, replacement)

output_file = input("Enter new output file name: ")

with open(output_file, "w") as file:
    file.write(text)

print("File saved successfully.")