from pathlib import Path

# Open the file words.txt in the same directory as the script
filePath = Path(__file__).parent / 'data_practice_1.txt'

def hasNoE(word):
    return "e" not in word

def printWordsWithoutE():
    totalWords = 0
    wordWithoutE = 0

    # Read the file
    with filePath.open('r') as file:
        for line in file:
            word = line.strip()
            totalWords += 1

            if hasNoE(word): 
                wordWithoutE += 1
    
    percentage = (wordWithoutE / totalWords) * 100
    print(f"Number of words without 'e': {wordWithoutE}")
    print(f"Percentage of words without 'e': {percentage:.2f}%")