# Date Extraction and Conversion using Regular Expression

import re
from datetime import datetime


def extract_dates(text):
    pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{4}\.\d{2}\.\d{2}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b'

    dates = re.findall(pattern, text)

    converted_dates = []

    for date in dates:
        if "/" in date:
            new_date = datetime.strptime(date, "%d/%m/%Y")
        elif "-" in date:
            new_date = datetime.strptime(date, "%m-%d-%Y")
        elif "." in date:
            new_date = datetime.strptime(date, "%Y.%m.%d")
        else:
            new_date = datetime.strptime(date, "%B %d, %Y")

        converted_dates.append(new_date.strftime("%Y-%m-%d"))

    return converted_dates


text = input("Enter a block of text: ")

dates = extract_dates(text)

print("\nDates in YYYY-MM-DD format:", dates)