word = input("Enter a word: ")
word = word.replace(" ", "")
reversed_word = ''

for char in word:
    reversed_word = char + reversed_word

is_palindrome = word == reversed_word

print("Palindrome" if is_palindrome else "Not a palindrome")