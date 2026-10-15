# Book Vocabulary Analysis

book1 = set(input("Enter words from Book 1: ").lower().split())
book2 = set(input("Enter words from Book 2: ").lower().split())

# Common words
common_words = book1.intersection(book2)

# Words unique to Book 1
unique_book1 = book1.difference(book2)

# Words unique to Book 2
unique_book2 = book2.difference(book1)

# All unique words across both books
all_words = book1.union(book2)

print("\nUnique words in Book 1:", book1)
print("Unique words in Book 2:", book2)

print("\nCommon words:", common_words)
print("Words unique to Book 1:", unique_book1)
print("Words unique to Book 2:", unique_book2)

print("\nTotal number of unique words across both books:", len(all_words))