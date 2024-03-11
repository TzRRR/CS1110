# Name: Lawrence Truong & Tianze Ren
# NetID: lt6vc & tr2bx


word = input("Enter a word or phrase: ")
word = word.lower()
word = "_".join(word)+ "_"
print("The word to guess: "+word)
letter = input("Guess a letter: ")
word = word.replace(letter+"_", letter+letter)
if "_" not in word:
    print("You have guessed the word!")
elif letter in word:
    word = word.replace(letter + "_", letter + letter)
    print(word)
    letter = input("Guess a letter: ")
elif letter not in word:
    print(word)
    letter = input("Guess a letter: ")
if "_" not in word:
    print("You have guessed the word!")
elif letter in word:
    word = word.replace(letter + "_", letter + letter)
    print(word)
    letter = input("Guess a letter: ")
elif letter not in word:
    print(word)
    letter = input("Guess a letter: ")
if "_" not in word:
    print("You have guessed the word!")
elif letter in word:
    word = word.replace(letter + "_", letter + letter)
    print(word)
    letter = input("Guess a letter: ")
elif letter not in word:
    print(word)
    letter = input("Guess a letter: ")