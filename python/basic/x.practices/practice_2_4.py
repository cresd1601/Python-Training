from pathlib import Path
from collections import defaultdict

# Define the file paths for the Gutenberg text and the word list
file_path = Path(__file__).parent / 'data_practice_2_2.txt'
word_list_path = Path(__file__).parent / 'data_practice_1.txt'

def skip_gutenberg_header(file):
    """Skip the header of a Gutenberg book."""
    for line in file:
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'):
            break

def clean_word(word):
    """Clean the word by removing punctuation and converting to lowercase."""
    cleaned_word = ''.join(char for char in word if char.isalpha())
    return cleaned_word.lower()

def load_word_list(word_list_path):
    """Load a word list from a file into a set."""
    with word_list_path.open('r', encoding='utf-8') as file:
        word_list = set(line.strip().lower() for line in file)
    return word_list

def process_file(file_path, word_list):
    """Reads a file, skips the Gutenberg header, and processes the rest of the text."""
    word_count = defaultdict(int)
    unknown_words = set()
    
    with file_path.open('r', encoding='utf-8') as file:
        skip_gutenberg_header(file)
        
        for line in file:
            line = line.strip()
            words = line.split()
            
            for word in words:
                cleaned_word = clean_word(word)
                
                if cleaned_word:
                    word_count[cleaned_word] += 1
                    if cleaned_word not in word_list:
                        unknown_words.add(cleaned_word)

    return word_count, unknown_words

def categorize_unknown_words(unknown_words, word_list):
    """Categorize unknown words into typos, common words, and obscure words."""
    typos = set()
    common_words = set()
    obscure_words = set()

    for word in unknown_words:
        if len(word) <= 2 and word not in word_list:  # Only add short words to typos if not in word list
            typos.add(word)
        elif word in word_list:  # Classify as common if it's in the word list
            common_words.add(word)
        else:
            obscure_words.add(word)

    return typos, common_words, obscure_words

def print_categorized_word_stats(typos, common_words, obscure_words):
    """Print statistics about categorized unknown words."""
    print(f"\nNumber of typos: {len(typos)}")
    print(f"Number of common words that should be in the word list: {len(common_words)}")
    print(f"Number of obscure words: {len(obscure_words)}")

    print("\nSample typos:")
    for word in sorted(typos)[:10]:  # Print first 10 typos
        print(word)

    print("\nSample common words:")
    for word in sorted(common_words)[:10]:  # Print first 10 common words
        print(word)

    print("\nSample obscure words:")
    for word in sorted(obscure_words)[:10]:  # Print first 10 obscure words
        print(word)
