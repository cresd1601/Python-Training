from pathlib import Path
from collections import defaultdict

# Define the file path for the Gutenberg text
file_path = Path(__file__).parent / 'data_practice_2_3.txt'

def skip_gutenberg_header(file):
    """Skip the header of a Gutenberg book."""
    for line in file:
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'):
            break

def skip_gutenberg_footer(file):
    """Detect the footer of a Gutenberg book."""
    if '*** END OF THIS PROJECT GUTENBERG EBOOK' in file:
        return True
    return False

def clean_word(word):
    """Clean the word by removing punctuation and converting to lowercase, but keep alphanumeric characters."""
    cleaned_word = ''.join(char for char in word if char.isalnum())  # Keep letters and numbers
    return cleaned_word.lower()  # Convert to lowercase

def process_file(file_path):
    """Reads a file, skips the Gutenberg header, processes the text, and skips the footer."""
    word_count = defaultdict(int)
    total_words = 0

    try:
        with file_path.open('r', encoding='utf-8') as file:
            skip_gutenberg_header(file)

            for line in file:
                if skip_gutenberg_footer(line):
                    break  # Stop when footer is detected

                line = line.strip()
                words = line.split()

                for word in words:
                    cleaned_word = clean_word(word)

                    if cleaned_word:
                        total_words += 1
                        word_count[cleaned_word] += 1

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

    return total_words, word_count

def print_word_stats(total_words, word_count, top_n=20):
    """Print statistics about the words in the book."""
    if total_words is None or word_count is None:
        print("No statistics to show due to an earlier error.")
        return

    print(f"Total number of words: {total_words}")
    print(f"Number of different words: {len(word_count)}")
    print(f"\nTop {top_n} most common words:")

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    total_words, word_count = process_file(file_path)
    print_word_stats(total_words, word_count)