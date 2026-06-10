word = input("enter a word: ")

word_lower = word.lower()

word_reversed = word_lower[::-1]

if word_lower == word_reversed:

    print(f"'{word}' is a palindrome  ✓")
else:
    print(f"'{word}' is not a palindrome ✗")
