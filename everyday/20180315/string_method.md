# Python string example.

* Basic function: https://repl.it/@Traveler/Python-String-practice-All
* Reference: https://www.tutorialspoint.com/python/python_strings.htm
Study the format function.
* Some of string method
    - strip(), rstrip(), lstrip(): 去除左右的空白
    - capitalize(): 首字母轉換成大寫
    - swapcase(): 小寫轉大寫，大寫轉小寫

## str_format.py
```python
def basic_method(text=' my name is Traveler. '):
    print(text.strip()) # My name is Traveler.
    print(text.strip().capitalize()) # My name is Traveler.
    print(text.strip().swapcase()) # My name is Traveler.

```