# Anagram Checker

import string

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Normalize strings by keeping only letters and numbers
str1 = ''.join(char.lower() for char in str1 if char.isalnum())
str2 = ''.join(char.lower() for char in str2 if char.isalnum())

# Count character frequencies
frequency1 = {}
frequency2 = {}

for char in str1:
    frequency1[char] = frequency1.get(char, 0) + 1

for char in str2:
    frequency2[char] = frequency2.get(char, 0) + 1

# Compare frequencies
if frequency1 == frequency2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")