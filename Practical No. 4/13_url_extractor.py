# URL Extraction using Regular Expression

import re


def extract_urls(html):
    pattern = r'https?://(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}|www\.[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    return re.findall(pattern, html)


html = input("Enter HTML content: ")

urls = extract_urls(html)

print("\nExtracted URLs:", urls)