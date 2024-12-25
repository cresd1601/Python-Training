from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import math

def read_file(file_path):
    """Reads the entire text from a file and returns it as a list of words."""
    with file_path.open('r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase for uniformity
    return text.split()

def count_word_frequencies(words):
    """Counts the frequency of each word in a list of words."""
    return Counter(words)

def calculate_log_values(word_freq):
    """Calculates the log of frequencies and ranks."""
    freqs = list(word_freq.values())
    ranks = range(1, len(freqs) + 1)
    
    log_f = [math.log(f) for f in freqs]
    log_r = [math.log(r) for r in ranks]
    
    return log_f, log_r

def plot_log_values(log_r, log_f):
    """Plots log(frequency) vs log(rank) to check Zipf's law."""
    plt.plot(log_r, log_f, 'o')
    plt.xlabel('log(rank)')
    plt.ylabel('log(frequency)')
    plt.title("Zipf's Law")
    plt.show()

def main(file_path):
    words = read_file(file_path)
    word_freq = count_word_frequencies(words)
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    
    log_f, log_r = calculate_log_values(sorted_word_freq)
    
    # Print words, log(f), and log(r)
    for i, (word, freq) in enumerate(sorted_word_freq.items()):
        print(f"{word}: log(f) = {log_f[i]:.4f}, log(r) = {log_r[i]:.4f}")
    
    plot_log_values(log_r, log_f)

# Example usage:
if __name__ == "__main__":
    # Specify the path to the text file using Path
    file_path = Path(__file__).parent / 'data_practice_2_3.txt'
    
    # Run the main function with the specified file path
    main(file_path)
