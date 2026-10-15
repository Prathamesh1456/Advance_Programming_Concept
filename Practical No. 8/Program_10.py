#10.	Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
str=input("Enter a string: ")
vowel_count = count_vowels(str)