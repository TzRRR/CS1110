# Name: Lawrence Truong & Tianze Ren
# NetID: lt6vc & tr2bx


word = input("Enter a word or phrase: ")
word = word.lower()
print("The word to guess: " + int(len(word)) * "_")
word = "_".join(word)+ "_"

while "_" in word:
    letter = input("Guess a letter: ")
    word = word.replace(letter + "_", letter)
    print(word)

print("You have guessed the word!")