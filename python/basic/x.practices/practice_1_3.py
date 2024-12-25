from pathlib import Path

# Open the file words.txt in the same directory as the script
filePath = Path(__file__).parent / 'data_practice_1.txt'

def avoids(word, forbiddenLetters):
    for letter in forbiddenLetters:
        if letter in word:
            return False
    
    return True

def countWordsWithoutForbiddenLetter(forbiddenLetters):
    totalWords = 0
    wordsWithoutForbidden = 0

    # Read the file
    with filePath.open('r') as file:
        for line in file:
            word = line.strip()
            totalWords += 1

            if avoids(word, forbiddenLetters): 
                wordsWithoutForbidden += 1
    
    print(f"Number of words without forbidden letters: {wordsWithoutForbidden}")
    print(f"Total number of words: {totalWords}")