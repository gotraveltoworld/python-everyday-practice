# Python string example.

* Basic function: https://repl.it/@Traveler/Python-String-practice-All

Study the format function.
1. format methd for (set key-value)

## str_format.py
```python
import sys

# Show current os environment.
def show_platform():
    sys_platform = sys.platform
    print('My platform is {os_env}'.format(os_env=sys_platform))
```