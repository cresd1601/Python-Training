# Chapter 1: Getting Started with Test-Driven Development

## Key Concepts:

### 1. What is Test-Driven Development (TDD)?

- A development process where you write tests first, then code to pass the tests, and finally refactor the code.
- Follows the **Red-Green-Refactor** cycle:
  1. **Red**: Write a failing test (since no implementation exists yet).
  2. **Green**: Write the simplest code to make the test pass.
  3. **Refactor**: Clean up the code, improving design and maintainability, while keeping the test passing.

### 2. Differences Between TDD, Unit Testing, and Integration Testing:

- **Unit Testing**: Focuses on testing individual units (e.g., functions, methods) in isolation.
- **Integration Testing**: Tests multiple components working together.
- **TDD**: Focuses on writing tests to drive development and ensures code quality by writing better, testable code.

### 3. First Test Example:

- The book introduces a **Stock Alert** application.
- **Test Case**: Write a test to ensure a new stock object has no price initially.

  ```python
  def test_price_of_a_new_stock_class_should_be_None(self):
      stock = Stock("GOOG")
      self.assertIsNone(stock.price)
  ```

### 4. Failing Test (Red Phase):

- Run the test, and it should fail because the `Stock` class is not implemented.
- Failing tests are expected in the **Red** phase.

### 5. Make the Test Pass (Green Phase):

- Implement the `Stock` class to make the test pass:

  ```python
  class Stock:
      def __init__(self, symbol):
          self.symbol = symbol
          self.price = None
  ```

- Run the test again, and it should pass.

### 6. Refactor the Code (Refactor Phase):

- After the test passes, refactor the code if necessary. Since the code is minimal in this example, there's no immediate need to refactor.

### 7. Organizing Test Code:

- Tests should be organized separately from the main code. Two common patterns:
  - Separate directory for tests (e.g., `tests/`).
  - Submodule for tests within the main module (e.g., `module/tests/`).

### 8. Running Tests:

- Use Python’s `unittest` framework to run the tests:

  ```bash
  python -m unittest discover
  ```

## Summary:

- TDD is more than just testing; it improves design and maintainability.
- The **Red-Green-Refactor** cycle ensures continuous verification of code functionality while encouraging better design.
- Tests should focus on small, testable pieces of functionality, and the code should be refactored to improve quality.

This chapter introduces the basic concepts of TDD and guides you through writing your first test-driven implementation.
