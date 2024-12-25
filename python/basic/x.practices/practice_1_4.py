from pathlib import Path

# The default file path (you can customize this path as per your project structure)
DEFAULT_FILE_PATH = Path(__file__).parent / 'data_practice_1.txt'

def usesOnly(word, allowedLetters):
    for letter in word:
        if letter not in allowedLetters:
            return False
    return True

def countWordsUsingOnlyAllowedLetters(filePath=DEFAULT_FILE_PATH, allowedLetters=''):
    totalWords = 0
    wordsWithAllowedLetters = 0

    # Read the file
    with filePath.open('r') as file:
        for line in file:
            word = line.strip()
            totalWords += 1

            if usesOnly(word, allowedLetters):
                wordsWithAllowedLetters += 1

    return wordsWithAllowedLetters, totalWords
