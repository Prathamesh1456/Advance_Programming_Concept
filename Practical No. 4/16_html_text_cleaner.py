# HTML Text Cleaner using Regular Expression

import re


def clean_html(html):
    pattern = r'<[^>]*>'
    cleaned_text = re.sub(pattern, ' ', html)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text


html = input("Enter HTML content: ")

cleaned_text = clean_html(html)

print("\nCleaned text:", cleaned_text)