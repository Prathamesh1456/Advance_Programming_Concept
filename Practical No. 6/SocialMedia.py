import re 

def get_hashtags(text):
    return re.findall(r'#[A-Za-z0-0_]+',text)

text = input("enter your post: ")
hashtags = get_hashtags(text)
print("hashtags :",hashtags)