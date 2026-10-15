import re

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

text = input("Enter social media post: ")

hashtags = extract_hashtags(text)

print("Hashtags:", hashtags)