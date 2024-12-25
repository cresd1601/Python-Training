import random

def histogram(s):
    """Takes a list of items and returns a histogram (dictionary) of frequencies."""
    hist = {}
    for item in s:
        hist[item] = hist.get(item, 0) + 1
    return hist

def choose_from_hist(hist):
    """Takes a histogram and returns a random key, weighted by its frequency."""
    # Create a list of the keys, with each key appearing according to its frequency
    keys = []
    for key, freq in hist.items():
        keys.extend([key] * freq)
    
    # Randomly choose one key from the list
    return random.choice(keys)