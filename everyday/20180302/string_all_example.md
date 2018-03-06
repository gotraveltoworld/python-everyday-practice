# Python string example.
All string(from basic to advantage)： https://repl.it/@Traveler/Python-String-practice-All

> 整理字串處理相關的方法，並練習用不同檔案引入的方式呈現專案。

## basic.py
```python
def simpla_case():
    # Simple case.
    fruit = 'banana'
    print(fruit[0])
    # b
    # Reversed, to use the negative index.
    print(fruit[-1])
    # a

# Traversal all string by while loop.
def traversal_str(fruit):
    index = 0
    while index < len(fruit):
        print(fruit[index])
        index += 1

def reversed_print_text(text):
    index = 0
    while index > -len(text):
        print(text[index])
        index -= 1

# Concatenation
def show_concatenation():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            letter += 'u'
        print(letter + suffix)

    # String segment.
    print(fruit[0:3])# from index 0 to (3-1)
    print(fruit[:3]) # from index 0 to (3-1)
    print(fruit[0:]) # from index 0 to end
    print(fruit[:]) # All string


# String search(find function)
def find(words, letter, strat=0):
    for index, word in enumerate(words[strat:]):
        if word == letter:
            return index
    return -1

# Count letter number.
def count(words, letter, strat=0):
    conuts = 0
    for word in words[strat:]:
        if word == letter:
            conuts += 1
    return conuts
```
### advantage.py
```python
# Reference: 'https://openhome.cc/Gossip/Python/StringType.html'
# palindrome <= 迴文
# noon, redivider
def is_palindrome(word):
    return word[::-1] == word
```

## main.py
```python
from basic import simpla_case, traversal_str, reversed_print_text, show_concatenation, find, count
from advantage import is_palindrome

# Reference:
# 1. https://stackoverflow.com/questions/4041238/why-use-def-main
# 2. http://technology-sea.blogspot.tw/2012/03/python-name-import.html
"""
可以用__name__來判斷該程式是否被import或是直接執行。
"""
if __name__ == '__main__':
    # basic
    simpla_case()

    # is_palindrome
    print(is_palindrome('bye'))
    print(is_palindrome('noon'))
```