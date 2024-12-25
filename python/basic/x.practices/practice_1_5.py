from pathlib import Path

# Open the file words.txt in the same directory as the script
filePath = Path(__file__).parent / 'data_practice_1.txt'

def usesAll(word, allowedLetters):
    # Return True only if all letters in word are in allowedLetters
    for letter in word:
        if letter not in allowedLetters:
            return False
    return True

def countWordsUsingOnlyAllowedLetters(allowedLetters):
    totalWords = 0
    wordsWithAllowedLetters = 0

    # Read the file
    with filePath.open('r') as file:
        for line in file:
            word = line.strip()
            totalWords += 1

            if usesAll(word, allowedLetters):
                wordsWithAllowedLetters += 1

    # Return the count of words with allowed letters and the total number of words
    return wordsWithAllowedLetters, totalWords
