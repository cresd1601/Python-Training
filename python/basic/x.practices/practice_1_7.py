def hasThreeConsecutiveDoubleLetters(word):
    count = 0
    i = 0
    
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            i += 2  # Move to the next pair after finding a double letter
            if count == 3:
                return True  # Return True if three consecutive double letters are found
        else:
            count = 0  # Reset count if the sequence breaks
            i += 1
    
    return False  # Return False if less than three consecutive double letters are found

def findWordWithThreeDoubleLetters(wordList):
    for word in wordList:
        if hasThreeConsecutiveDoubleLetters(word):
            return word  # Return the first word that meets the criteria
    return None  # Return None if no such word is found

if __name__ == "__main__":
    words = ["committee", "bookkeeper", "Mississippi", "subbookkeeper"]
    
    word = findWordWithThreeDoubleLetters(words)
    if word:
        print(f"The word with three consecutive double letters is: {word}")
    else:
        print("No word with three consecutive double letters found.")
