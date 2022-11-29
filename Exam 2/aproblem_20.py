# Get the sentence
sentence = input("Enter a sentence: ").split(" ")

# Counter function
def count_letters(word: str):
    c, v = 0, 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"

    for letter in word:
        if letter.lower() in alphabet and letter.lower() in vowels:
            v += 1
        elif letter.lower() in alphabet:
            c += 1

    return c, v

# Loop each word and check for vowels and consonants
for word in sentence:
    c, v = count_letters(word)
    print(f"{word} contains {c} consonant(s) and {v} vowel(s).")

