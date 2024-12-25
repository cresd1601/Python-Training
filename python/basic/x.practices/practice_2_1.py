import string
from pathlib import Path


def process_file(file_path):
    """Process words from a file, removing punctuation and converting to lowercase."""
    processed_words = []
    # Read the file
    with file_path.open('r') as file:
        for line in file:
            # Strip leading/trailing whitespace and split the line into words
            words = line.strip().split()

            for word in words:
                # Strip punctuation from the beginning and end of the word
                word = word.strip(string.punctuation)

                # Convert the word to lowercase
                word = word.lower()

                # Append the processed word to the list
                processed_words.append(word)

    return processed_words


if __name__ == "__main__":
    file_path = Path(__file__).parent / 'data_practice_2_1.txt'
    words = process_file(file_path)
    for word in words:
        print(word)
