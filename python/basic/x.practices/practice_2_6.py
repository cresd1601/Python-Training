from pathlib import Path

def load_words(file_path):
    """Load words from a file into a set, converting them to lowercase."""
    with file_path.open('r', encoding='utf-8') as file:
        words = set(line.strip().lower() for line in file)
    return words

def load_book(file_path):
    """Load all words from a book into a set, cleaning them by removing punctuation."""
    with file_path.open('r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove punctuation and split into words
    words = set()
    for word in text.split():
        clean_word = ''.join(char for char in word if char.isalpha()).lower()
        if clean_word:
            words.add(clean_word)
    return words

def find_unknown_words(book_words, word_list):
    """Find words in the book that are not in the word list using set subtraction."""
    return book_words - word_list

# File paths
book_file_path = Path(__file__).parent / 'data_practice_2_2.txt'
word_list_file_path = Path(__file__).parent / 'data_practice_1.txt'