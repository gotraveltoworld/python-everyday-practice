# Python's string format.
* Basic function: https://repl.it/@Traveler/Python-String-practice-All
* Template string: https://docs.python.org/3.6/library/string.html#template-strings

```python
from string import Template
# * substitute
# * safe_substitute: instead of raising a KeyError exception
def print_tempalate():
    s = Template('$who likes $what')
    print(s.substitute(who='John', what='apples'))
    # John likes apples
```