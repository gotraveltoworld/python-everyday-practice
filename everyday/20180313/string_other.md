# Python string example.

* All functions: https://repl.it/@Traveler/Python-String-practice-All

Reference:
1. https://pyformat.info/
2. http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-1-numeric-types-and-string/

Study the format function.
1. string format method(set key-value)

## str_format.py
```python
import sys

# Show current os environment.
def show_platform():
    sys_platform = sys.platform
    print('My platform is {os_env}'.format(os_env=sys_platform))
```