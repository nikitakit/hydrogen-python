# Python language-specific extensions for Hydrogen

Features:
* Variable explorer (see [nteract/hydrogen#64]( https://github.com/nteract/hydrogen/issues/64))
* Allows running code with common leading whitespace when there are empty lines at the start (see [nteract/hydrogen#862]( https://github.com/nteract/hydrogen/issues/862))
* Extend executable code to include `else` clauses, decorators, and more (experimental, must be manually enabled in the package settings)

Compatibility:
* [Hydrogen](https://github.com/nteract/hydrogen) version 2.3.0 or later
* Variable explorer has only been tested to work with Python 3.5 or later. Pull requests to add Python 2 support are welcome.

## Feature: Variable Explorer

Activate using the _"Hydrogen Python: Toggle Variable Explorer"_ command.

This feature is currently in proof-of-concept status. Please file an issue about any functionality you want to have in the variable exploror!

## Feature: Extend Executable Code [experimental]

When a line is executed without selection, hydrogen only passes on code up that is indented compared to the current line.
In python that unfortunately does not always work, because some control structures (e.g. else) continue on the same indentation level.
For example, the following code block would only execute the `if` statement, but not the `else` statement when the `Run and Move Down` or the `Run` commands are used.

```python
if False:
    print('False')
else:
    print('True')
# with `Run` or `Run and Move Down`
# there is no output in standard hydrogen
# as the else block is not included
```

Enabling the setting `Extend Executable Code` (by default it is disabled!) expands the executed code beyond what hydrogen suggests on the basis of the indentation level.
A list of strings for which the code is extended can be defined.
In the default setting, `else`, `elif`, `except`, `finally`, as well as all closing braces are included in the expansion.

**Warning:** Note with all this, that as of now the hydrogen tick markers are unfortunately _not_ moved to the right location. They still remain where the original code selection of hydrogen ended.

When enabling the setting, examples like the following should work as expected:

```python
someDictionary = {
    'one': 1
}

someList = [
    1,
    2,
    3
]

foo(
    argument1,
    argument2
)
# in hydrogen each of these would throw an error
# because the closing brace is not included
# as it is on the same indentation level
```

```python
if False:
    pass
elif False:
    pass
else:
    print('executed')
# in hydrogen this would only execute the
# if-statement as elif and else are not extended
```

```python
try:
    throw(IndentationError)
except:
    print('some error occurred')
finally:
    print('finally')
# in hydrogen this would only raise an error but not
# execute the except and finally blocks
```

### Extension to the Top (e.g. for decorators)

In the second configuration field, expansion towards the top is defined.
The preset is to extends decorators (`@`) of functions, so that the following example works when selecting either the line with the decorator or with the function definition and executing via `run` or `run-and-move-down`.

```python
def deco(f):
    return lambda x: f(x + 1)

@deco
def myfunc(x):
    return 1 / x

myfunc(0)
```

Contrary to the expansion to the bottom, this _does not_ automatically include comments, or further indentation, but only the immediate match.
The following example thus would not work with the default settings, but could easily be enabled by adding `#` to the list:

```python
@deco
# comment
def myfunc(x):
    return 1 / x
```

### Customisation

You can extend this list by your choice.
Make sure you check that the behaviour has no unintended circumstances;
`hydrogen-python` logs to the console when code is extended.
One possibly useful addition can be to add `plt\.` to the list, so that the following code block can be run without having to select lines independently:

```python
plt.plot()
plt.xlabel()
plt.ylabel()
plt.show()
```
