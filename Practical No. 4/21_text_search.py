import re

text = input("Enter text: ")
query = input("Enter search query: ")

count = len(re.findall(re.escape(query), text, re.IGNORECASE))

highlighted = re.sub(
    re.escape(query),
    lambda match: "**" + match.group() + "**",
    text,
    flags=re.IGNORECASE
)

print("\nNumber of occurrences:", count)
print("Highlighted text:", highlighted)