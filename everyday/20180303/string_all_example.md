# Python string example.
All string(from basic to advantage)： https://repl.it/@Traveler/Python-String-practice-All

> 加入islower(), isupper(), split()

## basic.py
```python

# is_lower
def has_lower(text):
    for c in text:
        if c.islower():
            return True
    return False

# is_upper
def has_upper(text):
    for c in text:
        if c.isupper():
            return True
    return False

# split string by specify symbol
def str_split(text, symbol=','):
    return text.split(symbol)

```
## main.py
```python
from basic import simple_case, traversal_str, reversed_print_text, show_concatenation, find, count, str_replace, str_strip, str_reversed
from advantage import is_palindrome
# Reference:
# 1. https://stackoverflow.com/questions/4041238/why-use-def-main
# 2. http://technology-sea.blogspot.tw/2012/03/python-name-import.html
# 3. https://openhome.cc/Gossip/Python/StringType.html
# 4. https://docs.python.org/3/library/stdtypes.html#string-methods
"""可以用__name__來判斷該程式是否被import或是直接執行。
"""
if __name__ == '__main__':
    # basic
    simple_case()

    # is_palindrome
    print(is_palindrome('bye'))
    print(is_palindrome('noon'))
    # Use new to replace old string.
    print(str_replace('Hi! I am John.', 'John', 'Mark'))
    # Strip both space.
    print(str_strip(' Bye '))
    # Reversed string.
    print(str_reversed('Hi! I am John.'))

    sentence = 'My name is John.'
    print(has_lower(sentence))
    print(has_upper(sentence))

    print(str_split(sentence, ' '))
```