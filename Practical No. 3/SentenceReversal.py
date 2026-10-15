# 29.	Sentence Reversal 
# ●	Reverse the order of words in a sentence without changing the words themselves. 
# ●	Example:
# ●	Input: Python is easy
# Output: easy is Python
Str=input("Enter a sentence: ")
words=Str.split()
reversed_sentence = " ".join(reversed(words))
print("Reversed sentence:", reversed_sentence)