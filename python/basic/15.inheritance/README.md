# Python Basics - Inheritance

Chapter 18 delves into the concept of inheritance in object-oriented programming, demonstrating how new classes can be derived from existing ones. This chapter builds on the principles of classes and methods introduced in earlier chapters, focusing on the mechanisms that allow for code reuse and extension. Below is a summary of the key concepts covered in Chapter 18.

---

## 1. Card Objects

The chapter begins by introducing a `Card` class, which represents a standard playing card. This class includes attributes such as `suit` and `rank`.

### Example:

```python
class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [None, 'Ace', '2', '3', ..., 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
```

### Use Cases:

- Modeling a deck of cards for card games.
- Demonstrating basic class structures in Python.

---

## 2. Class Attributes

Class attributes are variables that are shared across all instances of a class. In the `Card` class, `suits` and `ranks` are class attributes that define the possible suits and ranks for all card instances.

### Example:

```python
class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [None, 'Ace', '2', '3', ..., 'King']
```

### Use Cases:

- Defining constants or fixed values that are common to all instances of a class.
- Reducing redundancy by sharing data across all instances of a class.

---

## 3. Comparing Cards

The chapter introduces methods to compare card instances based on their suit and rank. This is essential for operations like sorting a deck of cards.

### Example Code:

```python
def __lt__(self, other):
    if self.suit < other.suit:
        return True
    if self.suit > other.suit:
        return False
    return self.rank < other.rank
```

### Use Cases:

- Sorting cards by rank and suit.
- Implementing game logic that requires comparing cards.

---

## 4. Decks

A `Deck` class is created to manage a collection of `Card` objects. The `Deck` class includes methods for shuffling, dealing, and printing the deck.

### Example Code:

```python
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)
```

### Use Cases:

- Simulating a deck of cards for games.
- Demonstrating how to work with collections of objects in Python.

---

## 5. Inheritance

Inheritance allows new classes to be derived from existing ones. The chapter explains how to create a `Hand` class that inherits from the `Deck` class, representing the cards held by a single player.

### Example Code:

```python
class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label
```

### Use Cases:

- Extending the functionality of existing classes without modifying them.
- Creating specialized versions of classes with additional features.

---

## 6. Class Diagrams

The chapter introduces class diagrams as a way to visually represent the relationships between classes, particularly in inheritance hierarchies.

### Use Cases:

- Documenting class structures in object-oriented design.
- Visualizing the relationships between parent and child classes.

---

### Summary:

Chapter 18 provides a comprehensive introduction to inheritance in Python, demonstrating how new classes can be built on top of existing ones. By understanding and using inheritance, you can create more modular, reusable, and maintainable code. This chapter is essential for advancing your knowledge of object-oriented programming in Python.
