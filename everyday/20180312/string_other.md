# Python string example.

Reference:
1. https://pyformat.info/
2. http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-1-numeric-types-and-string/

Study the format function.
1. format
2. __str__ and __repr__ function
    * __str__
    * __repr__


## string_other.py
```python
class String(object):

    def __str__(self):
        return 'I am a str function.'

    def __repr__(self):
        return 'I am a repr function.'

# I am a str function. I am a repr function.
```