# Chapter 7: Executable Documentation with doctest

## Overview:

This chapter introduces the `doctest` module, which allows embedding tests within Python docstrings. It focuses on how to use `doctest` to create executable documentation that can verify code functionality by running examples written within the code's documentation.

## Key Concepts:

### 1. Embedding Tests in Docstrings:

`doctest` allows for embedding examples within Python docstrings, replicating an interactive shell's behavior. These examples are then tested to ensure the correctness of both the documentation and the code. This approach guarantees that documentation stays synchronized with the code, preventing outdated or misleading examples.

### 2. Writing Doctests:

- Tests are written directly in docstrings using the `>>>` prompt for input and expected output.
- `doctest` captures the behavior of Python’s interactive shell, verifying that the code produces the expected result.

### 3. Running Doctests:

`doctest` can be executed by adding a few lines at the bottom of a script. It scans the docstrings, executes the examples, and verifies the output:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This allows tests to be easily integrated into the normal Python workflow.

### 4. Handling Failures:

When a test fails, `doctest` provides detailed information, including the exact line that caused the failure and the difference between the expected and actual output. This helps identify and resolve issues within both the code and the documentation.

### 5. Testing for Exceptions:

The chapter demonstrates how to test for exceptions using `doctest`. Example inputs can include expected exceptions to ensure the correct behavior of error handling in the code.

### 6. Package-level Doctests:

Tests can also be written at the package level, allowing for comprehensive documentation and verification of module interactions. Package-level doctests are particularly useful for testing the interaction between multiple components in a project.

### 7. Maintaining Doctests:

Doctests can become lengthy, especially if they include detailed examples. To keep the code clean, the chapter recommends moving doctests into separate files, which can be run using `doctest.testfile()`.

### 8. Limitations of Doctest:

`doctest` only compares printed output, which can lead to failures if the output is non-deterministic (e.g., memory addresses). The chapter introduces `doctest` directives like `ELLIPSIS` and `NORMALIZE_WHITESPACE` to handle such cases.

## Techniques for Improving Doctest Use:

### 1. Setup and Teardown:

The chapter explains how to set up and tear down the testing environment using the `setUp` and `tearDown` parameters of `doctest.DocTestSuite()` and `doctest.DocFileSuite()`. This helps avoid redundant setup code within each test.

### 2. Using Doctest Directives:

Directives like `ELLIPSIS` allow for partial matching in tests, helping handle outputs that change between runs (e.g., object memory addresses). Other directives like `NORMALIZE_WHITESPACE` can ignore minor formatting differences.

## Best Practices:

- **Embedding meaningful examples**: Doctests should not only test the code but also provide examples that explain the code’s purpose and usage.
- **Separating large doctests**: When doctests become too verbose, separating them into external files can help keep the code clean.
- **Handling complex outputs**: Use directives to manage complex or non-deterministic outputs, ensuring tests remain flexible but accurate.

## Example Code:

Here is an example of a doctest for a simple function:

```python
def price():
    """Returns the current price of the Stock
    
    >>> from datetime import datetime
    >>> stock = Stock("GOOG")
    >>> stock.update(datetime(2011, 10, 3), 10)
    >>> stock.price
    10
    """
    try:
        return self.history[-1].value
    except IndexError:
        return None
```

## Summary:

Chapter 7 highlights the use of `doctest` to create self-documenting code by embedding examples within docstrings. This method helps keep documentation and code synchronized, providing a reliable way to ensure that examples in documentation remain accurate. It discusses practical techniques like handling test failures, organizing doctests in separate files, and using directives to deal with dynamic outputs.
