# Chapter 8: Extending unittest with nose2

## Overview:

This chapter introduces the `nose2` test runner, which extends Python's built-in `unittest` framework by providing additional functionality and ease of use. `nose2` simplifies test discovery, parameterized testing, and code coverage while integrating with existing `unittest` code, allowing for a seamless transition from `unittest` to `nose2`.

## Key Concepts:

### 1. Getting Started with nose2:

`nose2` can be installed easily using `pip install nose2`, and it functions as a drop-in replacement for the standard `unittest` runner. It autodiscovers and runs tests without requiring any changes to the existing test structure.

### 2. Writing Tests for nose2:

- Tests can be written as regular functions, eliminating the need for test classes that inherit from `unittest.TestCase`.
- The standard `assert` statements in Python can be used in place of `unittest`'s assertion methods.
  
Example:

```python
def test_price_of_a_new_stock_class_should_be_None():
    goog = Stock("GOOG")
    assert goog.price is None
```

### 3. Setup and Teardown:

`nose2` also supports setup and teardown for function-based tests, where `setup` and `teardown` functions are attached to the test functions:

```python
def setup_test():
    global goog
    goog = Stock("GOOG")

def teardown_test():
    global goog
    goog = None

test_price_of_a_new_stock_class_should_be_None.setup = setup_test
test_price_of_a_new_stock_class_should_be_None.teardown = teardown_test
```

### 4. Parameterized Tests:

`nose2` supports parameterized (data-driven) tests, where the same test is run with different data inputs:

```python
from nose2.tools.params import params

@params(
    ([8, 10, 12], True),
    ([8, 12, 10], False)
)

def test_stock_trends(prices, expected_output):
    goog = Stock("GOOG")
    given_a_series_of_prices(goog, prices)
    assert goog.is_increasing_trend() == expected_output
```

### 5. Generated Tests:

Generated tests are similar to parameterized tests but can be created dynamically during runtime:

```python
def test_trend_with_all_consecutive_values_upto_100():
    for i in range(100):
        yield stock_trends_with_consecutive_prices, [i, i+1, i+2]
```

### 6. Layers:

Layers allow for hierarchical organization of tests, sharing fixtures between parent and child layers. This helps reduce repetitive setup code across different test cases.

### 7. Plugins:

`nose2` offers a rich set of plugins that extend its functionality, such as support for running doctests, generating XML test results, and measuring test coverage. These plugins can be configured via command-line options or by using a configuration file (`nose2.cfg`).

### 8. Measuring Test Coverage:

To measure test coverage, the `coverage` plugin can be enabled:

```bash
nose2 --with-coverage --coverage-report html
```

This generates a detailed coverage report that can be viewed in a browser.

## Best Practices:

- **Simplify test writing**: Use function-based tests and regular assertions to reduce boilerplate code.
- **Parameterize tests**: Reuse test logic with different inputs using parameterized tests.
- **Organize tests with layers**: Use layers to share fixtures and reduce duplication across tests.
- **Utilize plugins**: Leverage `nose2` plugins for enhanced functionality, such as code coverage and XML reporting.

## Example Code:

```python
from nose2.tools.params import params

@params(
    ([8, 10, 12], True),
    ([8, 12, 10], False)
)

def test_stock_trends(prices, expected_output):
    goog = Stock("GOOG")
    given_a_series_of_prices(goog, prices)
    assert goog.is_increasing_trend() == expected_output
```

## Summary:

Chapter 8 discusses the power and flexibility of `nose2` as an extended test runner for Python’s `unittest` framework. It simplifies test writing, enhances test discovery, and supports a variety of testing techniques such as parameterized tests, generated tests, and test coverage measurement. `nose2` integrates smoothly with existing `unittest` code, making it an effective tool for both new and legacy projects.
