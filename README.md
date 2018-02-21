# :package: Python language-specific extensions for Hydrogen

Features:
* Attempts to strip common leading whitespace (see [nteract/hydrogen#862]( https://github.com/nteract/hydrogen/issues/862))
* Variable explorer (see [nteract/hydrogen#64]( https://github.com/nteract/hydrogen/issues/64))

Compatibility:
* [Hydrogen](nteract/hydrogen) installed from master. Version 2.3 or later will work (but Hydrogen 2.3 hasn't been released yet).
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

### Limitations

Does not work if the first line ends in `:` and you have a comment after, i.e.

```python
if True: # having a comment here breaks things
    print("This doesn't work!")
```

It also can have unexpected results if you select some code that is malformed to begin with, e.g.

```python
x = 1
    print("x is", x) # This works even though it shouldn't
```

(Pull requests are welcome to fix the first issue; the second probably can't be fixed without changing the Hydrogen package)

## Feature: Variable Explorer

Activate using the _"Hydrogen Python: Toggle Variable Explorer"_ command.

This feature is currently in proof-of-concept status. Please file an issue about any functionality you want to have in the variable exploror!
