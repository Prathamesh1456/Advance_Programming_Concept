# Phone Number Extraction using Regular Expression

import re


def extract_phone_numbers(text):
    pattern = r'(?:\(\d{3}\)\s?\d{3}[-.]?\d{4}|\d{3}[-.]\d{3}[-.]\d{4}|\d{10})'

    return re.findall(pattern, text)


text = input("Enter a block of text: ")

phone_numbers = extract_phone_numbers(text)

print("\nPhone numbers found:", phone_numbers)