from pathlib import Path

# Open the file words.txt in the same directory as the script
filePath = Path(__file__).parent / 'data_practice_1.txt'

def isAbecedarian(word):
    previousLetter = word[0]
    for letter in word:
        if letter < previousLetter:
            return False
        previousLetter = letter
    return True

def countAbecedarianWords():
    abecedarianCount = 0
    totalWords = 0

    # Read the file
    with filePath.open('r') as file:
        for line in file:
            word = line.strip()
            totalWords += 1

            if isAbecedarian(word):
                abecedarianCount += 1
    
    print(f"Number of abecedarian words: {abecedarianCount}")
    print(f"Total number of words: {totalWords}")

# Call the function to count abecedarian words
countAbecedarianWords()
