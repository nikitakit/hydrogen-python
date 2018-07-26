# :package: Python language-specific extensions for Hydrogen

Features:
* Attempts to strip common leading whitespace (see [nteract/hydrogen#862]( https://github.com/nteract/hydrogen/issues/862))
* Variable explorer (see [nteract/hydrogen#64]( https://github.com/nteract/hydrogen/issues/64))

Compatibility:
* [Hydrogen](https://github.com/nteract/hydrogen) version 2.3.0 or later
* Variable explorer has only been tested to work with Python 3.5 or later. Pull requests to add Python 2 support are welcome.

## Feature: Strip common leading whitespace

Lets you select and run code blocks that are indented (e.g. inside a function). No configuration needed.

Example:

```python
def foo():
    x = 1
    print('x is', x)
    # Select the above two lines and run them with Hydrogen!
```

There is also an experimental option to expand the code passed on by hydrogen to include else/elif or closing brackets, which until now is only possible when selecting the code.
However, the tick mark can not be moved to the right location as of yet.

## Feature: Variable Explorer

Activate using the _"Hydrogen Python: Toggle Variable Explorer"_ command.

This feature is currently in proof-of-concept status. Please file an issue about any functionality you want to have in the variable exploror!
