# Chapter 3: Code Smells and Refactoring

## Overview:
This chapter focuses on identifying and eliminating "code smells," which are indicators of potential issues in code that can lead to poor design or make maintenance difficult. The chapter also introduces various refactoring techniques to improve the code’s structure while preserving its behavior.

## Key Concepts:
### 1. Code Smells:
These are signs that something might be wrong with your code’s design. Some common smells include:
- **Duplicated Code**: Repeated logic across the codebase.
- **Long Methods**: Methods that are too long and handle too much logic.
- **Magic Numbers**: Hard-coded values that make the code unclear.

### 2. Refactoring Techniques:
Several techniques are explored to address code smells:
- **Rename Variable and Method**: Improves readability by making variable and method names more meaningful.
- **Extract Method**: Breaks down long methods by creating smaller, more focused methods.
- **Replace Magic Literals with Constants**: Replaces hardcoded values with named constants to improve clarity.
- **Move Method**: Relocates methods to more appropriate classes, especially when a method seems to belong elsewhere.

### 3. Principles of Good Design:
- **DRY (Don't Repeat Yourself)**: Encourages removing duplication in code.
- **Single Responsibility Principle**: Each class or method should have a single responsibility, making code easier to maintain and extend.

### 4. Refactoring in TDD:
The chapter emphasizes that refactoring should always be done with tests in place, ensuring that the code’s behavior remains intact during changes. This allows developers to safely improve code quality without introducing bugs.

## Exercise:
The chapter includes exercises where the reader refactors a dual crossover moving average implementation by applying the discussed refactoring techniques.

### Example Refactoring Exercise Code:
Before Refactoring:
```python
def dual_crossover(prices, short_term=5, long_term=10):
    short_term_avg = sum(prices[-short_term:]) / short_term
    long_term_avg = sum(prices[-long_term:]) / long_term
    if short_term_avg > long_term_avg:
        return "Buy"
    else:
        return "Sell"
```

After Refactoring:
```python
class MovingAverage:
    def __init__(self, prices):
        self.prices = prices

    def calculate(self, period):
        return sum(self.prices[-period:]) / period

class CrossoverSignal:
    def __init__(self, prices, short_term=5, long_term=10):
        self.moving_average = MovingAverage(prices)
        self.short_term = short_term
        self.long_term = long_term

    def get_signal(self):
        short_term_avg = self.moving_average.calculate(self.short_term)
        long_term_avg = self.moving_average.calculate(self.long_term)
        if short_term_avg > long_term_avg:
            return "Buy"
        else:
            return "Sell"
```

## Summary:
Refactoring is an essential part of maintaining clean and efficient code. By identifying code smells and applying refactoring techniques like renaming, extracting methods, and removing duplication, developers can improve the readability, maintainability, and scalability of their code. Test-Driven Development (TDD) provides the safety net needed to refactor confidently.
