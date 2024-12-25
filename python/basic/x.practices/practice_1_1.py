from pathlib import Path

def find_long_words(file_name='data_practice_1.txt'):
    """
    Reads a file and prints words longer than 20 characters.

    Args:
    file_name (str): Name of the file to read.

    Returns:
    list: A list of words that are longer than 20 characters.
    """
    # Open the file in the same directory as the script
    file_path = Path(__file__).parent / file_name

    # List to hold long words
    long_words = []

    # Read the file
    with file_path.open('r') as file:
        for line in file:
            word = line.strip()

            if len(word) > 20:
                print(word)
                long_words.append(word)

    return long_words
