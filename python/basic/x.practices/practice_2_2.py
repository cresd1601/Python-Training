from pathlib import Path
from collections import defaultdict

# Define the file path for the Gutenberg text
file_path = Path(__file__).parent / 'data_practice_2_2.txt'

def skip_gutenberg_header(file):
    """Skip the header of a Gutenberg book."""
    for line in file:
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'):
            break
    # No need to advance to the next line after breaking, so no additional action is needed.

def clean_word(word):
    """Clean the word by removing punctuation and converting to lowercase."""
    # Remove any non-alphanumeric characters from the word
    cleaned_word = ''.join(char for char in word if char.isalnum())
    return cleaned_word.lower()

def process_file(file_path):
    """Reads a file, skips the Gutenberg header, and processes the rest of the text."""
    word_count = defaultdict(int)
    total_words = 0

    try:
        with file_path.open('r', encoding='utf-8') as file:
            skip_gutenberg_header(file)

            for line in file:
                print(f"Processing line: {line.strip()}")  # Debugging output

                # Remove leading/trailing whitespace
                line = line.strip()

                # Split the line into words
                words = line.split()

                for word in words:
                    cleaned_word = clean_word(word)

                    if cleaned_word:  # Only count non-empty cleaned words
                        total_words += 1
                        word_count[cleaned_word] += 1
                        print(f"Counted word: {cleaned_word}")  # Debugging output
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return None, None

    print(f"Total words counted: {total_words}")  # Debugging output
    return total_words, word_count

def print_word_stats(total_words, word_count, top_n=10):
    """Print statistics about the words in the book."""
    if total_words is None or word_count is None:
        print("No statistics to show due to an earlier error.")
        return

    print(f"Total number of words: {total_words}")
    print(f"Number of different words: {len(word_count)}")
    print("\nMost common words:")

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words[:top_n]:  # print top N most common words
        print(f"{word}: {count}")