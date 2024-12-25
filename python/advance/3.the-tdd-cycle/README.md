
# Chapter 2: Red-Green-Refactor – The TDD Cycle

## Key Concepts:

### 1. Tests as Executable Requirements:
- In TDD, tests serve as **executable requirements**. This means that writing tests before code helps define and clarify the exact behavior expected from the code.
- Requirements and tests are interchangeable in TDD, meaning once a test is passing, the corresponding requirement is fulfilled.
  
  > *Tests are living documentation* because they ensure that what is specified in the test aligns with what the code does. Any divergence results in a test failure.

### 2. The Red-Green-Refactor Cycle:
- **Red**: Start by writing a test that defines a small piece of functionality. Since no code exists yet, the test should fail.
- **Green**: Write the minimum amount of code necessary to make the test pass. Don’t worry about code quality at this point; just focus on getting the test to pass.
- **Refactor**: Improve the code’s design and maintainability while ensuring that the test remains passing.

  Example:
  
  ```python
  def test_stock_price_initially_none(self):
      stock = Stock("GOOG")
      self.assertIsNone(stock.price)
  ```

  - Red: The test will fail because there is no \`Stock\` class.
  - Green: Implement the \`Stock\` class minimally, just to make the test pass.
  
  ```python
  class Stock:
      def __init__(self, symbol):
          self.symbol = symbol
          self.price = None
  ```

  - Refactor: After ensuring the test passes, improve the code structure if necessary.

### 3. Arrange-Act-Assert Pattern:
- **Arrange**: Set up the environment or context for the test.
- **Act**: Perform the action you want to test.
- **Assert**: Verify the outcome.
  
  Example:

  ```python
  def test_stock_update(self):
      goog = Stock("GOOG")
      goog.update(datetime(2014, 2, 12), price=10)
      self.assertEqual(10, goog.price)
  ```

  - **Arrange**: Create a stock object.
  - **Act**: Update the stock with a new price.
  - **Assert**: Verify the updated price matches what was set.

### 4. Testing for Exceptions:
- TDD involves testing both the **expected behavior** and handling of **error conditions**.
- Use \`assertRaises\` to check for exceptions. For example, if a stock price cannot be negative, write a test to ensure this:

  ```python
  def test_negative_price_should_throw_ValueError(self):
      goog = Stock("GOOG")
      with self.assertRaises(ValueError):
          goog.update(datetime(2014, 2, 13), price=-1)
  ```

- This verifies that the code correctly raises a \`ValueError\` when a negative price is provided.

### 5. Exploring Assert Methods:
- The \`unittest\` module provides many assertion methods, such as:
  - \`assertEqual()\`: Verify two values are equal.
  - \`assertTrue()\` / \`assertFalse()\`: Check boolean conditions.
  - \`assertRaises()\`: Ensure an exception is raised.
  - \`assertAlmostEqual()\`: Useful for comparing floating-point numbers.

  Example:

  ```python
  def test_stock_price_should_give_the_latest_price(self):
      goog = Stock("GOOG")
      goog.update(datetime(2014, 2, 12), price=10)
      goog.update(datetime(2014, 2, 13), price=8.4)
      self.assertAlmostEqual(8.4, goog.price, delta=0.0001)
  ```

  - This test ensures the latest stock price is accurately reflected after updates.

### 6. Refactoring the Design:
- TDD enables safe refactoring. Once tests are in place, you can confidently refactor your code to improve its design, knowing that the tests will catch any errors you introduce.
- For example, you might refactor the \`Stock\` class to store price history, rather than just the latest price:

  ```python
  class Stock:
      def __init__(self, symbol):
          self.symbol = symbol
          self.prices = []
  
      def update(self, timestamp, price):
          if price < 0:
              raise ValueError("Price cannot be negative")
          self.prices.append((timestamp, price))
  
      @property
      def price(self):
          return self.prices[-1][1] if self.prices else None
  ```

  - This change allows the \`Stock\` class to store a history of prices while still passing the original tests.

### 7. Refactoring Tests:
- Tests themselves also need refactoring to avoid duplication and ensure clarity.
- Use \`setUp\` and \`tearDown\` methods to simplify repeated setup or teardown code across multiple tests.

  ```python
  def setUp(self):
      self.goog = Stock("GOOG")

  def test_stock_price_initially_none(self):
      self.assertIsNone(self.goog.price)

  def test_stock_update(self):
      self.goog.update(datetime(2014, 2, 12), price=10)
      self.assertEqual(10, self.goog.price)
  ```

  - \`setUp\` ensures each test starts with a fresh \`Stock\` object, reducing code duplication.

### 8. Avoiding Brittle Tests:
- Brittle tests are fragile and break when internal implementations change, even if the functionality remains correct.
- To avoid brittle tests:
  - Test the **public interface** rather than internal implementation details.
  - Avoid hardcoding specifics about internal states that may change with refactoring.

## Summary:

- Chapter 2 explores the TDD process through the **Red-Green-Refactor** cycle.
- The chapter emphasizes how tests act as executable requirements and how the **Arrange-Act-Assert** pattern simplifies test structure.
- It also explains testing for exceptions, using various assert methods, and refactoring both code and tests.
- Finally, it warns against brittle tests, encouraging testing public interfaces to ensure that changes to the codebase don’t unnecessarily break the tests.

This chapter deepens the understanding of the TDD cycle, providing the foundation for writing clean, maintainable, and robust code while supporting safe refactoring.
