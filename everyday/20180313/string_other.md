# Python string example.

* Basic regex function: https://repl.it/@Traveler/Python-String-practice-All

Reference:
1. https://pyformat.info/
2. http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-1-numeric-types-and-string/

Study the format function.
1. Padding
    * left
    * right
    * center

## str_format.py
```python
# Padding and aligning strings
def print_format(text='test'):
    # Right
    print('{:>10}'.format(text))

    # Left
    print('{:10}'.format(text))
    print('{:_<10}'.format(text))

    # Center
    print('{:>10}'.format(text))

```