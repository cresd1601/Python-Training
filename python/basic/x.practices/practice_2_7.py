import random
from pathlib import Path

def load_book_words(file_path):
    """Load all words from a book into a list, cleaning them by removing punctuation."""
    with file_path.open('r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove punctuation and split into words
    words = []
    for word in text.split():
        clean_word = ''.join(char for char in word if char.isalpha()).lower()
        if clean_word:
            words.append(clean_word)
    return words

def choose_random_word(words):
    """Choose a random word from the list of words."""
    return random.choice(words)

# File path
book_file_path = Path(__file__).parent / 'data_practice_2_2.txt'
