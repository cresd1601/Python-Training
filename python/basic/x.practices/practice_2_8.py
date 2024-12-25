from pathlib import Path

def read_file(file_path):
    """Reads the entire text from a file and returns it as a list of words."""
    with file_path.open('r', encoding='utf-8') as file:
        text = file.read()
    return text.split()

def markov_analysis(words, prefix_length=2):
    """
    Performs Markov analysis on a list of words.
    
    Returns a dictionary that maps from prefixes (tuples of words) to a list of suffixes.
    """
    markov_dict = {}
    
    # Loop over the words and build the Markov chain
    for i in range(len(words) - prefix_length):
        prefix = tuple(words[i:i + prefix_length])  # Get the prefix as a tuple
        suffix = words[i + prefix_length]  # The word following the prefix
        
        if prefix not in markov_dict:
            markov_dict[prefix] = []  # Initialize a list for this prefix
        
        markov_dict[prefix].append(suffix)  # Add the suffix to the list
    
    return markov_dict

# Example usage:
if __name__ == "__main__":
    # Specify the path to the text file
    file_path = Path(__file__).parent / 'data_practice_2_2.txt'
    
    # Read the words from the file
    words = read_file(file_path)
    
    # Perform Markov analysis with a prefix length of 2
    prefix_length = 2
    markov_dict = markov_analysis(words, prefix_length=prefix_length)
    
    # Print out part of the Markov dictionary for inspection
    for prefix, suffixes in list(markov_dict.items())[:10]:
        print(f"Prefix: {prefix}, Suffixes: {suffixes}")
