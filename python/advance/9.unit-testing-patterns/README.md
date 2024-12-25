# Chapter 9: Unit Testing Patterns

## Overview:

Chapter 9 of _Test-Driven Python Development_ explores various patterns in unit testing that help optimize the process of writing and maintaining tests. These patterns focus on speeding up tests, running specific subsets of tests, and improving test organization using attributes, data-driven tests, and mocking techniques. The chapter also covers strategies for integration testing and asserting sequences of method calls.

## Key Concepts:

### 1. Fast Tests:

The chapter emphasizes the importance of keeping tests fast. Slow tests can hinder frequent test execution and feedback loops, which are essential in Test-Driven Development (TDD). Fast tests ensure that developers can run tests frequently and get quick feedback without interrupting the flow of development.

### 2. Running a Subset of Tests:

Instead of running the entire test suite, developers can run specific tests or subsets of tests to focus on a particular feature or functionality. This can be done using test loaders, attributes, or skipping certain tests.

- **Test Loaders**: Test loaders allow for selecting and running specific test cases or suites, based on certain criteria.
- **Skipping Tests**: Tests can be conditionally skipped using decorators like `@unittest.skipIf` or `@unittest.skipUnless`, which is helpful when a test should only run under specific conditions.

### 3. Using Attributes:

Attributes provide a flexible way to categorize and run tests based on certain characteristics. By adding attributes to test methods or classes, developers can select and run only tests with matching attributes.

```python
@unittest.skip("Not implemented yet")
def test_future_feature():
    pass
```

### 4. Expected Failures:

Tests can be marked as expected to fail using the `@unittest.expectedFailure` decorator. This pattern is useful when certain tests are expected to fail due to known issues or incomplete features, without failing the entire test suite.

```python
@unittest.expectedFailure
def test_known_bug():
    # Test code for a known bug
    pass
```

### 5. Data-Driven Tests:

Data-driven tests (or parameterized tests) allow the same test logic to be run with different sets of input data. This reduces code duplication and helps validate multiple scenarios using the same test function.

```python
@unittest.subTest(price=[8, 10, 12])
def test_stock_trends(self):
    goog = Stock("GOOG")
    goog.update_prices([8, 10, 12])
    self.assertTrue(goog.is_increasing_trend())
```

### 6. Integration and System Tests:

Integration tests ensure that different units of the application work well together, while system tests check the overall functionality of the system. These types of tests are generally slower but are necessary to validate the application's end-to-end behavior.

### 7. Spies:

Spies are used to verify that certain methods or functions were called with the expected arguments during a test. This pattern is helpful when testing code that interacts with other components.

```python
with unittest.mock.patch('module.method') as spy:
    instance.do_something()
    spy.assert_called_once_with(expected_argument)
```

### 8. Asserting a Sequence of Calls:

When testing complex interactions between objects, asserting that methods are called in a specific sequence is crucial. This can be done using mocking frameworks that allow tracking method calls and their order.

```python
mock_object.method.assert_has_calls([
    unittest.mock.call(arg1),
    unittest.mock.call(arg2),
])
```

### 9. Patching the Open Function:

A common use case in testing is mocking file I/O operations. Patching the `open` function allows you to simulate reading from or writing to files without actually performing file operations.

```python
with unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data="data")):
    with open('file.txt') as f:
        result = f.read()
    assert result == "data"
```

### 10. Mocking with Mutable Arguments:

Handling mutable arguments in mocks can be tricky. The chapter covers techniques for ensuring that changes to mutable arguments in a mock are properly reflected during testing.

```python
mock_instance.method.assert_called_once_with(mock.ANY)
```

## Best Practices:

- **Keep tests fast**: Ensure that unit tests run quickly to encourage frequent execution during development.
- **Use parameterized tests**: Leverage data-driven tests to reduce code duplication and validate multiple scenarios.
- **Organize tests using attributes**: Use attributes and decorators to categorize and selectively run tests.
- **Mock dependencies effectively**: Use spies and mocks to test interactions between objects and assert call sequences.
- **Handle mutable arguments carefully**: Ensure mutable arguments in mocks behave as expected during tests.

## Example Code:

```python
@unittest.subTest(price=[8, 10, 12])
def test_stock_trends(self):
    goog = Stock("GOOG")
    goog.update_prices([8, 10, 12])
    self.assertTrue(goog.is_increasing_trend())
```

## Summary:

Chapter 9 provides practical unit testing patterns that help write better tests and maintain a robust test suite. It emphasizes the importance of fast tests, running targeted subsets of tests, using data-driven testing, and leveraging mocks effectively. The patterns introduced in this chapter, such as asserting sequences of calls and patching functions, contribute to writing more focused and reliable tests for Python applications.
